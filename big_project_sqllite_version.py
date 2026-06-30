import os
import sqlite3

db_name = "data.db"

def init_db():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS ratings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        product_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(product_id) REFERENCES products(id)
    )
    """)

    conn.commit()
    conn.close()


class User:
    def __init__(self, id_, name):
        self.name = name
        self.id = id_

class Product:
    def __init__(self, id_, name):
        self.name = name
        self.id = id_

class Rating:
    def __init__(self, user, product, rating):
        self.user = user
        self.product = product
        self.rating = rating

def add_user(name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
        print(f"User {name} added.")
    except sqlite3.IntegrityError:
        print("User already exists.")
    conn.close()

def add_product(name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO products (name) VALUES (?)", (name,))
        conn.commit()
        print(f"Product {name} added.")
    except sqlite3.IntegrityError:
        print("Product already exists.")
    conn.close()


def add_rating():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute("SELCET * FROM users")
    users = c.fetchall()
    if not users:
        print("Add users first!")
        conn.close()
        return
    print("\nUsers:")
    for u in users:
        print(f"{u[0]}. {u[1]}")
    try:
        user_id = int(input("Enter user ID: "))
        if not any(u[0] == user_id for u in users):
            print("Invalid user ID.")
            conn.close()
            return
    except ValueError:
        print("Invalid input.")
        conn.close()
        return

    c.execute("SELECT * FROM products")
    products = c.fetchall()
    if not products:
        print("Add products first!")
        conn.close()
        return
    print("\nProducts:")
    for p in products:
        print(f"{p[0]}. {p[1]}")

    try:
        product_id = int(input("Enter product ID:"))
        if not any(p[0] == product_id for p in products):
            print("Invalid input.")
            conn.close()
            return

    except ValueError:
        print("Invalid input.")
        conn.close()
        return

    try:
        rating_value = int(input("Enter rating (1-5): "))
        if not 1 <= rating_value <= 6:
            print("Rating out of range.")
            conn.close()
            return
    except ValueError:
        print("Invalid input.")
        conn.close()
        return


    c.execute("INSERT * INTO ratings (user_id, product_id, rating) VALUES(?, ?, ?)",
              (user_id, product_id, rating_value))
    conn.commit()
    print("Rating added!")
    conn.close()

def show_users():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    if not users:
        print("No users yet.")
    else:
        print("\nUsers list:")
        for u in users:
            print(f"{u[0]}. {u[1]}")
    conn.close()

def show_products():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    if not products:
        print("No products yet.")
    else:
        print("Products list:")
        for p in products:
            print(f"{p[0]}. {p[1]}")
    conn.close()

def show_ratings():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""
            SELECT users.name, products.name, ratings.rating"
            FROM ratings
            JOIN users ON users.id = ratings.user_id
            JOIN products ON products.id = ratings.product_id           
              """)
    ratings = c.fetchall()
    if not ratings:
        print("No ratings yet.")
    else:
        print("\nRatings:")
        for r in ratings:
            print(f"{r[0]} rated {r[1]}: {r[2]}")
    conn.close()

init_db()
print("SQLite DB ready!")

while True:
    print("\nMenu:")
    print("1. Add user")
    print("2. Show users")
    print("3. Add product")
    print("4. Show products")
    print("5. Add rating")
    print("6. Show all ratings")
    print("0. Quit")

    choice = input("Choose action: ")
    if choice == "1":
        add_user(input("Enter user name: "))
    elif choice == "2":
        show_users()
    elif choice == "3":
        add_product(input("Enter product name: "))
    elif choice == "4":
        show_products()
    elif choice == "5":
        add_rating()
    elif choice == "6":
        show_ratings()
    elif choice == "0":
        print("Bye!")
        break
    else:
        print("Invalid choice.")