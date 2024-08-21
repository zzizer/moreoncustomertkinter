import tkinter as tk0
import customtkinter as tk

app = tk.CTk()

tk.set_appearance_mode('system')
tk.set_default_color_theme('blue')

app.title("Custom Tkinter App Learning")
# app.geometry("500x240")

frame = tk.CTkFrame(master=app,
                    width=200, height=200, corner_radius=10
                    )
frame.pack(padx=20, pady=20)

tk_textbox = tk0.Text(frame, highlightthickness=0)
tk_textbox.grid(row=0, column=0, sticky="nsew")

ctk_textbox_scrollbar = tk.CTkScrollbar(frame, command=tk_textbox.yview)
ctk_textbox_scrollbar.grid(row=0, column=1, sticky='ns')

tk_textbox.config(yscrollcommand=ctk_textbox_scrollbar.set)

app.mainloop()