class Flight:
    """Parent class for shared flight information and behaviour."""

    def __init__(
        self,
        flight_number,
        origin,
        destination,
        departure_time,
        aircraft_type,
        capacity,
    ):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.aircraft_type = aircraft_type
        self.capacity = capacity
        self.status = "Scheduled"

    def get_route(self):
        return f"{self.origin} to {self.destination}"

    def update_status(self, new_status):
        self.status = new_status

    def delay_flight(self, new_departure_time):
        self.departure_time = new_departure_time
        self.status = "Delayed"

    def display_flight_info(self):
        return (
            f"Flight Number: {self.flight_number}\n"
            f"Route: {self.get_route()}\n"
            f"Departure Time: {self.departure_time}\n"
            f"Aircraft Type: {self.aircraft_type}\n"
            f"Capacity: {self.capacity}\n"
            f"Status: {self.status}"
        )


class PassengerService:
    """Parent class for passenger handling shared by flight types."""

    def __init__(self):
        self.passengers = []

    def add_passenger(self, passenger_name):
        self.passengers.append(passenger_name)

    def remove_passenger(self, passenger_name):
        if passenger_name in self.passengers:
            self.passengers.remove(passenger_name)
            return True
        return False

    def get_passenger_count(self):
        return len(self.passengers)

    def display_passengers(self):
        if not self.passengers:
            return "Passengers: None"
        return f"Passengers: {', '.join(self.passengers)}"


class BaggageService:
    """Parent class for baggage handling shared by flight types."""

    def __init__(self, baggage_limit_kg):
        self.baggage_limit_kg = baggage_limit_kg
        self.extra_baggage_fee_per_kg = 25

    def set_baggage_limit(self, baggage_limit_kg):
        self.baggage_limit_kg = baggage_limit_kg

    def calculate_extra_baggage_fee(self, baggage_weight_kg):
        extra_weight = max(0, baggage_weight_kg - self.baggage_limit_kg)
        return extra_weight * self.extra_baggage_fee_per_kg

    def display_baggage_policy(self):
        return (
            f"Baggage Limit: {self.baggage_limit_kg} kg\n"
            f"Extra Baggage Fee: ${self.extra_baggage_fee_per_kg} per kg"
        )


class DomesticFlight(Flight, PassengerService, BaggageService):
    """Child class for domestic flights using hybrid inheritance."""

    def __init__(
        self,
        flight_number,
        origin,
        destination,
        departure_time,
        aircraft_type,
        capacity,
        gate_number,
        baggage_claim,
        regional_service,
    ):
        Flight.__init__(
            self,
            flight_number,
            origin,
            destination,
            departure_time,
            aircraft_type,
            capacity,
        )
        PassengerService.__init__(self)
        BaggageService.__init__(self, baggage_limit_kg=23)
        self.gate_number = gate_number
        self.baggage_claim = baggage_claim
        self.regional_service = regional_service

    def requires_passport(self):
        return False

    def get_service_type(self):
        if self.regional_service:
            return "Regional domestic service"
        return "Main domestic service"

    def assign_gate(self, gate_number):
        self.gate_number = gate_number

    def display_domestic_info(self):
        return (
            f"{self.display_flight_info()}\n"
            f"{self.display_baggage_policy()}\n"
            f"Passenger Count: {self.get_passenger_count()}\n"
            f"Gate Number: {self.gate_number}\n"
            f"Baggage Claim: {self.baggage_claim}\n"
            f"Service Type: {self.get_service_type()}\n"
            f"Passport Required: {self.requires_passport()}"
        )


class InternationalFlight(Flight, PassengerService, BaggageService):
    """Child class for international flights using hybrid inheritance."""

    def __init__(
        self,
        flight_number,
        origin,
        destination,
        departure_time,
        aircraft_type,
        capacity,
        terminal,
        passport_control_required,
        visa_required,
        destination_country,
    ):
        Flight.__init__(
            self,
            flight_number,
            origin,
            destination,
            departure_time,
            aircraft_type,
            capacity,
        )
        PassengerService.__init__(self)
        BaggageService.__init__(self, baggage_limit_kg=30)
        self.terminal = terminal
        self.passport_control_required = passport_control_required
        self.visa_required = visa_required
        self.destination_country = destination_country

    def requires_passport(self):
        return self.passport_control_required

    def requires_visa(self):
        return self.visa_required

    def assign_terminal(self, terminal):
        self.terminal = terminal

    def display_international_info(self):
        return (
            f"{self.display_flight_info()}\n"
            f"{self.display_baggage_policy()}\n"
            f"Passenger Count: {self.get_passenger_count()}\n"
            f"Terminal: {self.terminal}\n"
            f"Destination Country: {self.destination_country}\n"
            f"Passport Required: {self.requires_passport()}\n"
            f"Visa Required: {self.requires_visa()}"
        )


class FlightManagementSystem:
    """System class that manages domestic and international flights."""

    def __init__(self, airline_name):
        self.airline_name = airline_name
        self.flights = {}

    def add_flight(self, flight):
        self.flights[flight.flight_number] = flight

    def remove_flight(self, flight_number):
        return self.flights.pop(flight_number, None)

    def find_flight(self, flight_number):
        return self.flights.get(flight_number)

    def list_all_flights(self):
        return list(self.flights.values())

    def display_system_report(self):
        report_lines = [
            f"{self.airline_name} Flight Management System",
            f"Total Flights: {len(self.flights)}",
        ]

        for flight in self.list_all_flights():
            report_lines.append(
                f"- {flight.flight_number}: {flight.get_route()} ({flight.status})"
            )

        return "\n".join(report_lines)
