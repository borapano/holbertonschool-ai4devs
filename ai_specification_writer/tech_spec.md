# Technical Specification

## System Components
- **Authentication Service**  
  Handles user authentication through corporate Single Sign-On (SSO) and manages secure access to the platform.

- **Commute Matching Service**  
  Matches employees with similar routes, schedules, and preferences to form carpool groups.

- **Communication & Notification Service**  
  Enables in-app messaging, schedule coordination, and notifications for changes in carpool plans.

- **Analytics & Reporting Service**  
  Tracks CO₂ savings, cost reductions, and employee participation metrics for company reporting.

## Data Models
- **User**: id, name, email, role, home_location, work_location, schedule  
- **CarpoolGroup**: id, driver_id, passenger_ids, route, departure_time, available_seats  
- **Trip**: id, group_id, date, status, estimated_co2_savings, estimated_cost_savings  

## API Endpoints
- **POST /auth/login**  
  Parameters: email, password  

- **GET /carpools/match**  
  Parameters: user_id, home_location, work_location, schedule  

- **POST /carpools/create**  
  Parameters: driver_id, route, departure_time, available_seats  

- **POST /carpools/join**  
  Parameters: user_id, carpool_id  

- **GET /analytics/savings**  
  Parameters: user_id, period