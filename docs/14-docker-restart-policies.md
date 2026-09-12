# Lesson 14 — Docker Restart Policies

## 1. What is a Restart Policy?

A Docker restart policy tells Docker what to do when a container's main process stops or exits.

Restart policies are configured with the `restart` option.

Example:

```yaml
services:
  app:
    image: my-app
    restart: always
```

The important point is:

> **Restart policies react to the container's main process stopping/exiting.**

A restart policy does **not** automatically restart a container just because its healthcheck reports `unhealthy`.

---

## 2. `restart: no`

```yaml
restart: "no"
```

This is the default behavior.

Docker does not automatically restart the container when it stops.

```text
Container stops
      ↓
No automatic restart
```

---

## 3. `restart: on-failure`

```yaml
restart: on-failure
```

Docker restarts the container when the main process exits with a non-zero exit code.

For example:

```text
Application crashes
      ↓
Exit code: 1
      ↓
Docker restarts container
```

However, if the application exits successfully with exit code `0`, Docker does not restart it.

```text
Exit code 0 → No restart
Exit code 1 → Restart
Exit code 2 → Restart
```

---

## 4. `restart: on-failure:N`

A maximum number of restart attempts can be specified.

Example:

```yaml
restart: on-failure:3
```

This means Docker can restart the container up to 3 times when the main process fails.

Example:

```text
Application starts
      ↓
Crash
      ↓
Restart #1
      ↓
Crash
      ↓
Restart #2
      ↓
Crash
      ↓
Restart #3
      ↓
No more restart attempts
```

The number `3` here is related to **restart attempts**, not healthcheck retries.

---

## 5. `restart: always`

```yaml
restart: always
```

Docker automatically restarts the container when it stops.

This includes cases where the main process exits successfully.

For example:

```text
Container stops
      ↓
Docker restarts container
```

However, an unhealthy healthcheck by itself does not cause `restart: always` to restart the container.

Example:

```yaml
services:
  app:
    image: my-app
    restart: always
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000"]
```

If:

```text
Container: Running
Health: Unhealthy
```

the container is still running, so the restart policy does not restart it simply because the healthcheck failed.

---

## 6. `restart: unless-stopped`

```yaml
restart: unless-stopped
```

This behaves similarly to `always`, except that Docker will keep the container stopped if I manually stop it.

For example:

```text
Application crashes
      ↓
Docker restarts container
```

But:

```bash
docker stop app
```

means:

```text
Manual stop
      ↓
Container stays stopped
```

---

## 7. Restart Policy Comparison

| Policy           | Crash / non-zero exit | Exit `0` |   Manually stopped |
| ---------------- | --------------------: | -------: | -----------------: |
| `no`             |                     ❌ |        ❌ |                  ❌ |
| `on-failure`     |                     ✅ |        ❌ |                  ❌ |
| `always`         |                     ✅ |        ✅ | Generally restarts |
| `unless-stopped` |                     ✅ |        ✅ |                  ❌ |

---

## 8. Restart Policy vs Healthcheck

These are two different mechanisms.

### Restart policy

Answers:

> **What should Docker do when the container stops?**

### Healthcheck

Answers:

> **Is the application healthy/ready?**

For example:

```text
Healthcheck fails
      ↓
Container becomes Unhealthy
      ↓
Container may still be Running
      ↓
Restart policy does not automatically restart it
```

Therefore:

> **Healthcheck failure and container restart are not the same thing.**

---

## 9. Important Distinction: Healthcheck Retries vs Restart Attempts

These two settings can look similar but have different purposes.

Healthcheck:

```yaml
healthcheck:
  retries: 3
```

means Docker can tolerate repeated failed healthcheck attempts before marking the container as unhealthy.

Restart policy:

```yaml
restart: on-failure:3
```

means Docker can restart the container up to 3 times after main-process failures.

They are independent concepts.

---

## 10. Key Takeaways

* `restart: no` → do not automatically restart.
* `restart: on-failure` → restart when the main process fails.
* `restart: on-failure:3` → restart up to 3 times after failures.
* `restart: always` → restart when the container stops.
* `restart: unless-stopped` → restart when the container stops unless I manually stopped it.
* Restart policies are based on the container's main process stopping/exiting.
* A healthcheck reporting `unhealthy` does not by itself trigger a restart.
* `healthcheck.retries` and `restart:on-failure:N` control different things.

### Mental Model

```text
                 Docker Container
                       │
              ┌────────┴────────┐
              │                 │
         Main Process       Healthcheck
              │                 │
        stops / exits      healthy / unhealthy
              │                 │
              ↓                 ↓
       Restart Policy       Health Status
```

