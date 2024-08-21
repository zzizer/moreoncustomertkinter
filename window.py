import customtkinter

customtkinter.set_appearance_mode("system") # "light" or "dark" mode
customtkinter.set_default_color_theme("blue") # "blue", "green", "red", "purple", "black", "white", "yellow", "orange", "grey", "pink", "brown", "cyan", "magenta", "teal", "lime", "indigo", "amber", "lightblue", "lightgreen", "lightred", "lightpurple", "lightblack", "lightwhite", "lightyellow", "lightorange", "lightgrey", "lightpink", "lightbrown", "lightcyan", "lightmagenta", "lightteal", "lightlime", "lightindigo", "lightamber" color theme

app = customtkinter.CTk()

app.title("Custom Tkinter App Learning")
app.geometry("500x240")


app.mainloop()