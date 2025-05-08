from datetime import date


#A class representing a new version
class Commit:
    def __init__(self, message):
        self.message = message
        self.date = date.today()
        self.id = hash(message) % 1000000

    def __str__(self):
        return str(self.id) + " " + str(self.date) + " " + self.message
