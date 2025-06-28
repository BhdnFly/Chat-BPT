## Project Title: Chat-BPT – Chat Bot of Polish Tourism
The goal is to design a Python-based console chatbot for Polish tourism using OOP principles.

## Technology Stack
 * Language: Python 3.x
 * Unit testing: unittest
 * Architecture: Object-Oriented Programming, using inheritance and polymorphism
 * Data store: Simulated with in-memory dictionaries (extendable internal or external DBs)
 * Testing: Manual testing via CLI

## Project scope
 * Greets users and asks for their city in Poland. Use only 3 cities per voivodeships for the initial implementation
 * Displays a list of commands (e.g. /help) or no command is given
 * Recommends tourism types (mountain, sea, cultural, spa, eco). Each turism class to have 3 diferent types
 * Asks follow-up questions based on user interest
 * Suggests one nearest tourist spot and the highest-rated destination for each tourism type
 * Provides distance and voivodeship to both. + highlited user comment
 * Allows users to change their city at any time, to restart the program(take advantage of geopy)

 ## OOP Implementation
 * Base class (TourismType) with common functionality for all tourism types
 * Derived classes (MountainTourism, SeaTourism, CulturalTourism) that inherit from base class
 * Polymorphic behavior through method overriding (get_description, recommend_attraction)
 * Factory pattern to create appropriate tourism type objects based on user input
 * Encapsulation of data and behavior within classes
 * Clean separation of concerns between chatbot logic and tourism domain

## Polymorphism Examples
 * Each tourism type provides its own implementation of recommend_attraction() method
 * The chatbot can use any tourism type object interchangeably through the common interface
 * Different tourism types respond differently to the same method calls
 * New tourism types can be added without changing the chatbot logic

## Data Structure
 * Define clear schemas for tourism types, locations, and ratings
 * Structure data to allow easy transition from dictionaries to databases
 * Include metadata for attractions (opening hours, contact info, etc.)

## Error Handling
 * Validate user input for city names and commands
 * Handle edge cases like unknown locations or unavailable data
 * Provide helpful error messages with suggestions

## Command Structure
 * /help - Display available commands
 * /city [name] - Change current city
 * /restart - Reset the conversation
 * /info [attraction] - Get detailed information about an attraction
 * /nearby [type] - Find attractions of specific type near current city

## Deployment
 * Package as a standalone Python application
 * Provide installation instructions for end users

## Future Enhancements
 * Multilingual support (Polish and Ukrainian)
 * Integration with external APIs for real-time data
 * Expand to cover all cities in Poland
 * Web or mobile interface options
 * Consider user experience and add more features to the chatbot
 * Consider containerization for easier deployment
