from src.menu.data import load_data
from src.menu.utils import get_valid_id


def search_student():

    data = load_data()

    search_id = get_valid_id()

    for s in data:
        if s["id"] == search_id:
            print(s)
            return

    print(" Student not found")
