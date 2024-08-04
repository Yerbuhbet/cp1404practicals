from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Represent a luxury version of a Taxi with additional fare costs."""

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness  # Multiply base price by fanciness level
