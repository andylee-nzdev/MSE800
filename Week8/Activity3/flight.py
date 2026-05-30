class Flight:
    """Parent class representing a general Air New Zealand flight."""

    def __init__(self, flight_number, origin, destination, departure_time, aircraft_type):
        # These attributes are shared by all flight types.
        # DomesticFlight receives them automatically by calling super().__init__().
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.aircraft_type = aircraft_type
        self.status = "Scheduled"

    def get_route(self):
        # This shared method can be used by Flight and every subclass.
        return f"{self.origin} to {self.destination}"

    def update_status(self, new_status):
        # This shared method changes a parent attribute inherited by the subclass.
        self.status = new_status

    def display_flight_info(self):
        # This shared method displays the common flight information.
        return (
            f"Flight Number: {self.flight_number}\n"
            f"Route: {self.get_route()}\n"
            f"Departure Time: {self.departure_time}\n"
            f"Aircraft Type: {self.aircraft_type}\n"
            f"Status: {self.status}"
        )


class DomesticFlight(Flight):
    """Subclass representing an Air New Zealand domestic flight."""

    def __init__(
        self,
        flight_number,
        origin,
        destination,
        departure_time,
        aircraft_type,
        gate_number,
        baggage_claim,
        regional_service,
    ):
        # super() calls the parent constructor so the subclass inherits
        # flight_number, origin, destination, departure_time, aircraft_type, and status.
        super().__init__(
            flight_number,
            origin,
            destination,
            departure_time,
            aircraft_type,
        )

        # These attributes belong only to DomesticFlight.
        self.gate_number = gate_number
        self.baggage_claim = baggage_claim
        self.regional_service = regional_service

    def requires_passport(self):
        # Domestic flights within New Zealand do not require a passport.
        return False

    def display_domestic_info(self):
        # This method uses inherited parent methods and domestic-only attributes.
        passport_message = "No passport required"
        service_type = "Regional service" if self.regional_service else "Main domestic service"

        return (
            f"{self.display_flight_info()}\n"
            f"Gate Number: {self.gate_number}\n"
            f"Baggage Claim: {self.baggage_claim}\n"
            f"Service Type: {service_type}\n"
            f"Travel Document: {passport_message}"
        )
