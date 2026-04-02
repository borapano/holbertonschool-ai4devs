Risk | Severity | Notes

Global state reliance | High | Core components depend heavily on global variables (e.g., $wp_query), making behavior unpredictable and increasing risk of side effects when multiple plugins/themes interact
Plugin security vulnerabilities | High | Plugins are developed by third parties with varying standards; poorly written plugins can introduce SQL injection, XSS, or privilege escalation risks
Limited automated testing | High | Lack of comprehensive test coverage in legacy areas increases risk of regressions and undetected bugs during updates or refactoring
Performance bottlenecks | Medium | Complex database queries (e.g., WP_Query) and excessive hooks can slow down response times, especially under high traffic or with many plugins installed
Inconsistent coding standards | Medium | Combination of procedural and object-oriented code leads to confusion, harder onboarding, and increased maintenance cost
Lack of strict typing | Medium | Dynamic typing in PHP allows invalid data types to propagate, increasing likelihood of runtime errors and making debugging more difficult