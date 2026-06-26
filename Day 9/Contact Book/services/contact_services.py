from model.contact import Contact

class ContactBook:
    def __init__(self,data = None):
        if data is None:
            self.contacts = []
        else:
            self.contacts = data
    
    def add_contact(self,name,number):
        contact = Contact(name,number)
        self.contacts.append(contact)

    def delete_contact(self, contact_name):
        found = False
        for contact in self.contacts:
            if contact_name == contact.contact_name:
                self.contacts.remove(contact)
                found = True
        if found == False:
            print("Contact not Found")    

    def search_contact(self,contact_name):
        found = False
        for contact in self.contacts:
            if contact_name == contact.contact_name:
                print(f"{contact.contact_name:<20}{contact.contact_number}")
                found = True
                break
        if found == False:
            print("Contact not Found")
