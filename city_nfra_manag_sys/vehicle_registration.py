class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner


    def upDate(self, owner, new_type):
        """Updates the vehicle's owner and type with new values."""
        self.owner = owner
        self.type = new_type

    def display_Register(self):
        """Displays the vehicle's registration details."""
        print(f"'Owner': {self.owner}, 'Type': {self.type}, Registration number: {self.registration_number}")