from model.contact import Contact
from services.contact_services import ContactBook
from storage import json_storage 


contacts = ContactBook()
while True:
    print("----------------Menu-----------------\n")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Save Contacts")
    print("5. Load Contacts")
    print("6. Exit")
    print("\n----------------Menu-----------------")

    while True:
        try:
            choice = int(input("Choose an option : "))
            break
        except ValueError:
            print("Invalid Option")

    if choice == 6:
        break
    
    match choice:
        case 1:
            name = input("Enter the name of the contact : ")
            number = input("Enter the number of the input : ")
            contacts.add_contact(name,number)

        case 2:
            name = input("Enter the name of the contact you want to search : ")
            contacts.search_contact(name)

        case 3:
            name = input("Enter the name of the contact you want to delete : ")
            contacts.delete_contact(name)

        case 4:
            json_storage.save_to_json(contacts)

        case 5:
            contacts = json_storage.load_from_json()