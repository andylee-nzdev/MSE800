# Auckland Aquarium Management System

This project manages the number of fish currently available in an aquarium in Auckland.

Supported fish:

- Goldfish
- Shark
- Angelfish
- Tuna
- Salmon

The system accepts fish data from the user and displays each fish type, its category, and the current number available in the aquarium.

Inventory data is stored in a local SQLite database named `aquarium_inventory.db`.
The database is created automatically the first time the program runs.

## Design Patterns

### Factory Pattern

The `FishFactory` class creates fish objects based on the fish type entered by the user.

The main program does not directly create `Goldfish`, `Shark`, `Angelfish`, `Tuna`, or other objects. Instead, it asks the factory to create the correct fish object. 

Also, we can extend more fish categories easily in later development without changing too much current codebase.

### Singleton Pattern

The `AquariumInventory` class uses the Singleton pattern.

Only one shared aquarium inventory object is created during the program. This ensures all fish records are stored in the same Auckland aquarium inventory.

### SQLite Database

The `fish_inventory` table stores each fish name, category, and quantity.

If the same fish type is added more than once, the database updates the existing record by adding the new quantity to the saved quantity.

## Project Files

- `aquarium.py`: Contains the fish classes, factory class, and singleton inventory class.
- `database_manager.py`: Manages the SQLite database connection, table, and inventory queries.
- `main.py`: Runs the console application and accepts user input.
- `aquarium_inventory.db`: SQLite database created automatically when the app runs.
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
