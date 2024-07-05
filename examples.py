examples = [
    {"input": "Explain the concept of recursion", 
     "output": """Recursion is a programming technique where a function calls itself directly or indirectly in order to solve a problem. The recursive function solves a small part of the problem and then calls itself to solve the smaller remaining problem. This continues until the function reaches a base case, which is a condition that stops the recursion.

To illustrate this concept, I will create a flowchart showing how recursion works with an example of calculating the factorial of a number. A flowchart is suitable here as it helps visualize the step-by-step process of recursion.

Example: Calculating Factorial
Factorial of n (n!) is the product of all positive integers up to n.
Recursive Definition:
Base Case: fact(1) = 1
Recursive Case: fact(n)=n*fact(n-1)

Flowchart:
```mermaid
graph TD
  A["Main Program"] --> B["fact(4)"]
  B --> C["fact(3)"]
  C --> D["fact(2)"]
  D --> E["fact(1)"]
  E -- base case: \n return 1 --> D
  D -- return 2 * 1 = 2 --> C
  C -- return 3 * 2 = 6 --> B
  B -- return 4 * 6 = 24 --> A
```

This diagram illustrates the recursive calculation of the factorial of 4. Here's a step-by-step explanation:
1. Main Program starts the calculation and calls fact(4).
2. fact(4) calls fact(3).
3. fact(3) calls fact(2).
4. fact(2) calls fact(1).
5. fact(1) hits the base case and returns 1.
6. The result of fact(1) is used by fact(2) to return 2.
7. The result of fact(2) is used by fact(3) to return 6.
8. The result of fact(3) is used by fact(4) to return 24."""},

{"input": "explain the binary search algorithm.", 
 "output": """
    Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.
    To visualize the algorithm's steps, a flowchart is most suitable.
    ```mermaid
        graph TD
            A["Start"] --> B["Initialize low = 0, high = n-1"]
            B --> C["Calculate mid = (low + high) / 2"]
            C --> D["Compare target with arr[mid]"]
            D --> E["Target found at mid"]
            D --> F["Target < arr[mid]"]
            D --> G["Target > arr[mid]"]
            F --> H["Update high = mid - 1"]
            G --> I["Update low = mid + 1"]
            H --> C
            I --> C
            E --> J["End"]
            C --> K["low > high"]
            K --> L["Target not found"]
            L --> J
        ```

    Here's a step-by-step explanation of the binary search algorithm:

    1. Initialize `low` to 0 and `high` to `n-1`, where `n` is the length of the array.
    2. Calculate the middle index `mid` using the formula `(low + high) / 2`.
    3. Compare the target value with the value at `arr[mid]`.
    4. If the target value is found at `arr[mid]`, return the index `mid`.
    5. If the target value is less than `arr[mid]`, update `high` to `mid - 1`.
    6. If the target value is greater than `arr[mid]`, update `low` to `mid + 1`.
    7. Repeat steps 2-6 until `low` is greater than `high`.
    8. If `low` is greater than `high`, the target value is not found in the array.

    The binary search algorithm has a time complexity of O(log n), making it very efficient for large lists.
    """},

{"input": "What are the main principles of Object-Oriented Programming (OOP)?", "output": """
    Object-Oriented Programming (OOP) is a programming paradigm based on the concept of objects. These objects contain data and methods that manipulate that data. To explain the main principles of OOP, I will create a mind map, which is suitable for organizing concepts hierarchically.
 
    Mind Map:
    ```mermaid
       mindmap
        root(("Object-Oriented Programming (OOP)"))
            Encapsulation
            Data Hiding
            Access Modifiers
                Private
                Public
                Protected
            Abstraction
            Simplification
            Essential Features
            Interface
            Inheritance
            Reusability
            Base Class
            Derived Class
            Overriding
            Polymorphism
            Method Overloading
            Method Overriding
            Runtime Polymorphism
            Compile-time Polymorphism
            Classes and Objects
            Class Definition
            Object Instantiation
            Attributes
            Methods
            Additional Principles
            Composition
            Aggregation
            Association

    ```
    This mind map provides a structured overview of the main principles and components of Object-Oriented Programming (OOP).
    1. Encapsulation
        - Data Hiding: Encapsulation involves hiding the internal state of objects and restricting access to it.
        - Access Modifiers: Controls access levels to the attributes and methods of a class.
            -- Private: Accessible only within the class.
            -- Public: Accessible from any other code.
            -- Protected: Accessible within the class and its subclasses.
    2. Abstraction
        - Simplification: Focuses on the essential qualities of an object rather than the specific characteristics.
        - Essential Features: Provides only the necessary details and hides the complexity.
        - Interface: Defines a contract for what a class can do without specifying how it does it.
    3. Inheritance
        - Reusability: Allows a new class to inherit properties and behaviors from an existing class.
        - Base Class: The class whose properties are inherited.
        - Derived Class: The class that inherits properties from the base class.
        - Overriding: Allows a subclass to provide a specific implementation of a method already defined in its superclass.
    4. Polymorphism
        - Method Overloading: Allows multiple methods with the same name but different parameters within the same class.
        - Method Overriding: Allows a subclass to provide a specific implementation of a method defined in its superclass.
        - Runtime Polymorphism: Method overriding achieved during runtime.
        - Compile-time Polymorphism: Method overloading achieved during compile-time.
    5. Classes and Objects
        - Class Definition: A blueprint for creating objects (a particular data structure).
        - Object Instantiation: The creation of a real instance (object) from a class.
        - Attributes: Characteristics or properties of a class.
        - Methods: Functions or behaviors defined within a class.
    6. Additional Principles
        - Composition: A way to combine simple objects or data types into more complex ones.
        - Aggregation: A specialized form of composition where the child can exist independently of the parent.
        - Association: A relationship between two objects. 
"""},

{"input": "what're middlewares in terms of backend development?" , 
 "output": """In backend development, a middleware is a software component that mediates between two or more applications, services, or systems. It acts as an intermediary layer that enables communication, data exchange, and functionality between these entities.

To illustrate the concept of middleware, a sequence diagram is most suitable. It shows the flow of requests and responses between components.

Sequence Diagram:
```mermaid
sequenceDiagram
    participant Client as "Client App"
    participant Middleware as "Middleware"
    participant Server as "Backend Server"

    Client->>Middleware: Request
    Middleware->>Middleware: Process request
    Middleware->>Server: Forward request
    Server->>Middleware: Response
    Middleware->>Middleware: Process response
    Middleware->>Client: Forward response
```
In this sequence diagram, the middleware acts as an intermediary between the client application and the backend server. It receives requests from the client, processes them, and then forwards them to the server. The server responds to the middleware, which then processes the response and forwards it to the client.

Middlewares can perform various tasks, such as:

1. Authentication and authorization
2. Request and response logging
3. Error handling and debugging
4. Data encryption and decryption
5. Rate limiting and throttling
6. Caching and content delivery
7. API gateway and routing
8. Message queuing and workflow management"""},
    {"input": "Create a class diagram for a simple e-commerce system with classes for User, Product, Order, and Payment", "output": """
        To model the relationships and structure of a simple e-commerce system, a class diagram is most appropriate. It allows us to visualize the classes, their attributes, methods, and relationships.
        Class Diagram:
        ```mermaid
            classDiagram
            class User {
                +int userId
                +String name
                +String email
                +String password
                +login()
                +logout()
            }
            class Product {
                +int productId
                +String name
                +String description
                +float price
                +int stock
                +addProduct()
                +removeProduct()
            }
            class Order {
                +int orderId
                +Date orderDate
                +addProduct(Product product)
                +removeProduct(Product product)
                +calculateTotal()
            }
            class Payment {
                +int paymentId
                +float amount
                +Date paymentDate
                +processPayment()
            }

            User "1" --> "0..*" Order : places
            Order "1" --> "1" Payment : has
            Order "1" --> "0..*" Product : contains
            Product "0..*" --> "1" Order : ordered in
        ```
        This class diagram depicts a simplified model for an e-commerce system. Let's break down each component:

        1. User Class:
            - Attributes: userId, name, email, password
            - Methods: login(), logout()
            - Relationship: A User can place 0 to * Orders (1 to * relationship).
        2. Product Class:
            - Attributes: productId, name, description, price, stock
            - Methods: addProduct(), removeProduct()
            - Relationship: A Product can be contained in 0 to * Orders (0..* to 1 relationship).
        
        3. Order Class:

            - Attributes: orderId, orderDate
            - Methods: addProduct(Product product), removeProduct(Product product), calculateTotal()
            - Relationship: An Order has exactly 1 Payment (1 to 1 relationship) and can contain 0 to * Products (1 to 0..* relationship).
        
        4. Payment Class:
            - Attributes: paymentId, amount, paymentDate
            - Methods: processPayment()
            - Relationship: A Payment is associated with exactly 1 Order (1 to 1 relationship).
    """},

    {"input": "Explain the behavior of a traffic light system.", 
     "output": """
        To model the behavior and state transitions of a traffic light system, a state diagram is most suitable. It helps visualize the different states and the transitions between them.

        State Diagram:
        ```mermaid
            stateDiagram-v2
            [*] --> Red
            Red --> Green : Timer expires
            Green --> Yellow : Timer expires
            Yellow --> Red : Timer expires
        ```
    """},
    {"input": "Plan a software development project.", 
     "output":"""
        To plan a software development project, a Gantt chart is most appropriate. It provides a visual timeline of tasks, their durations, and dependencies, helping in project management.
        Gant Chart:
        ```mermaid
            gantt
            title Software Development Project Plan
            dateFormat  YYYY-MM-DD
            section Planning
            Requirement Analysis      :a1, 2024-07-01, 10d
            Feasibility Study         :a2, after a1, 7d
            Project Planning          :a3, after a2, 5d
            section Design
            System Design             :b1, 2024-07-20, 15d
            Architecture Design       :b2, after b1, 10d
            Database Design           :b3, after b1, 10d
            section Development
            Frontend Development      :c1, 2024-08-10, 20d
            Backend Development       :c2, after c1, 25d
            API Development           :c3, after c1, 15d
            section Testing
            Unit Testing              :d1, 2024-09-10, 10d
            Integration Testing       :d2, after d1, 10d
            System Testing            :d3, after d2, 10d
            section Deployment
            Deployment Preparation    :e1, 2024-09-30, 5d
            Final Deployment          :e2, after e1, 2d
        ```
        This Gantt chart outlines a software development project plan, with tasks divided into five sections: Planning, Design, Development, Testing, and Deployment. Each section contains tasks with specified start dates and durations. Dependencies between tasks are also indicated, meaning that some tasks can only start after others are completed. Here's a breakdown:

        1. Planning
            - Requirement Analysis: Starts on 2024-07-01 and lasts for 10 days.
            - Feasibility Study: Starts after Requirement Analysis and lasts for 7 days.
            - Project Planning: Starts after Feasibility Study and lasts for 5 days.
        
        2. Design
            - System Design: Starts on 2024-07-20 and lasts for 15 days.
            - Architecture Design: Starts after System Design and lasts for 10 days.
            - Database Design: Starts after System Design and lasts for 10 days.
        
        3. Development
            - Frontend Development: Starts on 2024-08-10 and lasts for 20 days.
            - Backend Development: Starts after Frontend Development and lasts for 25 days.
            - API Development: Starts after Frontend Development and lasts for 15 days.
        
        4. Testing
            - Unit Testing: Starts on 2024-09-10 and lasts for 10 days.
            - Integration Testing: Starts after Unit Testing and lasts for 10 days.
            - System Testing: Starts after Integration Testing and lasts for 10 days.
        
        5. Deployment
            - Deployment Preparation: Starts on 2024-09-30 and lasts for 5 days.
            - Final Deployment: Starts after Deployment Preparation and lasts for 2 days.
    """},

    {"input": "Model a library system", 
     "output": """
        To model a library system, an Entity-Relationship (ER) diagram is most appropriate. It helps visualize the entities, their attributes, and relationships.

        ```mermaid
            erDiagram
            BOOK {
                int BookID PK
                string Title
                string Author
                string ISBN
                string Publisher
                int YearPublished
                string Genre
                int CopiesAvailable
            }
            
            MEMBER {
                int MemberID PK
                string FirstName
                string LastName
                string Address
                string PhoneNumber
                string Email
                date MembershipDate
            }
            
            LOAN {
                int LoanID PK
                int BookID FK
                int MemberID FK
                date LoanDate
                date DueDate
                date ReturnDate
            }
            
            BOOK ||--o{ LOAN : has
            MEMBER ||--o{ LOAN : borrows
        ```
        Entities and Attributes:
            1. Book
                - BookID (Primary Key)
                - Title
                - Author
                - ISBN
                - Publisher
                - YearPublished
                - Genre
                - CopiesAvailable
            
            2. Member
                - MemberID (Primary Key)
                - FirstName
                - LastName
                - Address
                - PhoneNumber
                - Email
                - MembershipDate
            
            3. Loan
                - LoanID (Primary Key)
                - BookID (Foreign Key)
                - MemberID (Foreign Key)
                - LoanDate
                - DueDate
                - ReturnDate

        Relationships:
            1. Book - Loan
                - One Book can be associated with many Loans.
                - One Loan is associated with one Book.
                - Relationship: "Book" 1..* - 0..1 "Loan"
            
            2. Member - Loan
                - One Member can have many Loans.
                - One Loan is associated with one Member.
                - Relationship: "Member" 1..* - 0..1 "Loan"
    """}
]