from abc import ABC, abstractmethod


class Fish(ABC):
    """Abstract product used by the FishFactory."""

    name = ""
    category = ""

    def __init__(self, quantity):
        self.quantity = quantity

    def display(self):
        return f"{self.name} | Category: {self.category} | Available: {self.quantity}"


class Goldfish(Fish):
    name = "Goldfish"
    category = "Freshwater fish"


class Shark(Fish):
    name = "Shark"
    category = "Marine predator fish"


class Angelfish(Fish):
    name = "Angelfish"
    category = "Tropical fish"


class Tuna(Fish):
    name = "Tuna"
    category = "Marine fish"


class Salmon(Fish):
    name = "Salmon"
    category = "Migratory fish"


class Factory(ABC):
    @abstractmethod
    def create_fish(self, fish_type, quantity):
        pass


class FishFactory(Factory):
    """Factory Pattern: creates fish objects without exposing class creation."""

    _fish_classes = {
        "goldfish": Goldfish,
        "shark": Shark,
        "angelfish": Angelfish,
        "tuna": Tuna,
        "salmon": Salmon,
    }

    def create_fish(self, fish_type, quantity):
        fish_class = self._fish_classes.get(fish_type.lower())

        if fish_class is None:
            supported_fish = ", ".join(self.available_fish())
            raise ValueError(f"Unsupported fish type. Choose from: {supported_fish}")

        return fish_class(quantity)

    def available_fish(self):
        return [fish_class.name for fish_class in self._fish_classes.values()]


class AquariumInventory:
    """Singleton Pattern: keeps one shared aquarium inventory for the app."""

    # Class variable to hold the single instance of AquariumInventory
    _instance = None

    # Override __new__ to control instance creation and ensure only one instance exists
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AquariumInventory, cls).__new__(cls)
            cls._instance._fish_records = {}
            cls._instance.location = "Auckland"
        return cls._instance

    # Add or update fish in the inventory
    def add_fish(self, fish):
        if fish.name in self._fish_records:
            self._fish_records[fish.name].quantity += fish.quantity
        else:
            self._fish_records[fish.name] = fish

    # Retrieve all fish records as a list
    def get_all_fish(self):
        return list(self._fish_records.values())

    # Check if there are any fish in the inventory
    def has_fish(self):
        return len(self._fish_records) > 0

    # Display the inventory in a user-friendly format
    def display_inventory(self):
        if not self.has_fish():
            return "No fish are currently available in the aquarium."

        lines = [f"Aquarium Inventory - {self.location}"]
        lines.append("-" * 40)

        for fish in self.get_all_fish():
            lines.append(fish.display())

        return "\n".join(lines)
