class Magazine:
    def __init__(self, title, issue, year):
        self.title = title
        self.issue = issue
        self.year = year

    def __str__(self):
        return f"Журнал: {self.title} №: {self.issue} ({self.year})"
