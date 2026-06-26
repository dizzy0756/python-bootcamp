from model.contact import Contact
from services.contact_services import ContactBook
import json

def save_to_json(contacts):
    contacts_new = [contact.to_dict() for contact in contacts.contacts]

    with open("D:\\AI-Automation-Bootcamp\\Day 9\\Contact Book\\storage\\contacts.json", "w") as file:
        json.dump(contacts_new, file, indent=4)
    print("Saved to contacts.json")

def load_from_json():
    try:
        with open("D:\\AI-Automation-Bootcamp\\Day 9\\Contact Book\\storage\\contacts.json","r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    contacts_list = [Contact.from_dict(item) for item in data]
    contacts = ContactBook(contacts_list)
    return contacts


    