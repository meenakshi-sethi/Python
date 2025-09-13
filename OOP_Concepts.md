Object-oriented programming paradigm enables us to think in a natural way, it mimics the working of real-life entities or objects.
Its a foundational paradigm that helps structure code by grouping related data and behavior into classes and objects.

OOP approach bundles data (attributes) and behaviors (methods) within a single unit, enabling modular, maintainable and scalable code. Every entity in OOP is modeled as an object, having attributes (data) and behaviors (actions performed)

Advantages of OOP - Provides a clear structure to programs
	•	Makes code easier to maintain, reuse and debug
	•	Helps keep your code DRY (Don't Repeat Yourself)
The DRY principle means you should avoid writing the same code more than once. Move repeated code into functions or classes and reuse it.
	•	Allows you to build reusable applications with less code
core concepts of OOP
	1	Classes and Objects:
	1	A class acts as a blueprint or a template for creating objects. It defines the attributes (data) and methods (functions) that an object of that class will possess. Classes are user-defined templates that group related data (attributes) and functions (methods) together.
Classes are entities

	2	An object is an instance of a class, meaning it is a concrete realization of the blueprint defined by the class. Objects store data in attributes and provide behavior through methods. Multiple objects can be created from a single class, each with their own attribute values.
Everything is an Object
	Link of details

	2	Encapsulation: (principle) involves bundling data (attributes) and the methods that operate on that data within a single unit (the class). Use public, protected, private variables. It helps in controlling access to the data, promoting data protection and organization.

	3	Inheritance: Inheritance allows a new class (subclass or child class) to derive attributes and methods from an existing class (parent class or superclass). This promotes code reusability and establishes a hierarchical relationship between classes.

	4	Polymorphism: Polymorphism means "many forms." In OOP, it refers to the ability of objects of different classes to respond to the same method call in a way that is specific to their own class. This enables flexible and extensible code.

	5	Abstraction: Abstraction focuses on showing only the essential features of an object and hiding the complex implementation details. It allows you to create simplified interfaces for complex systems. Python inherently doesn’t support abstraction so we need to import module abs 

Key elements in Python OOP:
	1	`class` keyword: Used to define a class.
	2	`__init__` method: A special method known as the constructor, used to initialize an object's attributes when it is created.
	3	`self` parameter: A reference to the current instance of the class, used to access attributes and methods within the class.
	4	Attributes: Variables associated with a class or object, representing its characteristics. Aka Data/State. Attributes variables that store information about the object's state, such as a person's name or age.
	5	Methods: Functions defined within a class that operate on the object's data. AKA behaviour/functions. Methods are functions inside the class that define what actions the object can perform, like greeting or updating data. 
All objects created from a class contain the attributes and methods defined by that class, encapsulating both state and behavior in a single unit.











Need to check: [https://python-course.eu/](https://python-course.eu/)
# Payment System: Business Case & OOP Implementation

This demonstrates how ALL OOP concepts work together in a real-world payment processing system:
- Classes and Objects: Foundation structure for payment entities
- Encapsulation: Data protection and controlled access for financial security
- Inheritance: Code reuse and specialization for different payment types
- Polymorphism: Same interface, different behaviors for flexible payment processing
- Abstraction: Simple interfaces hiding complex payment workflows
- Composition: Objects containing other objects for complex relationships
- Aggregation: Objects using other objects without owning them

## 🏢 Business Problem & Use Case

### Background: Fintech Startup Challenge

**Your Role**: Sr Developer + Architect + QA
 - **Company Context:**
   - **PayEasy**: 25 person fintech startup
   - **Your tile**: Senior Software Engineer (but you are the entire tech team)
   - **Reporting to**: CEO directly
   - **Supporting**: 5 Customer support staff, 2 product managers, finance team
   - **Current System**: Built by previous developer who left 6 months ago (Link to legacy code:)

**Scenario**: You are the lead developer at "PayEasy", a growing fintech startup. The CEO comes to you with an urgent problem: 
*"We started with just credit card processing, but now customers want debit cards, digital wallets, crypto payments and international forex cards. Our current system is a mess - every time we add a new payment method, we have to rewrite half the codebase. We are losing customers to competitors who can integrate new payment methods in days, not months. We need a scalable, maintainable solution that can grow with use."*

### Business Requirements
1. **Multiple Payment Methods**: Support credit cards, debit cards, digital wallets, forex cards and cryptocurriences
2. **Easy Extensibility**: Add new payment types without breaking existing code













# COMPLETE LIBRARY MANAGEMENT SYSTEM - LINE BY LINE CODE EXPLANATION
[Link to code file](oop.py)

This file explains EVERY important line of code from the complete integraded system:
- WHAT each line does
- WHY i wrote it that way
- HOW it demonstrates OOP concepts
- WHEN you would use similar patterns

This is my complete guide to understanding every single design decision in the OOP system

01. IMPORT STATEMENTS - Building Our  toolkit
 

