## User Stories

- **Original**: As a corporate employee, I want to find colleagues with similar commute routes so that I can share rides.  
- **Refined**: As a corporate employee, I want the system to suggest colleagues with similar routes and schedules so that I can easily join a carpool and reduce commuting costs.

- **Original**: As an employee, I want to coordinate schedules with my carpool group.  
- **Refined**: As a carpool participant, I want to coordinate schedules with my carpool group through the app so that we can maintain reliable commuting plans.

- **Original**: As an employee, I want to see my cost savings from carpooling.  
- **Refined**: As a corporate employee, I want to view estimated monthly cost savings from carpooling so that I understand the financial benefits of participating.

## APIs

- **Original**: POST /login  
- **Refined**: POST /auth/login { email, password }

- **Original**: GET /match  
- **Refined**: GET /carpools/match { user_id, home_location, work_location, schedule }

- **Original**: POST /join  
- **Refined**: POST /carpools/join { user_id, carpool_id }

- **Original**: GET /savings  
- **Refined**: GET /analytics/savings { user_id, period }