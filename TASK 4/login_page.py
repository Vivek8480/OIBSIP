import tkinter as tk
from tkinter import messagebox
from twilio.rest import Client
import mysql.connector

def login():
    root = tk.Tk()
    root.title("LOGIN")

    # Database connection
    connection = mysql.connector.connect(
        host='localhost', user='root', password='123456', port='3306', database='LOGIN_CREDENTIALS')
    cursor = connection.cursor()

    bkg = "#636e72"
    flag = 0
    frame = tk.Frame(root, bg=bkg)

    label_phoneno = tk.Label(frame, text="Phone number: ", font=('verdana', 10), bg=bkg)
    entry_phoneno = tk.Entry(frame, font=('verdana', 10))

    label_OTP = tk.Label(frame, text="OTP: ", font=('verdana', 10), bg=bkg)
    entry_OTP = tk.Entry(frame, font=('verdana', 10))
    def check_db(phoneno):
        insert_query= "select ph_no from users_login_details"
        try:
            ph_no_list=[]
            cursor.execute(insert_query)
            rows= cursor.fetchall()
            phoneno2=float(phoneno1)
            for i in rows:
                ph_no_list.append(i)
            if (phoneno2,) in ph_no_list:
                messagebox.showinfo("success", "login successful")
            else:
                messagebox.showinfo("failed", "login unsuccessful. It seems to be look like you have have registered yet...")       
                                
            

        except mysql.connector.Error as e:
            print("Error:", e)
            messagebox.showerror("Error", "Failed to login")
    def otp_verify(verify_sid, client):
        global flag
        global phoneno1
        phoneno1=entry_phoneno.get()
        phoneno = "+91" + entry_phoneno.get()
        OTP = entry_OTP.get()

        try:
            verification_check = client.verify.services(verify_sid).verification_checks.create(
                to=phoneno,
                code=OTP
            )
            print(verification_check.status)

            if verification_check.status == 'approved':
                flag = 1
                check_db(phoneno)
            else:
                print("Invalid OTP. Please enter the correct OTP and submit.")
                messagebox.showwarning("Warning", "Invalid OTP")
        except Exception as e:
            print("Error occurred during OTP verification:", e)
            messagebox.showerror("Error", "Failed to verify OTP")

    def send_otp():
        global flag
        flag = 0

        try:
            account_sid = "AC16947aba5653754ad5b15f230a7e6e63"
            auth_token = "4e38f4ebd5e33ee5e9808ae075f33fbb"
            verify_sid = "VAe17e6a097e444568d8d07fdc2dc91356"
            client = Client(account_sid, auth_token)

            phoneno = "+91" + entry_phoneno.get()

            verification = client.verify.services(verify_sid).verifications.create(
                to=phoneno,
                channel="sms"
            )
            print(verification.status)

            label_OTP.grid(row=6, column=0, sticky='e')
            entry_OTP.grid(row=6, column=1, pady=10, padx=10)

            button_submit = tk.Button(frame, text="Submit", font=('verdana', 12), bg='orange',
                                    command=lambda: otp_verify(verify_sid, client))
            button_submit.grid(row=7, column=0, columnspan=2, pady=10, padx=10, sticky='nsew')
        except Exception as e:
            print("Error occurred while sending OTP:", e)
            messagebox.showerror("Error", "Failed to send OTP")

    button_getotp = tk.Button(frame, text="Get OTP", font=('verdana', 12), bg='orange', command=send_otp)

    # Grid layout
    label_phoneno.grid(row=4, column=0, sticky='e')
    entry_phoneno.grid(row=4, column=1, pady=10, padx=10)

    button_getotp.grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky='nsew')

    frame.grid(row=0, column=0)
    root.mainloop()
    exit()
