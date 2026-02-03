def add_contact():
    name = input("Enter name :")
    phone = input("Enter phone number :")
    email = input("Enter email :")

    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone},{email}\n")
        print("Contact added successfully")

def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()

        if not contacts:
            print("No contacts")
        else:
            print("\n--- Contact List ---")

        
        for contact in contacts:
            name ,phone , email = contact.strip().split(",")
            print(f"Name: {name}, Phone: {phone}, Email: {email}")

    except FileNotFoundError:
        print("No Contacts file found")

def search_contact():
    search_name = input("Enter name to search: ")
    found = False

    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                if name .lower() == search_name.lower():
                    print(f"Found -> Name: {name}, Phone: {phone}, Email: {email}")
                    found = True
        if not found:
            print("Contact not found")

    except FileNotFoundError:
        print("No contacts file found.")

def delete_contact():
    delete_name = input("Enter name to delete:")
    found = False
    contacts = []

    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
        with open("contacts.txt", "w") as file:
            for line in contacts:
                name, phone, email = line.strip().split(",")
                if name.lower() != delete_name.lower():
                    file.write(line)
                else:
                    found = True
        if found:
            print("Contact deleted successfully!")
        else:
            print("Contact not found")

    except FileNotFoundError:
        print("No contacts file found")

while True:
    print("\n--- Contact Management System developed by Monty ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choic(1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Good Byee!")
        break
    else:
        print("Invalid Choice, Try Again.")
