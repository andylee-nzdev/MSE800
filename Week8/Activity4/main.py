from flight_management import (
    DomesticFlight,
    FlightManagementSystem,
    InternationalFlight,
)


def main():
    print("Complete Flight Management System - Hybrid Inheritance")
    print("=" * 64)

    system = FlightManagementSystem("Air New Zealand")

    domestic_flight = DomesticFlight(
        flight_number="NZ423",
        origin="Auckland",
        destination="Wellington",
        departure_time="10:15",
        aircraft_type="Airbus A320neo",
        capacity=180,
        gate_number="Gate 32",
        baggage_claim="Belt 4",
        regional_service=False,
    )

    international_flight = InternationalFlight(
        flight_number="NZ103",
        origin="Auckland",
        destination="Sydney",
        departure_time="08:30",
        aircraft_type="Boeing 787-9",
        capacity=302,
        terminal="International Terminal",
        passport_control_required=True,
        visa_required=False,
        destination_country="Australia",
    )

    domestic_flight.add_passenger("Mia Taylor")
    domestic_flight.add_passenger("Noah Wilson")
    domestic_flight.update_status("Boarding")

    international_flight.add_passenger("Ava Brown")
    international_flight.add_passenger("Liam Smith")
    international_flight.delay_flight("09:10")

    system.add_flight(domestic_flight)
    system.add_flight(international_flight)

    print("\nDomestic Flight")
    print("-" * 64)
    print(domestic_flight.display_domestic_info())

    print("\nInternational Flight")
    print("-" * 64)
    print(international_flight.display_international_info())

    print("\nInherited and Shared Method Examples")
    print("-" * 64)
    print(f"Domestic route from Flight parent: {domestic_flight.get_route()}")
    print(
        "International passengers from PassengerService parent: "
        f"{international_flight.get_passenger_count()}"
    )
    print(
        "Domestic extra baggage fee from BaggageService parent: "
        f"${domestic_flight.calculate_extra_baggage_fee(28)}"
    )

    print("\nManagement System Report")
    print("-" * 64)
    print(system.display_system_report())


if __name__ == "__main__":
    main()
