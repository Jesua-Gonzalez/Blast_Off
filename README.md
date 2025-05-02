# Blast_Off
~ Developing a python program using OOP principles, class structures and unit tests.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

I have built a space exploration simulation system in Python using object-oriented programming (OOP) principles. The application models key components of space missions, including astronauts, spacecraft (both crewed and autonomous), and missions themselves. I designed and implemented multiple classes with realistic constraints, interactions, and behavior, and I thoroughly tested the system using Python’s unittest module.

ASTRONAUT CLASS
- Represents crew members who participate in missions.
- Stores the astronaut’s name, role, and mission experience.
- Dynamically accepts and stores additional attributes.
- Includes methods for gaining experience and retrieving info.

SPACECRAFT CLASS 
- Models crewed spacecraft.
- Manages a list of astronaut objects onboard.
- Handles constraints like maximum capacity.
- Includes methods to add astronauts, list crew, and provide spacecraft details.

MISSION CLASS
- Simulates a space expedition.
- Tracks the mission name, destination, assigned spacecraft, and current status.
- Manages lifecycle transitions (e.g., launch → ongoing, complete → completed).
- Reflects realistic mission conditions, like requiring crew before launch.

AUTONOMOUSSPACECRAFT CLASS
- A special type of spacecraft that operates without astronauts.
- Overrides the astronaut-adding mechanism to reject crew additions.
- Adds a new attribute autonomy_level (1–10 scale).
- Still provides all standard spacecraft details, adapted for autonomy.

TESTING (UNITTEST) 
- I wrote unit tests for key components using Python’s unittest framework to ensure:
- Astronaut experience increments correctly.
- Spacecraft doesn't exceed its defined capacity.
- Autonomous spacecraft doesn't allow astronauts to be added.
- These tests helped verify class behavior, enforce business logic, and ensure reliability.