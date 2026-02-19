from src.menu.data import load_data


# 🔹 UNIQUE ID (for add student)
def get_unique_id():

    data = load_data()

    while True:
        user_id = input("Enter 6 digit ID: ").strip()

        if not (user_id.isdigit() and len(user_id) == 6):
            print("❌ ID must be exactly 6 digits")
            continue

        user_id = int(user_id)

        for s in data:
            if s["id"] == user_id:
                print("❌ ID already exists")
                break
        else:
            return user_id


# 🔹 NORMAL ID (for search, update, delete)
def get_valid_id():

    while True:
        user_id = input("Enter 6 digit ID: ").strip()

        if user_id.isdigit() and len(user_id) == 6:
            return int(user_id)
        else:
            print("❌ ID must be exactly 6 digits")


# 🔹 NAME
def get_valid_name():

    while True:
        name = input("Enter name: ").strip()

        if name.isalpha():
            return name
        else:
            print(" Name must contain only alphabets")



def get_valid_address():

    while True:
        address = input("Enter address: ").strip()

        if address.replace(" ", "").isalpha():
            return address
        else:
            print("❌ Address must contain only alphabets")



def get_valid_email():

    while True:
        email = input("Enter email: ").strip()

        if "@" in email and email.endswith(".com"):
            return email
        else:
            print(" Invalid email")
