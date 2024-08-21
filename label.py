import tkinter as tk
import customtkinter as ctk

app = ctk.CTk()

app.title("Custom Tkinter App Learning")
app.geometry("500x240")

label = ctk.CTkLabel(
    master=app, text="Hello, World!", corner_radius=10,
    fg_color=('white', 'gray75'))

label.pack(padx=20, pady=20)

app.mainloop()