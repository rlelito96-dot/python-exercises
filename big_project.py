import os, json


print("\nWELCOME IN MY PROGRAM!")

users = []
products = []
ratings = []


def save_data():
    with open("users.json", "w", encoding="utf8") as f:
        json.dump(users, f, indent=4)

    with open("products.json", "w", encoding="utf8") as f:
        json.dump(products, f, indent=4)

    with open("ratings.json", "w", encoding="utf8") as f:
        json.dump(ratings, f, indent=4)

def load_data():
    global users, products, ratings

    if os.path.exists("users.json"):
        with open("users.json", "r", encoding="utf8") as f:
            users = json.load(f)
    if os.path.exists("products.json"):
        with open("products.json", "r", encoding="utf8") as f:
            products = json.load(f)

    if os.path.exists("ratings.json"):
        with open("ratings.json", "r", encoding="utf8") as f:
            ratings = json.load(f)

load_data()

def add_user():
    user = input("Enter user name to add: ".strip())
    users.append(user)
    save_data()
    print(f"User {user} has been added to list!")


def show_users():
    if not users:
        print(f"\nUsers list is empty. Add something.")
    else:
        print(f"\nUsers list: ")
        for i, u in enumerate(users, start=1):
            print(f"{i}.{u}")

def add_product():
    new_product = input("Enter product name: ")
    products.append(new_product)
    save_data()
    print(f"{new_product} has been added to list!")

def show_products():
    if not products:
        print(f"\nProducts list is empty. Add something.")
    else:
        print(f"\nProducts list: ")
        for i, p in enumerate(products, start=1):
            print(f"{i}.{p}")

def add_rating():
    if not users or not products:
        print(f"First add users and products!")
        return

    while True:
        show_users()

        try:
            user_index = int(input(f"Enter user number:")) -1
            if not (0 <= user_index < len(users)):
                print(f"Wrong action. Try again.")
                continue
        except ValueError:
            print(f"Invalid input. Try again.")
            continue

        print(f"Products:")
        show_products()
        try:
            product_index = int(input(f"Enter product number:")) -1
            if not (0 <= product_index < len(products)):
                print(f"Wrong action. Try again.")
                continue
        except ValueError:
            print(f"Invalid input. Try again.")
            continue
        try:
            rating = int(input(f"Enter rating (1-5): "))
            if not (1 <= rating < 6):
                print(f"Number out of range. Choose straight number 1-5.")
                continue
            ratings.append({"user": users[user_index],
                            "product": products[product_index],
                            "rating": rating})
            save_data()
            print(f"Added a rating {rating} for product {products[product_index]} by {users[user_index]}")
            break
        except ValueError:
            print(f"Wrong action. Choose straight number 1-5.")
            continue

def show_ratings():
    if not ratings:
        print("Rating list is empty. Add something.")
    else:
        print("Ratings list:")
        for r in ratings:
            print(f"{r['user']} rated {r['product']} at {r['rating']} ")


while True:

    print()
    print("1.Add user")
    print("2.Show users")
    print("3.Add product")
    print("4.Show products")
    print("5.Add rating")
    print("6.Show all ratings")
    print("0.Quit")


    try:
        user_choice = int(input("\nChoose action: "))
    except ValueError:
        print("Choose straight number 0-6.")
        continue

    if user_choice == 1:
        add_user()
    elif user_choice == 2:
        show_users()
    elif user_choice == 3:
        add_product()
    elif user_choice == 4:
        show_products()
    elif user_choice == 5:
        add_rating()
    elif user_choice == 6:
        show_ratings()
    elif user_choice == 0:
        print("\nProgram has been ended.")
        break
    else:
        print("\nWrong action! Try again.")



