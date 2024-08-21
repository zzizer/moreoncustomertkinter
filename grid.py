import customtkinter as ctk

app = ctk.CTk()

app.title("Custom Tkinter App Learning")
app.geometry('450x200')

def button_callback():
    pass

button = ctk.CTkButton(app, text="my button", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20)

app.mainloop()