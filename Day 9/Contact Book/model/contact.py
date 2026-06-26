class Contact:
    def __init__(self,contact_name,contact_number):
        self.contact_name = contact_name
        self.contact_number = contact_number

    def display(self):
        print(f"{self.contact_name:<20}{self.contact_number}")

    def to_dict(self):
        return {
            "Name" : self.contact_name,
            "Number" : self.contact_number
        }
    
    @classmethod
    def from_dict(cls,data):
        return cls(contact_name = data["Name"], contact_number = data["Number"])