from aquarium import AquariumInventory, FishFactory


def get_quantity():
    while True:
        try:
            quantity = int(input("Enter number of fish available: "))
            if quantity < 0:
                print("Quantity cannot be negative. Please try again.")
                continue
            return quantity
        except ValueError:
            print("Please enter a valid whole number.")


def main():
    fish_factory = FishFactory()
    aquarium = AquariumInventory()

    print("Auckland Aquarium Management System")
    print("Available fish:", ", ".join(fish_factory.available_fish()))
    print("Type 'done' when you have finished entering fish data.\n")

    while True:
        fish_type = input("Enter fish type: ").strip()

        if fish_type.lower() == "done":
            break

        try:
            quantity = get_quantity()
            fish = fish_factory.create_fish(fish_type, quantity)
            aquarium.add_fish(fish)
            print(f"{fish.name} added successfully.\n")
        except ValueError as error:
            print(error)
            print()

    print()
    print(aquarium.display_inventory())


if __name__ == "__main__":
    main()
