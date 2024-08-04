from car import Car

class UnreliableCar(Car):
    """Represent a car that may or may not drive based on its reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability
