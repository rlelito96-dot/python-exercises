from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)

############################

import tkinter as tk
import time

# Tworzymy okno
root = tk.Tk()
root.title("Migająca dioda")
root.geometry("200x200")

# Tworzymy „diodę” jako kwadrat
canvas = tk.Canvas(root, width=100, height=100)
canvas.pack(pady=40)
led = canvas.create_oval(10, 10, 90, 90, fill="gray")

# Funkcja migania
def blink():
    current_color = canvas.itemcget(led, "fill")
    new_color = "green" if current_color == "gray" else "gray"
    canvas.itemconfig(led, fill=new_color)
    root.after(1000, blink)  # powtarza co 1 sekundę

blink()
root.mainloop()