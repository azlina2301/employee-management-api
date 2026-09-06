# Docker Healthcheck

## 1. Container Started vs Application Ready
Starting container doesn't mean the application inside it is ready to accept connection.

## 2. What is a Healthcheck
Healthcheck check whether the application inside the container is healthy or ready according to the test specified.

## 3. depends_on vs service_healthy
depends_on control the start-up order, while service_healthy allows compose to wait until the dependency healthcheck report healty.

## 4. Healthcheck Configuration
interval-->timeout-->retries

## 5. interval
How often the healthcheck runs.

## 6. timeout
how long an individual healthcheck attempt is allowed to run before it is considered failed.

## 7. retries
how many consecutive failed attempts are needed before the health status becomes unhealthy.

## 8. Running vs Healthy
the container still running though it unhealthy.

```yaml
healthcheck:
  test: ["CMD-SHELL", "pg_isready -U postgres"]
  interval: 5s
  timeout: 5s
  retries: 5
  ```
  