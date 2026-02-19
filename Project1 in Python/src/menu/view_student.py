from src.menu.data import load_data


def view_student():

    students = load_data()

    if not students:
        print("No data found")
        return

    print("\n===== STUDENT LIST =====")

    for s in students:
        print(f"""
ID      : {s['id']}
Name    : {s['name']}
Address : {s['address']}
Email   : {s['email']}
-------------------------
""")
