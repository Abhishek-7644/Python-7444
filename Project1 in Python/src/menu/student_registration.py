from src.menu.data import load_data, save_data
from src.menu.utils import (
    get_unique_id,
    get_valid_name,
    get_valid_address,
    get_valid_email
)


def student_registration():

    students = load_data()

    print("=== REGISTRATION ===")

    new_id = get_unique_id()
    name = get_valid_name()
    address = get_valid_address()
    email = get_valid_email()

    student = {
        "id": new_id,
        "name": name,
        "address": address,
        "email": email
    }

    students.append(student)
    save_data(students)

    print(" Registration successful")
