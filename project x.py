



def show_tasks(shopping_list):
    """Showing list with strings"""
    if not shopping_list:
        print("\nNo product on the list yet. Add something.")
        return []

    print("\nYour shopping list:")

    for index, name in enumerate(shopping_list, 1):
        print(f"{index}. {name}")
        shopping_list.sort()

def add_tasks(shopping_list):
    """Adding strings to list"""
    adding = input("Enter product name:")
    shopping_list.append(adding.strip())
    for index, name in enumerate(shopping_list, 1):
        print(f"\nProduct {name} has been aded!")

def delete_task(shopping_list):
    """Removing strings from list"""
    if not shopping_list:
        print("No product on the list yet. Add something.")
    else:
        print("\nYour shopping list:")

    for index, name in enumerate(shopping_list, 1):
        print(f"{index}. {name}")

    try:
        deleting = int(input("\nEnter number of products to remove:"))
    except ValueError:
        print("Invalid input. Try again.")
        return

    checking = deleting -1

    if 0 <= checking < len(shopping_list):
        remove = shopping_list.pop(checking)
        print(f"Product {remove} has been removed!")
    else:
        print("Wrong number!Try again.")
        return

def save_file(shopping_list, file_name = "shopping_list.txt"):
    """Saving list to .txt file"""
    with open(file_name, "w", encoding = "utf-8") as f:
        f.write("Your shopping list:\n")
        for index, product in enumerate(shopping_list, 1):
            f.write(f"{index}. {product.strip()}\n")
    print("\nFile has been saved!")


def load_file(file_name = "shopping_list.txt"):
     """Loading list of strings from .txt file"""
     try:
        with open(file_name, "r", encoding = "utf-8") as f:
            return [line.strip() for line in f.readlines()]
     except FileNotFoundError:
         return []

shopping_list = []
load = load_file()

while True:

    print()
    print("1.Show tasks")
    print("2.Add task")
    print("3.Delete task")
    print("4.Save")
    print("5.Exit")

    try:
        user_choice = int(input("Enter action 1-5:"))
        if user_choice < 1 or user_choice > 5:
            print("\nInvalid!Choose number 1-5. ")
            continue

    except ValueError:
        print("\nInvalid!Choose number 1-5. ")
        continue

    if user_choice == "5":
        print("Program has been closed.Goodbye!")
        break

    if user_choice == "1":
        show_tasks(shopping_list)
    elif user_choice == "2":
        add_tasks(shopping_list)
    elif user_choice == "3":
        delete_task(shopping_list)
    elif user_choice == "4":
        save_file(shopping_list)