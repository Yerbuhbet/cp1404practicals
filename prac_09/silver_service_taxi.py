from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Represent a luxury version of a Taxi with additional fare costs."""
    flagfall = 4.50  # Class variable for the additional charge on each new fare

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness  # Multiply base price by fanciness level

    def get_fare(self):
        """Calculate and return the price for the taxi trip including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
