## Reviewer Comments

- Missing architectural separation between controller, service, and data layers, reducing long-term scalability and maintainability.
- Business logic is tightly coupled with filtering logic, making the code harder to test and extend in future iterations.
- Security issue: user authorization is not explicitly enforced in the filtering flow, risking potential cross-user data access in multi-user environments.
- Input validation for `category` is incomplete; no strict whitelist or schema enforcement is applied.
- Error handling is inconsistent; invalid inputs may return silent failures (empty results) instead of structured error responses.
- Performance concern: filtering is done in-memory instead of at the database/query level, which will not scale with larger datasets.
- Repeated string normalization inside loops introduces unnecessary overhead and should be extracted into a helper function.
- Logging may expose sensitive information (user identifiers or financial data), which is unsafe for production environments.
- Test coverage is incomplete for edge cases such as null inputs, empty datasets, and invalid categories.
- API contract is not clearly defined, making integration with frontend or external services ambiguous.