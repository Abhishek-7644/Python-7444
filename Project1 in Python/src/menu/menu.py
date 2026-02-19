from src.menu.student_registration import student_registration
from src.menu.search_student import search_student
from src.menu.update_student import update_student
from src.menu.delete_student import delete_student
from src.menu.view_student import view_student


def menu():

    while True:

        print("""
===== MENU =====
1. Registration
2. Search
3. Update
4. Delete
5. View
6. Exit
""")

        choice = input("Enter choice: ")

        if choice == "1":
            student_registration()

        elif choice == "2":
            search_student()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            view_student()

        elif choice == "6":
            print("Exit")
            break

        else:
            print(" Invalid choice")
