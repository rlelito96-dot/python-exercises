import os, json

if not os.path.exists("data"):
    os.makedirs("data", exist_ok=True)

class User:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {"name": self.name}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"])

class Product:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {"product": self.name}

    @classmethod
    def from_dict(cls, data):
        return cls(data["product"])

class Rating:
    def __init__(self, user, product, rating):
        self.user = user
        self.product = product
        self.rating = rating

    def to_dict(self):
        return {
            "user": self.user.name,
            "product": self.product.name,
            "rating": self.rating

        }

    @classmethod
    def from_dict(cls, data, users, products):
        user = next(u for u in users if u.name == data["user"])
        product = next(p for p in products if p.name == data["product"])
        return cls(user, product, data["rating"])

print("\nWELCOME IN MY PROGRAM!")

users = []
products = []
ratings = []


def save_data():
    with open("users.json", "w", encoding="utf8") as f:
        json.dump([u.to_dict() for u in users], f, indent=4)

    with open("products.json", "w", encoding="utf8") as f:
        json.dump([p.to_dict() for p in products], f, indent=4)

    with open("ratings.json", "w", encoding="utf8") as f:
        json.dump([r.to_dict() for r in ratings], f, indent=4)

def load_data():
    global users, products, ratings

    if os.path.exists("users.json"):
        with open("users.json", "r", encoding="utf8") as f:
            users = [User.from_dict(d) for d in json.load(f)]
    if os.path.exists("products.json"):
        with open("products.json", "r", encoding="utf8") as f:
            products = [Product.from_dict(d) for d in json.load(f)]

    if os.path.exists("ratings.json"):
        with open("ratings.json", "r", encoding="utf8") as f:
            ratings = [Rating.from_dict(d, users, products) for d in json.load(f)]

load_data()

def add_user():
    name = input("Enter user name to add: ".strip())
    user = User(name)
    users.append(user)
    save_data()
    print(f"User {user} has been added to list!")


def show_users():
    if not users:
        print(f"\nUsers list is empty. Add something.")
    else:
        print(f"\nUsers list: ")
        for i, u in enumerate(users, start=1):
            print(f"{i}.{u.name}")

def add_product():
    name = input("Enter product name: ")
    product = Product(name)
    products.append(product)
    save_data()
    print(f"{product} has been added to list!")

def show_products():
    if not products:
        print(f"\nProducts list is empty. Add something.")
    else:
        print(f"\nProducts list: ")
        for i, p in enumerate(products, start=1):
            print(f"{i}.{p.name}")

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
            ratings.append(
                Rating(users[user_index],
                products[product_index],
                rating))

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
            print(f"{r.user.name} rated {r.product.name} at {r.rating} ")


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