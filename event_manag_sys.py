class Event:

    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0


    def add_participant(self, number):
        """Increases the participant count by the amount the user puts in"""
        self.participant_count += number 


    def get_participant_count(self):
        """Returns the current number of participants"""
        return self.participant_count 