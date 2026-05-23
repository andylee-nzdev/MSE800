# Auckland Aquarium Management System

This project manages the number of fish currently available in an aquarium in Auckland.

Supported fish:

- Goldfish
- Shark
- Angelfish
- Tuna
- Salmon

The system accepts fish data from the user and displays each fish type, its category, and the current number available in the aquarium.

## Design Patterns

### Factory Pattern

The `FishFactory` class creates fish objects based on the fish type entered by the user.

The main program does not directly create `Goldfish`, `Shark`, `Angelfish`, `Tuna`, or other objects. Instead, it asks the factory to create the correct fish object. 

Also, we can extend more fish categories easily in later development without changing too much current codebase.

### Singleton Pattern

The `AquariumInventory` class uses the Singleton pattern.

Only one shared aquarium inventory object is created during the program. This ensures all fish records are stored in the same Auckland aquarium inventory.

## Project Files

- `aquarium.py`: Contains the fish classes, factory class, and singleton inventory class.
- `main.py`: Runs the console application and accepts user input.
- `README.md`: Explains the project and design patterns.

## How to Run

From this folder, run:

```bash
python3 main.py
```

## Example Input

```text
Enter fish type: Goldfish
Enter number of fish available: 12
Enter fish type: Shark
Enter number of fish available: 2
Enter fish type: Salmon
Enter number of fish available: 7
Enter fish type: done
```

## Example Output

```text
Aquarium Inventory - Auckland
----------------------------------------
Goldfish | Category: Freshwater fish | Available: 12
Shark | Category: Marine predator fish | Available: 2
Salmon | Category: Migratory fish | Available: 7
```
