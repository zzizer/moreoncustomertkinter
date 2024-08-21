import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("Two-Frame Window")
app.geometry("800x500")

# Configure grid layout for the app
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)

# Create the sidebar frame without rounded corners
sidebar_frame = ctk.CTkFrame(app, width=250, corner_radius=0)
sidebar_frame.grid(row=0, column=0, sticky="ns", padx=(0, 10))  # Adjust padding to create space from the main content
sidebar_frame.grid_rowconfigure(6, weight=1)

# Add content to the sidebar frame
logo_label = ctk.CTkLabel(sidebar_frame, text="Olivers' Enterprize Ltd", font=ctk.CTkFont(size=20, weight="bold"))
logo_label.grid(row=0, column=0, padx=20, pady=20)

sidebar_button_1 = ctk.CTkButton(sidebar_frame, text="Home")
sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

sidebar_button_2 = ctk.CTkButton(sidebar_frame, text="Sales")
sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

sidebar_button_3 = ctk.CTkButton(sidebar_frame, text="Supplies")
sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

sidebar_button_4 = ctk.CTkButton(sidebar_frame, text="Expenditures")
sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)

sidebar_button_5 = ctk.CTkButton(sidebar_frame, text="Support")
sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)

logout_button = ctk.CTkButton(sidebar_frame, text="Logout", fg_color="red")
logout_button.grid(row=6, column=0, padx=20, pady=20, sticky="s")

# Create the main content frame with rounded corners
main_content_frame = ctk.CTkFrame(app, corner_radius=20)
main_content_frame.grid(row=0, column=1, sticky="nsew", padx=10)  # Adjust padding to create space from the sidebar

# Configure the grid layout in the main_content_frame to make the textbox extend horizontally
main_content_frame.grid_columnconfigure(0, weight=1)

# Add content to the main content frame
content_label = ctk.CTkLabel(main_content_frame, text="Dashboard", font=ctk.CTkFont(size=20, weight="bold"))
content_label.grid(row=0, column=0, padx=20, pady=20, sticky='w')  # Aligning to the start (left) of the frame

# Introduction text
introduction_text = (
    "This is where your main intro goes. "
    "This is where your main intro goes. "
    "This is where your main intro goes. "
    "This is where your main intro goes."
)

# Create the introduction_textbox and limit its vertical size
introduction_textbox = ctk.CTkTextbox(main_content_frame, height=60)  # Adjust height to fit about 3 lines of text
introduction_textbox.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
introduction_textbox.insert("0.0", introduction_text)
introduction_textbox.configure(state="disabled")

# Create a tab view
title_label = ctk.CTkLabel(main_content_frame, text='Tab View Example', font=ctk.CTkFont(size=16, weight='bold'))
title_label.grid(row=2, column=0, padx=20, pady=5, sticky='w')

tabView = ctk.CTkTabview(main_content_frame)
tabView.grid(row=3, column=0, padx=20, pady=5, sticky="nsew")

tabView.add('Tab 1')
tabView.add('Tab 2')
tabView.add('Tab 3')

tabView.set('Tab 1')

label1 = ctk.CTkLabel(tabView.tab('Tab 1'), text='This is tab 1')
label1.place(relx=0.5, rely=0.1, anchor= tk.CENTER)

button1 = ctk.CTkButton(tabView.tab('Tab 1'), text='More Info', command=lambda: print('button 1 clicked'))
button1.place(relx=0.5, rely=0.3, anchor= tk.CENTER)

label2 = ctk.CTkLabel(tabView.tab('Tab 2'), text='This is tab 2')
label2.place(relx=0.5, rely=0.1, anchor= tk.CENTER)

button2 = ctk.CTkButton(tabView.tab('Tab 2'), text='More Info', command=lambda: print('button 2 clicked'))
button2.place(relx=0.5, rely=0.6, anchor= tk.CENTER)

label3 = ctk.CTkLabel(tabView.tab('Tab 3'), text='This is tab 3')
label3.place(relx=0.5, rely=0.1, anchor= tk.CENTER)

button3 = ctk.CTkButton(tabView.tab('Tab 3'), text='More Info', command=lambda: print('button 3 clicked'))
button3.place(relx=0.5, rely=0.9, anchor= tk.CENTER)

app.mainloop()
