# API Requirements – Expense Mate API

## Domain
Collaborative Group Finance & Expense Sharing

## Target Users
- **Developers:** Integrate frontend dashboard with real-time data
- **Group Members:** Manage shared trip/household expenses

## Core Operations
- **Create Group:** Initialize a new group with a unique Invite Code
- **Join Group:** Link a User ID to a Group ID via Invite Code
- **Post Expense:** Log a new transaction (Amount, Category, Payer)
- **Calculate Splits:** Automatically generate debt rows for each member
- **Get Group Summary:** Fetch totals for "Spend Velocity" graphs
- **Get Member Balances:** Fetch +/- standing for the "Members" card
- **Update Expense:** Edit or delete an existing transaction
- **Settle Debt:** Mark specific P2P balances as "Paid"
- **Get User Profile:** Fetch avatar and personal settings
- **Search Ledger:** Filter transactions by date, category, or payer

## Data Rules
- **Currency Accuracy:** All amounts must be stored as Decimals (not Floating Points)
- **Zero-Sum Splitting:** Total of all `share_amount` must equal `total_amount`
- **Unique Membership:** A user cannot join the same group twice
- **Category Validation:** Must belong to predefined list (Food, Transport, etc.)

## Non-Functional
- **Real-time Latency:** Push notifications for new expenses < 500ms
- **Authentication:** Supabase Auth / JWT required for all private endpoints
- **Data Integrity:** Transactional "All-or-Nothing" writes for expense + split creation