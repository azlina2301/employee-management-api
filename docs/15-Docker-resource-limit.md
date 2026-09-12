# Lesson 15 — Docker Resource Limits

## 1. Why Resource Limits Matter

Docker containers share the resources of the host machine.

For example, if the host has:

```text
8 GB RAM
```

and one container suddenly consumes 7 GB, other containers and processes may be affected.

Without resource limits, one badly behaved container can consume a large amount of the host's available resources.

---

## 2. Memory Limits

Docker can limit how much memory a container is allowed to use.

Example:

```yaml
services:
  app:
    image: my-app
    mem_limit: 512m
```

This means:

> The container has a memory limit of 512 MB.

The limit is a **ceiling**, not a guaranteed allocation.

For example:

```text
Memory
  ↑
800 MB ─── ❌ Beyond limit
  │
512 MB ─── 🚧 Memory limit
  │
300 MB ─── Application usage
  │
  0 MB
```

If the application tries to use more memory than the configured limit, it may be terminated because of an **out-of-memory (OOM)** condition.

---

## 3. CPU Resources

Containers also share the host's CPU resources.

For example:

```text
Mac: 8 CPU cores

Container A → CPU-intensive workload
Container B → Employee API
```

If Container A consumes a large amount of CPU, Container B may become slower because both containers compete for the host's CPU resources.

Docker allows us to limit CPU consumption.

Example:

```yaml
services:
  app:
    image: my-app
    cpus: 1.0
```

Conceptually, this means:

> Allow the container to use up to approximately one CPU's worth of processing capacity.

---

## 4. CPU Limit Is Not a Physical CPU Assignment

A CPU limit does not mean Docker assigns a specific physical CPU core to the container.

For example:

```yaml
cpus: 1.0
```

does **not** mean:

```text
CPU Core #1 → Container A
```

Instead, it limits the amount of CPU processing capacity the container can consume.

It is better to think of it as a **CPU capacity limit** rather than a physical-core assignment.

---

## 5. CPU and Memory Behave Differently

CPU and memory limits are both resource constraints, but exceeding them can have different consequences.

### CPU

If a container tries to use more CPU than its configured limit:

```text
CPU usage exceeds limit
        ↓
CPU is throttled
```

The application may become slower.

### Memory

If a container tries to exceed its memory limit:

```text
Memory usage exceeds limit
        ↓
Memory pressure / OOM condition
        ↓
Process may be killed
```

Therefore:

> **CPU over the limit → throttling.**

> **Memory over the limit → potentially OOM-killed.**

---

## 6. Example: CPU and Memory Together

We can configure both limits:

```yaml
services:
  app:
    image: my-app
    cpus: 1.0
    mem_limit: 512m
```

This gives the container:

```text
CPU limit    → approximately 1 CPU's worth of capacity
Memory limit → 512 MB
```

The application cannot simply request additional resources and cause Docker to automatically increase these limits.

---

## 7. Resource Limits and Shared Resources

Containers do not have completely independent physical resources.

They share resources from the host:

```text
                  Host Machine
              8 CPU cores / 8 GB RAM
                       │
          ┌────────────┼────────────┐
          │            │            │
      Container A  Container B   Container C
          │            │            │
       CPU/RAM      CPU/RAM      CPU/RAM
```

Resource limits help prevent one container from consuming an excessive amount of the host's resources.

---

## 8. Key Takeaways

* Containers share the host's CPU and memory.
* Without resource limits, one container can consume a large amount of host resources.
* `mem_limit` places a ceiling on memory usage.
* Exceeding a hard memory limit can result in an OOM kill.
* `cpus: 1.0` represents approximately one CPU's worth of processing capacity.
* A CPU limit does not assign a specific physical CPU core to a container.
* CPU overuse is generally handled through throttling.
* Memory overuse can result in an OOM kill.
* CPU and memory limits are independent constraints.

## Mental Model

```text
                    Host Resources
                         │
             ┌───────────┴───────────┐
             │                       │
            CPU                    Memory
             │                       │
       CPU capacity             Memory ceiling
             │                       │
        ┌────┴────┐             ┌────┴────┐
        │         │             │         │
    Container A Container B  Container A Container B
        │         │             │         │
      Limit     Limit         Limit     Limit
```

The purpose of resource limits is to control how much of the host's shared resources each container can consume.
