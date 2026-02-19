from src.menu.data import load_data, save_data
from src.menu.utils import get_valid_id


def delete_student():

    data = load_data()

    search_id = get_valid_id()

    new_data = [s for s in data if s["id"] != search_id]

    save_data(new_data)

    print(" Deleted (if ID existed)")
