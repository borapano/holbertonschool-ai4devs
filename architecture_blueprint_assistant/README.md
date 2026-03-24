# ExpenseMate

## Application Concept
ExpenseMate is a web-based application designed to simplify shared expense management within groups. Users can register and log in to the platform, create new groups, or join existing ones using unique group codes. Within each group, members can add expenses by specifying the amount, description, payer, and participants. Expenses can be split equally or among selected participants, and users can edit or delete only the expenses they created. The system automatically calculates balances, showing who owes whom, and provides clear summaries of all debts, making group financial management transparent, accurate, and efficient. Optional enhancements like user avatars, phone numbers, group descriptions, and receipt images improve user experience and enable future functionality.

## Key Architecture Choices
ExpenseMate was explored through both **monolithic** and **microservices** architectures.  

- In the **monolithic approach**, all functionality — authentication, group management, expense management, balance calculation, and reporting — resides within a single backend application. This design simplifies deployment, data management, and initial development but can become harder to scale as the number of users and groups grows.  

- The **microservices architecture** decomposes the system into independent services: Authentication, Group Management, Expense Management, Balance Calculation, and Reporting. Each service has its own database, which allows for improved scalability, isolation of responsibilities, and easier future extensions (e.g., adding notifications or analytics). An API Gateway coordinates requests from the frontend, ensuring seamless communication between services.

The **data model** supports these architectures, with entities for Users, Groups, Expenses, Balances, and a junction table for group membership. Optional fields such as avatars, phone numbers, group descriptions, and receipt images enhance usability without overcomplicating the core structure.

## Insights from Comparison
The comparison of monolithic and microservices architectures highlighted trade-offs in simplicity versus flexibility. Monoliths are easier to develop and test initially, but scaling and introducing new features can become challenging. Microservices provide modularity and independent scalability but introduce complexity in terms of deployment, inter-service communication, and database management. For an MVP, a monolithic approach may be sufficient, while a microservices approach is better suited for long-term growth or enterprise-scale usage.

## Lessons on AI Contribution
AI proved valuable in **rapidly generating structured documentation, architecture diagrams, and data models**. It allowed for consistent formatting across multiple deliverables, accelerated decision-making by comparing architectures, and suggested optional features to enhance the user experience. Key lessons include the importance of carefully specifying constraints and optional fields, validating generated diagrams for logical consistency, and using AI as a complement to human review rather than a replacement for architectural reasoning. By iterating on prompts and verifying outputs, AI can significantly reduce development planning time and improve clarity in technical documentation.

## Conclusion
ExpenseMate demonstrates how thoughtful design, clear data modeling, and careful consideration of architecture choices can streamline shared expense management. Whether using a monolithic or microservices approach, the system prioritizes usability, transparency, and scalability. AI-assisted documentation and design insights accelerate planning, helping teams visualize the system and make informed architectural decisions. With future enhancements like notifications and receipt verification, ExpenseMate can evolve into a comprehensive platform for collaborative financial management.