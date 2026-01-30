#1 username and password login anr checking

username = input("enter username: ")

if username.isalnum():
    print("username valid:")
else:
    print("only alphabet and number is valid in username")
    
password = input("enter password: ")

if password == "":
    print("empty password cannot be valid")
else:
    print("password is valid")



 #2 checking number can divisible by 5 and 11 or not

num = int(input("enter number: "))
if num % 5 == 0 and num % 11 == 0:
    print("this number is divisible by 5 and 11")
else:
    print("this number is not divisible by 5 and 11")


#3 checking even and odd number tacking number from user

num = int(input("enter number: "))
if num % 2 == 0:
    print("this is even number")
else:
    print("this is odd number")



 #4 checking grade according to marks

marks = int(input("enter your marks: "))
if marks >= 90:
    print("your grade is a+")
elif marks >= 80:
    print("your grade is a")
elif marks >= 70:
    print("your grade is b")
elif marks >= 60:
    print("your grade is c")
elif marks >= 50:
    print("your grade is d")
elif marks >= 40:
    print("your grade is e")
else:
    print("you are fail")



#5 Leap year checking
year = int(input("enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("this year is a leap year")
else:
    print("this year is not a leap year")



#6 checking positive and negative number 
num = int(input("enter number: "))
if num > 0:
    print("this is positive number ")
else:
    print("this is negative number ")



#7 taking 3 random number from user and which is the largest number find in these
a = int(input("enter number: "))
b = int(input("enter number: "))
c =int(input("enter number: "))

if a > b and a > c:
    print("a is largest")
elif b > a and b > c:
    print("b is largest")
else:
    print("c is largest")


#8 age checking 
age = int(input("enter your age: "))
if age >= 18:
    print("you can vote ")
else:
    print("you cannot vote ")



#9 checking Vowels 
alphabet = input("Enter character: ")
if alphabet == 'a' or alphabet == 'e' or alphabet == 'i' or alphabet == 'o' or alphabet == 'u':
    print("This character is vowel")
else:
    print("this character is consonant ")


#10 checking email is valid or not

email = input("enter email: ")

if "@" in email and  "." in email:

    print("email is valid")
    
else:
    print("email is valid")


#length check 

    name = input("enter your name: ")
print(len(name))




# check the user full name check valid or invalid 


# type1

correct_name = "Abhishek kumar yadav"
name = input("enter your name: ")
if name == correct_name:
    print("contratulations")
else:
    print("invalid")




# type 02


name = input("enter your name: ")
confirm_name = input("enter your name:")

if name == confirm_name:
    print("conratulations")
else:
    print("invalid name")



# user se 3 student ka data lena  hai ek hi veriable ke andar list me dictationary banake aur uske id se search karne par uska detail apne aap aa jaye


students = []

student1 = {
    "id": input("enter student1 id: "),
    "name": input("enter student1 name: "),
    "qualification": {
        "degree": input("enter student1 qualification: "),
        "year": input("enter passing year: ")
    },
    "email": input("enter student1 email: ")
}

students.append(student1)

student2 = {
    "id": input("enter student2 id: "),
    "name": input("enter student2 name: "),
    "qualification": {
        "degree": input("enter student2 qualification: "),
        "year": input("enter passing year: ")
    },
    "email": input("enter student2 email: ")
}

students.append(student2)

student3 = {
    "id": input("enter student3 id: "),
    "name": input("enter student3 name: "),
    "qualification": {
        "degree": input("enter student3 qualification: "),
        "year": input("enter passing year: ")
    },
    "email": input("enter student3 email: ")
}

students.append(student3)

print(students)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@ LOOOOP USES @@@@@@@@@@@@@@@@@@@@@@@

# user se 3 student ka data lena  hai ek hi veriable ke andar list me dictationary banake aur uske id se search karne par uska detail apne aap aa jaye




students = []

# ---------- Student 1 ----------
student1 = {
    "id": input("Enter student1 id: "),
    "name": input("Enter student1 name: "),
    "qualification": {
        "degree": input("Enter student1 qualification: "),
        "year": input("Enter passing year: ")
    },
    "email": input("Enter student1 email: ")
}
students.append(student1)

# ---------- Student 2 ----------
student2 = {
    "id": input("Enter student2 id: "),
    "name": input("Enter student2 name: "),
    "qualification": {
        "degree": input("Enter student2 qualification: "),
        "year": input("Enter passing year: ")
    },
    "email": input("Enter student2 email: ")
}
students.append(student2)

# ---------- Student 3 ----------
student3 = {
    "id": input("Enter student3 id: "),
    "name": input("Enter student3 name: "),
    "qualification": {
        "degree": input("Enter student3 qualification: "),
        "year": input("Enter passing year: ")
    },
    "email": input("Enter student3 email: ")
}
students.append(student3)

# ---------- Search Student By ID ----------
search_id = input("\nEnter student id to search: ")

found = False

for student in students:
    if student["id"] == search_id:
        print("\n Student Found")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Degree:", student["qualification"]["degree"])
        print("Passing Year:", student["qualification"]["year"])
        print("Email:", student["email"])
        found = True
        break

if not found:
    print("\nStudent ID not found")



# mujhe ka use krke list ke andar dictationar data dalna hai uske bad usme user se name lena hai aue data ko match karana hai


    dictdata = [
    {"id":101,"name":"Abhishek","address":"gopalganj"},
    {"id":102,"name":"indixpert","address":"Hyderabad"},
    {"id":103,"name":"Aryan","address":"bihar"}
]

name = input("enter name: ")

found = False

for data in dictdata:
    if data["name"].lower() == name.lower():
        print("Record found successfully")
        print("id:", data["id"])
        print("name:", data["name"])
        print("address:", data["address"])
        found = True
        break

if not found:
    print("Record not found")


# loop ka use karke dict in list me se key and value likanlna hai 


dictdata = [
    {"id":101,"name":"Abhishek","address":"gopalganj"},
    {"id":102,"name":"indixpert","address":"Hyderabad"},
    {"id":103,"name":"Aryan","address":"bihar"}
]

name = input("enter name: ")

found = False

for data in dictdata:
    if data["name"].upper() == name.upper():
        print("Record found successfully")
        print("id:", data["id"])
        print("name:", data["name"])
        print("address:", data["address"])
        found = True
        break

if not found:
    print("Record not found")


# loop ka use krke user se input lena hai maximum 5 student ka data lena aur usko dict in list me print karana hai aur usko id sirf dalne se pura detail print ho jaye 

students = []

user_choice = int(input("How many students data do you want to enter (1 to 5): "))

if user_choice < 1 or user_choice > 5:
    print("Please enter student between 1 to 5")
else:
    for i in range(1, user_choice + 1):
        print(f"\nEnter details of student {i}")

        name = input("Enter student name: ")
        sid = int(input("Enter student id: "))
        address = input("Enter student address: ")

        student_data = {
            "name": name,
            "id": sid,
            "address": address
        }

        students.append(student_data)

    print("Student Data Entered Successfully")


    print(" All Students Data:")
    for s in students:
        print(s)

    search_id = int(input("Enter student ID to view details: "))

    found = False
    for s in students:
        if s["id"] == search_id:
            print("\n Student Found")
            print("Name    :", s["name"])
            print("ID      :", s["id"])
            print("Address :", s["address"])
            found = True
            break

    if not found:
        print(" Student ID not found")

# phle data ko dict in list me likhna hai aur same data ko user se input lekar match karana hai aur use name se print hona chahiye


dictdata = [
    {"id":101,"name":"Abhishek","address":"gopalganj"},
    {"id":102,"name":"indixpert","address":"Hyderabad"},
    {"id":103,"name":"Aryan","address":"bihar"}
]

name = input("enter name: ")

found = False

for data in dictdata:
    if data["name"].upper() == name.upper():
        print("Record found successfully")
        print("id:", data["id"])
        print("name:", data["name"])
        print("address:", data["address"])
        found = True
        break

if not found:
    print("Record not found")


# user se 4 subject ka marks lena hai aur sabko sum percentage ke base pe usko division dena hai

s1  = int(input("enter your1 s1 marks: "))
s2 = int(input("enter your s2 marks: "))
s3  = int(input("enter your s3 marks: "))
s4  = int(input("enter your s4 marks: "))

total = s1+s2+s3+s4
print("total marks:", total)

percentage = (total/400)*100
print("percentage:",percentage)

if percentage >= 60:
    print("1st division")
elif percentage >= 45:
    print("2nd division")
elif percentage >= 30:
    print("3rd division")

else:
    print("you are fail")



# vowels check karna hai if else ka use karke


s = input("enter your name: ")

print(s.lower().count("a") + s.lower().count("e") + s.lower().count("i") + s.lower().count("o") + s.lower().count("u"))


