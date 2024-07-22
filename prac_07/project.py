from datetime import datetime

class Project:
    def __init__(self, name, completion, priority, start_date):
        self.name = name
        self.completion = completion
        self.priority = priority
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()

    def __str__(self):
        return f"{self.name} - {self.completion}% completed, Priority: {self.priority}, Start Date: {self.start_date.strftime('%d/%m/%Y')}"

    def __lt__(self, other):
        return self.priority < other.priority
