from flight import DomesticFlight, Flight


def main():
    print("Air New Zealand Flight Inheritance Demonstration")
    print("=" * 52)

    # Flight is the parent class for general flight information.
    general_flight = Flight(
        flight_number="NZ900",
        origin="Auckland",
        destination="Sydney",
        departure_time="08:30",
        aircraft_type="Boeing 787-9",
    )

    print("\nGeneral Flight")
    print("-" * 52)
    print(general_flight.display_flight_info())

    # DomesticFlight is the subclass. It inherits shared attributes and methods
    # from Flight, then adds domestic-only details such as gate and baggage claim.
    domestic_flight = DomesticFlight(
        flight_number="NZ423",
        origin="Auckland",
        destination="Wellington",
        departure_time="10:15",
        aircraft_type="Airbus A320neo",
        gate_number="Gate 32",
        baggage_claim="Belt 4",
        regional_service=False,
    )

    # update_status() is inherited from Flight and works on the DomesticFlight object.
    domestic_flight.update_status("Boarding")

    print("\nDomestic Flight")
    print("-" * 52)
    print(domestic_flight.display_domestic_info())

    print("\nInherited Method Example")
    print("-" * 52)
    print(f"Domestic route using inherited get_route(): {domestic_flight.get_route()}")


if __name__ == "__main__":
    main()
