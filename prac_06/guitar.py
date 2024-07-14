"""CP1404/CP5632 Practical - Guitar class example.

Estimate: 45 minutes
Start time: [record your start time here]
"""

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Get the age of the guitar in years."""
        return 2022 - self.year  # or you can use datetime module to get the current year

