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
        current_year = 2023  # update this to the current year as needed
        return current_year - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage (50 or more years old)."""
        return self.get_age() >= 50

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Less than, used for sorting Guitars by year."""
        return self.year < other.year
