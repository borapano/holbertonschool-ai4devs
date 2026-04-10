## Reviewer Comments

- In-memory filtering can produce incorrect results when data is partially loaded or large; filtering should be moved closer to the data source to ensure correctness and consistency.
- No strict validation is applied to `category`, allowing invalid values to enter the filtering pipeline and produce misleading empty results.
- User authorization is not enforced inside the filtering logic, which may allow unauthorized access to data in multi-user scenarios.
- Error handling does not differentiate between an empty result set and invalid input, which can lead to incorrect system behavior.
- Business logic is mixed with filtering logic, reducing testability and making it harder to isolate filtering behavior for debugging or unit testing.
- String normalization is performed repeatedly during iteration, which can introduce unnecessary processing overhead and inconsistent comparisons.
- Null or undefined dataset inputs are not explicitly handled, which may cause runtime failures in production.
- API behavior for edge cases (empty dataset, invalid category) is not explicitly defined, leading to inconsistent client-side handling.