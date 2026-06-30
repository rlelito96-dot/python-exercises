import tkinter as tk

# Funkcja do dodawania cyfr i operatorów do wyświetlacza
def add_to_expression(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(symbol))

# Funkcja do czyszczenia wyświetlacza
def clear():
    entry.delete(0, tk.END)

# Funkcja do obliczenia wyrażenia
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Tworzymy okno główne
root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)  # blokuje zmianę rozmiaru okna
root.geometry("300x400")      # ustalamy wymiary okna (prostokąt)

# Wyświetlacz (Entry)
entry = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

# Lista przycisków w układzie grid
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Tworzymy przyciski
for (text, row, col) in buttons:
    if text == "=":
        b = tk.Button(root, text=text, font=("Arial", 18), bg="#4CAF50", fg="white",
                      command=calculate)
    else:
        b = tk.Button(root, text=text, font=("Arial", 18),
                      command=lambda t=text: add_to_expression(t))
    b.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Przyciski czyszczenia (Clear)
clear_button = tk.Button(root, text="C", font=("Arial", 18), bg="#f44336", fg="white",
                         command=clear)
clear_button.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Ustawiamy wagi kolumn i wierszy, żeby przyciski się skalowały równomiernie
for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(6):
    root.rowconfigure(i, weight=1)

root.mainloop()