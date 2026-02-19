from src.menu.data import load_data, save_data
from src.menu.utils import (
    get_valid_name,
    get_valid_address,
    get_valid_email
)


def update_student():

    data = load_data()

    search_id = int(input("Enter ID to update: "))

    for s in data:
        if s["id"] == search_id:

            print("""
1. Name
2. Address
3. Email
            """)

            choice = input("What do you want to update: ")

            if choice == "1":
                s["name"] = get_valid_name()

            elif choice == "2":
                s["address"] = get_valid_address()

            elif choice == "3":
                s["email"] = get_valid_email()

            else:
                print("Invalid choice")
                return

            save_data(data)
            print("Updated successfully")
            return

    print(" Student not found")
