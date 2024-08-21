import customtkinter as tk
import tkinter as tk0

app = tk.CTk()

app.geometry("300x300")

frame = tk.CTkFrame(master = app, 
                            width=400, height=200, bg_color='yellow', 
                            corner_radius=10)

frame.pack(padx=20,pady=20)

button = tk.CTkButton(frame, text='click me', command=lambda: print('button 1 clicked'))
button.place(relx=0.5, rely=0.3, anchor= tk0.CENTER)

button2 = tk.CTkButton(frame, text='click me', command=lambda: print('button 2 clicked'))
button2.place(relx=0.5, rely=0.6, anchor= tk0.CENTER)

app.mainloop()