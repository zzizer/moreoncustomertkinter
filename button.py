import customtkinter as tk
import tkinter as tk0

app = tk.CTk()

def button_fxn():
    print('button clicked')

button = tk.CTkButton(app, text='click me', command=button_fxn)
button.place(relx=0.5, rely=0.8, anchor= tk0.CENTER)

app.mainloop()