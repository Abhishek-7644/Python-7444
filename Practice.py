# Dictionaries
students = {}
teachers = {}

# Colors
GREEN = "\033[92m"
BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\033[0m"


# ---------------- STUDENT SIGNUP ----------------
def student_signup():
    while True:
        roll = input("Enter student roll number: ")

        if not roll.isdigit():
            print("Error: Roll number must contain digits only!")
            continue

        if roll in students:
            print("Roll number already exists!")
            continue

        name = input("Enter student name: ")
        if not name.replace(" ", "").isalpha():
            print("Error: Name must contain alphabets only!")
            continue

        email = input("Enter student email: ")
        if '@' not in email or '.' not in email:
            print("Error: Invalid email!")
            continue

        contact = input("Enter contact number: ")
        if not contact.isdigit() or len(contact) != 10:
            print("Error: Contact must be 10 digits!")
            continue

        password = input("Enter password: ")
        if password == "":
            print("Password cannot be empty!")
            continue

        students[roll] = {
            "name": name,
            "email": email,
            "contact": contact,
            "password": password
        }

        print(f"{GREEN}Student registered successfully!{RESET}")

        if input("Add more students? (yes/no): ").lower() != "yes":
            break


# ---------------- STUDENT DASHBOARD ----------------
def student_dashboard(roll):
    while True:
        print(f"\n{BLUE}--- Student Dashboard ---{RESET}")
        print("1. View Profile")
        print("2. Change Password")
        print("3. Logout")

        ch = input("Enter choice: ")

        if ch == "1":
            s = students[roll]
            print(f"""
Name    : {s['name']}
Email   : {s['email']}
Contact : {s['contact']}
Roll No : {roll}
""")

        elif ch == "2":
            old = input("Enter old password: ")
            if old == students[roll]["password"]:
                new = input("Enter new password: ")
                students[roll]["password"] = new
                print(f"{GREEN}Password changed successfully!{RESET}")
            else:
                print(f"{RED}Wrong old password!{RESET}")

        elif ch == "3":
            print("Logged out!")
            break
        else:
            print("Invalid choice!")


# ---------------- STUDENT LOGIN ----------------
def student_login():
    roll = input("Enter roll number: ")
    password = input("Enter password: ")

    if roll in students and students[roll]["password"] == password:
        print(f"{GREEN}Welcome {students[roll]['name']}!{RESET}")
        student_dashboard(roll)
    else:
        print(f"{RED}Invalid login credentials!{RESET}")


# ---------------- TEACHER SIGNUP ----------------
def teacher_signup():
    tid = input("Enter teacher ID: ")
    password = input("Enter password: ")
    name = input("Enter name: ")

    teachers[tid] = {
        "name": name,
        "password": password
    }

    print(f"{GREEN}Teacher registered successfully!{RESET}")


# ---------------- TEACHER DASHBOARD ----------------
def teacher_dashboard():
    while True:
        print(f"\n{BLUE}--- Teacher Dashboard ---{RESET}")
        print("1. View All Students")
        print("2. Delete Student")
        print("3. Logout")

        ch = input("Enter choice: ")

        if ch == "1":
            if not students:
                print("No students found!")
            else:
                for r, s in students.items():
                    print(f"{r} -> {s['name']} | {s['email']}")

        elif ch == "2":
            roll = input("Enter roll number to delete: ")
            if roll in students:
                del students[roll]
                print(f"{GREEN}Student deleted successfully!{RESET}")
            else:
                print("Roll number not found!")

        elif ch == "3":
            print("Teacher logged out!")
            break
        else:
            print("Invalid choice!")


# ---------------- TEACHER LOGIN ----------------
def teacher_login():
    tid = input("Enter teacher ID: ")
    password = input("Enter password: ")

    if tid in teachers and teachers[tid]["password"] == password:
        print(f"{GREEN}Welcome {teachers[tid]['name']}!{RESET}")
        teacher_dashboard()
    else:
        print(f"{RED}Invalid teacher credentials!{RESET}")


# ---------------- MAIN MENU ----------------
while True:
    print(f"\n{BLUE}==== Student Management System ===={RESET}")
    print("1. Student Signup")
    print("2. Student Login")
    print("3. Teacher Signup")
    print("4. Teacher Login")
    print("5. Exit")

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
        print("Invalid choice!")