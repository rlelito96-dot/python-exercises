import sqlite3
import os

if not os.path.exists("kurka"):
    os.makedirs("kurka", exist_ok=True)

db_name = os.path.join("kurka/dupa.db")

def init_db():
    conn = sqlite3.connect("db_name")
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
            print(f"User {name} has been added!")
        except sqlite3.IntegrityError:
            print("User already exists.")

        conn.close()

    def add_product(name):
        conn= sqlite3.connect(db_name)
        c = conn.cursor()
        try:
            c.execute("INSERT INTO products (name) VALUES (?)", (name,))
            conn.commit()
            print(f"Product {name} has been added!")
        except sqlite3.IntegrityError:
            print("Product already exists.")

        conn.close()

    def add_rating():
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        c.execute("SELECT * FROM users")
        users = c.fetchall()
        if not users:
            print("Users list is empty.")
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
            print("Products list is empty.")
            conn.close()
            return

        print("\nProducts:")
        for p in products:
            print(f"{p[0]}. {p[1]}")

        try:
            product_id = int(input("Enter product ID."))
            if not any(p[0] == product_id for p in products):
                print("Invalid product ID.")
                conn.close()
                return
        except ValueError:
            print("Invalid input.")
            conn.close()
            return

        try:
            rating_value = int(input("Enter rating (1-5): "))
            if not 0 <= rating_value <= 6:
                print("Rating out of range.")
                conn.close()
                return
        except ValueError:
            print("Invalid input.")
            conn.close()
            return

        c.execute("INSERT INTO ratings (user_id, product_id, rating) VALUES (?, ?, ?)",
                  (user_id,product_id, rating_value))

        conn.commit()
        print("Ratings has been added!")
        conn.close()

        def show_users():
            conn = sqlite3.connect(db_name)
            c = conn.cursor()
            c.execute("SELECT * FROM users")
            users = c.fetchall()
            if not users:
                print("Not users yet.")
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
                print("Not products yet.")
            else:
                print("\nProducts list:")
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


    init.db()
    print("SQLite DB ready!")

    while True:








