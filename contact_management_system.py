import json

# File to store the contacts persistently
FILE_NAME = "contacts.json"

# Function to load contacts from file
def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if the file does not exist
    except json.JSONDecodeError:
        print("Error: File is corrupted. Starting with an empty contact list.")
        return []

# Function to save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Function to display all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return

    print("\nContact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contacts.append({"name": name, "phone": phone, "email": email})
    print(f"Contact {name} added successfully!")

# Function to edit an existing contact
def edit_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter the contact number to edit: ")) - 1
        if 0 <= index < len(contacts):
            print("Leave a field blank to keep it unchanged.")
            name = input(f"Enter new name (current: {contacts[index]['name']}): ").strip()
            phone = input(f"Enter new phone (current: {contacts[index]['phone']}): ").strip()
            email = input(f"Enter new email (current: {contacts[index]['email']}): ").strip()

            if name:
                contacts[index]['name'] = name
            if phone:
                contacts[index]['phone'] = phone
            if email:
                contacts[index]['email'] = email

            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter the contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            print(f"Contact {deleted_contact['name']} deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main function to run the contact management system
def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
            save_contacts(contacts)
        elif choice == "4":
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == "5":
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
