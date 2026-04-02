Risk | Severity | Notes
Global state reliance | High | Heavy use of globals (e.g., $wp_query) causes unpredictable behavior and side effects; mitigation: refactor toward dependency injection and reduce shared mutable state
Plugin security vulnerabilities | High | Third-party plugins may introduce SQL injection or XSS vulnerabilities; mitigation: enforce plugin review, use security scanners, and keep plugins updated
Limited automated testing | High | Low test coverage increases risk of regressions and undetected bugs; mitigation: introduce unit/integration tests for critical modules
Performance bottlenecks | Medium | Expensive queries and excessive hooks degrade performance under load; mitigation: optimize queries, implement caching, and limit unnecessary hooks
Inconsistent coding standards | Medium | Mixed coding styles slow development and increase maintenance errors; mitigation: enforce coding standards (e.g., PSR) and apply linting tools