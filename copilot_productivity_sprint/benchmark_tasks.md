## Task 1 - Create Group
**Requirements**: Implement functionality to create a new group with a unique group code.  
**Inputs**: JSON {group_name, creator_id}  
**Outputs**: Created group with id and generated group_code  
**Acceptance Criteria**:  
- Group is stored in database  
- Unique group_code is generated  
- Returns 201 on success  
- Returns 400 if input is invalid  

## Task 2 - Join Group with Code
**Requirements**: Allow a user to join a group using a valid group code.  
**Inputs**: JSON {user_id, group_code}  
**Outputs**: User added to group membership  
**Acceptance Criteria**:  
- User is added to the group if code is valid  
- Returns 200 on success  
- Returns 404 if group_code does not exist  
- Prevent duplicate membership  

## Task 3 - Add Expense
**Requirements**: Implement functionality to add a new expense to a group.  
**Inputs**: JSON {group_id, amount, description, paid_by, participants[]}  
**Outputs**: Stored expense with calculated shares  
**Acceptance Criteria**:  
- Expense is saved in database  
- Participants are correctly associated  
- Equal split is calculated correctly  
- Returns 201 on success  
- Returns 400 if required fields are missing  