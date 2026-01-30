students = []

while True:
    print("\n-------STUDENT MENU-------")
    print("1. Registration System")
    print("2. Search Student Record")
    print("3. Exit")
    
    try:
        user_choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if user_choice == 1:
        # Registration
        try:
            student_id = int(input("Enter your ID: "))
        except ValueError:
            print("ID must be a number!")
            continue

        name = input("Enter your name: ")
        address = input("Enter your address: ")
        email = input("Enter your email: ")

        # Store student info as a dictionary
        student = {
            "id": student_id,
            "name": name,
            "address": address,
            "email": email
        }

        students.append(student)  # <-- append the dictionary, NOT the list
        print("Registration Successful!")

    elif user_choice == 2:
        # Search student record
        try:
            search_id = int(input("Enter student ID to search: "))
        except ValueError:
            print("ID must be a number!")
            continue

        found = False
        for student in students:
            if student["id"] == search_id:
                print("\nStudent Found:")
                print(f"ID: {student['id']}")
                print(f"Name: {student['name']}")
                print(f"Address: {student['address']}")
                print(f"Email: {student['email']}")
                found = True
                break

        if not found:
            print("Student record not found.")

    elif user_choice == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
