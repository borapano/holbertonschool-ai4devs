# Pull Request: Add Expense Category Filtering Feature

## Summary
This PR introduces a new feature that allows users to filter expenses by category. It adds filtering logic to the backend and integrates it into the existing expense retrieval flow. Users can now retrieve only the expenses that match a specific category, improving usability and data organization.

## Changes
- Added `filter_expenses_by_category()` function in expense service/module
- Updated existing expense retrieval endpoint to accept optional `category` query parameter
- Modified data handling logic to apply filtering when parameter is provided
- Added input validation for category values
- Added 5 new unit tests covering:
  - Valid category filtering
  - No category provided (returns all expenses)
  - Invalid category handling
  - Empty result case
  - Case-insensitive matching

## Context
This feature enhances the Expense Management functionality by allowing users to better organize and view their data. It is especially useful in group expense scenarios where multiple categories (e.g., food, travel, utilities) are involved.

Motivation:
- Improve user experience when dealing with large numbers of expenses
- Enable more granular data access without modifying core structures

Related Issue: #58  
Estimated Size: ~150 LOC

## Testing
- All existing tests pass successfully
- New unit tests added and verified
- Edge cases (empty results, invalid input) covered

## Notes
- Feature is backward-compatible
- No database schema changes required