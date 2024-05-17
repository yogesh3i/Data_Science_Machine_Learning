import random
import smtplib
from tkinter import *
from tkinter import messagebox
import threading
import time

# Function to generate OTP
def generateOTP():
    randomCode = ''.join(str(random.randint(0, 9)) for i in range(6))
    return randomCode

# Function to send OTP to the receiver email
def sendOTP():
    global code, attempts
    receiver = receiverMail.get()
    code = generateOTP()
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    
    msg = 'Hello! \n This is your OTP: ' + code
    server.sendmail(sender, receiver, msg)
    server.quit()
    
    attempts = 0

# Function to check OTP validity
def checkOTP():
    global attempts
    entered_code = codeEntry.get()
    if entered_code == code:
        messagebox.showinfo('Success', 'Successful Verification!')
    else:
        attempts += 1
        if attempts >= max_attempts:
            messagebox.showinfo('Limit Exceeded', 'You have reached the maximum OTP entry limit. Please try again after 12 hours.')
            sendOTPButton.config(state=DISABLED)
        else:
            messagebox.showinfo('Error', 'Invalid OTP! Please try again.')

# GUI setup
otp = Tk()
otp.title('OTP Verification')
otp.geometry('750x400')
otp.config(bg='#FFF1DC')

sender = 'yogideotale33@gmail.com'
password = 'auzj dueh rsje ptfk'
code = ''
attempts = 0
max_attempts = 3

mailMsg = Label(otp, text="E-Mail", justify=LEFT, bg='#FFF1DC', font=("Arial", 16))
mailMsg.place(x=15, y=40)

receiverMail = Entry(otp, width=35, font=("Arial", 20), borderwidth=0)
receiverMail.place(x=100, y=40)

sendOTPButton = Button(otp, text="Send OTP", width=8, height=1, font=("Arial", 20), borderwidth=0, bg="#AA5656", fg="black", command=sendOTP)
sendOTPButton.place(x=280, y=100)

otpMsg = Label(otp, text="OTP", bg='#FFF1DC', font=('Arial', 16))
otpMsg.place(x=15, y=210)

codeEntry = Entry(otp, width=6, font=("Arial", 20), borderwidth=0)
codeEntry.place(x=100, y=210)

verifyButton = Button(otp, text="Verify", width=8, height=1, font=("Arial", 20), borderwidth=0, bg="#AA5656", fg="black", command=checkOTP)
verifyButton.place(x=280, y=280)

otp.mainloop()
