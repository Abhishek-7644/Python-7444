students = []

id1 = int(input("Enter Student 1 ID: "))
name1 = input("Enter Student 1 Name: ")

students.append({"id": id1, "name": name1})


id2 = int(input("Enter Student 2 ID: "))
name2 = input("Enter Student 2 Name: ")

students.append({"id": id2, "name": name2})


print("\nRegistered Students:")
for student in students:
    print("ID:", student["id"], "| Name:", student["name"])




