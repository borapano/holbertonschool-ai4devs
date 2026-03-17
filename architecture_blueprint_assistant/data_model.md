# Data Model

- **User**: id, name, email, role  
- **Group**: id, name, creator_id, group_code  
- **Expense**: id, group_id, description, amount, created_by, date  
- **Participant**: id, expense_id, user_id, share_amount  
- **Payment**: id, expense_id, payer_id, amount, status