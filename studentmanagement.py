# Dictionaries to store signup info
students = {}
teachers = {}

# Colors
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Student signup
def student_signup():
    while True:
        roll = input("Enter student roll number: ")

        # Roll number validation
        if not roll.isdigit():
            print("Error: Roll number must contain digits only!")
            continue

        if roll in students:
            print("Roll number already exists! Try again.")
            continue

        name = input("Enter student name: ")
        # Name validation: alphabets only
        if not name.replace(" ", "").isalpha():
            print("Error: Name must contain alphabets only!")
            continue

        # Email validation
        email = input("Enter student email: ")
        if '@' not in email or '.' not in email:
            print("Error: Invalid email! Must contain '@' and '.'")
            continue

        contact = input("Enter student contact number: ")
        # Contact validation: digits only and exactly 10 digits
        if not contact.isdigit() or len(contact) != 10:
            print("Error: Contact number must be exactly 10 digits!")
            continue

        # Password validation
        password = input("Enter password: ")
        if password == "":
            print("Error: Password cannot be empty!")
            continue

        # Store all info in a dictionary
        students[roll] = {
            "name": name,
            "email": email,
            "contact": contact,
            "password": password
        }

        print(f"{GREEN}Student {name} signed up successfully!{RESET}")

        more = input("Do you want to add another student? (yes/no): ").lower()
        if more != "yes":
            break

# Student login
def student_login():
    if not students:
        print("Signup first! No student registered.")
        return

    roll = input("Enter student roll number: ")
    password = input("Enter password: ")

    if roll in students:
        if students[roll]["password"] == password:
            print(f"{GREEN}Welcome, {students[roll]['name']}!{RESET}")
        else:
            print("Incorrect password!")
    else:
        print("Roll number not found. Signup first!")

# Teacher signup
def teacher_signup():
    tid = input("Enter teacher ID: ")
    name = input("Enter teacher name: ")
    teachers[tid] = name
    print(f"{GREEN}Teacher signed up successfully!{RESET}")

# Teacher login
def teacher_login():
    if not teachers:
        print("Signup first! No teacher registered.")
        return

    tid = input("Enter teacher ID: ")
    if tid in teachers:
        print(f"{GREEN}Welcome, {teachers[tid]}!{RESET}")
    else:
        print("Teacher ID not found. Signup first!")

# Main menu loop
while True:
    print(f"\n{BLUE}==== Student Management System ===={RESET}")
    print(f"{BLUE}1. Student Signup{RESET}")
    print(f"{BLUE}2. Student Login{RESET}")
    print(f"{BLUE}3. Teacher Signup{RESET}")
    print(f"{BLUE}4. Teacher Login{RESET}")
    print(f"{BLUE}5. Exit{RESET}")

    choice = input("Enter choice: ")

    if choice == "1":
        student_signup()
    elif choice == "2":
        student_login()
    elif choice == "3":
        teacher_signup()
    elif choice == "4":
        teacher_login()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice")