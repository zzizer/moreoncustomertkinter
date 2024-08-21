import customtkinter as tk
import tkinter as tk0

app = tk.CTk()

app.title("Custom Tkinter App Learning")
app.geometry("500x240")

textbox = tk.CTkTextbox(app)
textbox.grid(row=0, column=0, padx=20, pady=20)

text = "Hello, World!"

textbox.insert(0.0, text)
textbox.configure(state='disabled') # normal, disabled

button = tk.CTkButton(app, text='Enable', command=lambda: textbox.configure(state='normal'))
button.place(relx=0.5, rely=0.5, anchor=tk0.CENTER)

app.mainloop()