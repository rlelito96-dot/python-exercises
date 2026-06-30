import tkinter as tk
from tkinter import simpledialog, messagebox

# --- dane ---
users = []
products = []
ratings = []


# --- funkcje ---
def add_user():
    user = simpledialog.askstring("Add user", "Enter user name:")
    if user:
        users.append(user)
        messagebox.showinfo("Success", f"User {user} has been added!")


def show_users():
    if not users:
        messagebox.showinfo("Users", "Users list is empty.")
    else:
        messagebox.showinfo("Users", "\n".join(f"{i + 1}. {u}" for i, u in enumerate(users)))


def add_product():
    product = simpledialog.askstring("Add product", "Enter product name:")
    if product:
        products.append(product)
        messagebox.showinfo("Success", f"Product {product} has been added!")


def show_products():
    if not products:
        messagebox.showinfo("Products", "Products list is empty.")
    else:
        messagebox.showinfo("Products", "\n".join(f"{i + 1}. {p}" for i, p in enumerate(products)))


def add_rating():
    if not users or not products:
        messagebox.showwarning("Warning", "First add users and products!")
        return

    # wybór użytkownika
    user_num = simpledialog.askinteger("Add rating", f"Enter user number (1-{len(users)}):")
    if not user_num or not (1 <= user_num <= len(users)):
        messagebox.showerror("Error", "Invalid user number.")
        return
    user_index = user_num - 1

    # wybór produktu
    product_num = simpledialog.askinteger("Add rating", f"Enter product number (1-{len(products)}):")
    if not product_num or not (1 <= product_num <= len(products)):
        messagebox.showerror("Error", "Invalid product number.")
        return
    product_index = product_num - 1

    # wpisanie oceny
    rating = simpledialog.askinteger("Add rating", "Enter rating (1-5):")
    if not rating or not (1 <= rating <= 5):
        messagebox.showerror("Error", "Rating must be 1-5.")
        return

    ratings.append({
        "user": users[user_index],
        "product": products[product_index],
        "rating": rating
    })
    messagebox.showinfo("Success", f"Added rating {rating} for {products[product_index]} by {users[user_index]}")


def show_ratings():
    if not ratings:
        messagebox.showinfo("Ratings", "Rating list is empty.")
    else:
        messagebox.showinfo("Ratings", "\n".join(f"{r['user']} rated {r['product']} at {r['rating']}" for r in ratings))


# --- GUI ---
root = tk.Tk()
root.title("Ratings Program")
root.geometry("300x400")

tk.Button(root, text="Add user", width=25, command=add_user).pack(pady=5)
tk.Button(root, text="Show users", width=25, command=show_users).pack(pady=5)
tk.Button(root, text="Add product", width=25, command=add_product).pack(pady=5)
tk.Button(root, text="Show products", width=25, command=show_products).pack(pady=5)
tk.Button(root, text="Add rating", width=25, command=add_rating).pack(pady=5)
tk.Button(root, text="Show all ratings", width=25, command=show_ratings).pack(pady=5)
tk.Button(root, text="Quit", width=25, command=root.destroy).pack(pady=5)

root.mainloop()