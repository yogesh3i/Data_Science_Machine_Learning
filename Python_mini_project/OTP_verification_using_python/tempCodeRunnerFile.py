import smtplib
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import simpledialog, messagebox
import random

# Function to generate a 6-digit OTP randomly
def generate_otp():
    return str(random.randint(100000, 999999))

# Function to send OTP to the user's email address
def send_otp_email(email, otp):
    sender_email = 'yogideotale33@gmail.com'  # Your Gmail address
    sender_password = 'Yogesh@123'      # Your Gmail password

    message = MIMEText(f'Your OTP is: {otp}')
    message['Subject'] = 'OTP Verification'
    message['From'] = sender_email
    message['To'] = email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(message)
        messagebox.showinfo('OTP Sent', 'OTP successfully sent to your email.')
    except Exception as e:
        messagebox.showerror('Error', f'Failed to send OTP: {str(e)}')

# Function to get the user's email address and send OTP
def get_email_and_send_otp():
    email = simpledialog.askstring('Email Address', 'Please enter your email address:')
    if email:
        otp = generate_otp()
        send_otp_email(email, otp)

# Main function to create GUI
def main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Button to trigger OTP sending process
    send_otp_button = tk.Button(root, text='Send OTP', command=get_email_and_send_otp)
    send_otp_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
