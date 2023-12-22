
import New_Registration
import login_page
import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("LOGIN AUTHENTICATION PAGE")

bkg = "#636e72"
flag = 0
frame = tk.Frame(root, bg=bkg)

button_login = tk.Button(frame, text="LOGIN", font=('verdana', 12), bg='orange',
                                  command=lambda: login_page.login())
button_login.grid(row=1, column=0, columnspan=2, pady=10, padx=10, sticky='nsew')
button_register = tk.Button(frame, text="NEW REGISTRATION", font=('verdana', 12), bg='orange',
                                  command=lambda: New_Registration.registration())
button_register.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky='nsew')
frame.grid(row=0, column=0)
root.mainloop()
exit(True)
