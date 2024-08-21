import tkinter as tk0
import customtkinter as tk

app = tk.CTk()

app.title("Custom Tkinter App Learning")
app.geometry("500x240")

tabView = tk.CTkTabview(app)
tabView.pack(padx=20,pady=20)

tabView.add('Tab 1')
tabView.add('Tab 2')
tabView.add('Tab 3')

tabView.set('Tab 1')

button1 = tk.CTkButton(tabView.tab('Tab 1'), text='click me', command=lambda: print('button 1 clicked'))
button1.place(relx=0.5, rely=0.3, anchor= tk0.CENTER)

button2 = tk.CTkButton(tabView.tab('Tab 2'), text='click me', command=lambda: print('button 2 clicked'))
button2.place(relx=0.5, rely=0.6, anchor= tk0.CENTER)

button3 = tk.CTkButton(tabView.tab('Tab 3'), text='click me', command=lambda: print('button 3 clicked'))
button3.place(relx=0.5, rely=0.9, anchor= tk0.CENTER)

app.mainloop()