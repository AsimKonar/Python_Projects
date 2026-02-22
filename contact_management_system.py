import json
import os

class ContactManagement:
    def __init__(self, file_path = "JSON_files/contact_book.json"):
        self.filename = file_path
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        self.numbers = self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r") as file:
                return json.load(file)

        except json.JSONDecodeError:
            print("File Corrupted, Resetting the file")
            return []

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.numbers, file, indent=4)

    def add_contact(self, name, number, email, address):
        try:
            if not number.isdigit() or len(number) != 10:
                return "Invalid phone number. Must be 10 digits."
            if "@" not in email or "." not in email:
                return "Invalid email format."
            for i in self.numbers:
                if i['number'] == number:
                    return "Number already exist in the Database."
            number = {
                'id': max([e['id'] for e in self.numbers], default=0)+1,
                'name':name,
                'number': number,
                'email': email,
                'address': address
            }
            self.numbers.append(number)
            self.save_data()
            return "Number added successfully."
        except ValueError:
            return "Something went wrong while adding the Number"

    def view_all(self):
        return self.numbers

    def get_sorted_contacts(self, sort_by="id", reverse=False):
        if sort_by not in ["id", "name", "number"]:
            return self.numbers
        return sorted(self.numbers, key=lambda x: x[sort_by], reverse=reverse)

    def search_by_name(self, name):
        return [i for i in self.numbers if name.lower() in i['name'].lower()]

    def search_by_number(self, number):
        return [i for i in self.numbers if i['number'] == number]

    def update_contact(self,name, number, email, address):
        try:
            if not number.isdigit() or len(number) != 10:
                return "Invalid phone number. Must be 10 digits."
            if "@" not in email or "." not in email:
                return "Invalid email format."
            found = False
            for num in self.numbers:
                if num['number'] == number and num['name'].lower() != name.lower():
                    return "Number already associated with another number"
            for num in self.numbers:
                if num['number'].lower() == number:
                    num['name'] = name
                    num['number'] = number
                    num['email'] = email
                    num['address'] = address
                    found = True
                    break
            if not found:
                return "Contact Does not Exist."
            self.save_data()
            return "Number updated successfully."
        except ValueError:
            return "Something went wrong while updating the number"

    def delete_contact(self, name, number):
        initial_length = len(self.numbers)
        self.numbers = [i for i in self.numbers if i['name'].lower() != name.lower() or i['number'] != number]
        if len(self.numbers) == initial_length:
            return "Contact Does not Exist."

        self.save_data()
        return "Contact Deleted Successfully."


def main():
    contact_management = ContactManagement()
    def pretty_print(numbers):
        for i in numbers:
            print('-'*30)
            print('id: '+str(i['id']))
            print('name: '+i['name'])
            print('number: '+str(i['number']))
            print('email: ' +i['email'])
            print('address: '+i['address'])
            print('-' * 30)
    while True:
        print("""
        Select One of the Below option:
        1. Add contact
        2. View all contacts
        3. Search by name
        4. Search by phone number
        5. Update contact
        6. Delete contact
        7. Exit
        """)
        try:
            action = int(input("Select one: ").strip())
        except ValueError:
            print("Invalid Input.")
            continue
        if action == 1: # Add contact
            name = input("Enter the Name: ").strip()
            number = input("Enter the Number: ").strip()
            email = input("Enter the Email: ").strip().lower()
            address = input("Enter the Address: ").strip()
            print(contact_management.add_contact(name, number, email, address))
        elif action == 2: # View all contacts
            pretty_print(contact_management.view_all())
        elif action == 3:
            sort_by = input("Sort by (id/name/number): ").strip().lower()
            order = input("Order (asc/desc): ").strip().lower()
            reverse = True if order == "desc" else False
            pretty_print(contact_management.get_sorted_contacts(sort_by, reverse))
        elif action == 3: # Search by name
            name = input("Enter the name: ").strip()
            pretty_print(contact_management.search_by_name(name))
        elif action == 4: # Search by phone number
            number = input("Enter the number: ").strip()
            pretty_print(contact_management.search_by_number(number))
        elif action == 5: # Update contact
            name = input("Enter the Name: ").strip()
            number = str(input("Enter the Number: ").strip())
            email = input("Enter the Email: ").strip().lower()
            address = input("Enter the Address: ").strip()
            print(contact_management.update_contact(name, number, email, address))
        elif action == 6: # Delete contact
            name = input("Enter the Name to be deleted: ").strip()
            number = input("Enter the Number to be deleted: ").strip()
            print(contact_management.delete_contact(name, number))
        elif action == 7: # Exit
            print("Thank You For Using Our Contact Management App")
            break
        else:
            print("Please Enter a Valid Input.")

main()