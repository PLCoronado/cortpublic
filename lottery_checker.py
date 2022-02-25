from tabnanny import check
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import smtplib
import os
import sys

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    
    application_path = os.path.dirname(sys.executable)
elif __file__:
    
    application_path = os.path.dirname(os.path.realpath(__file__))
    
file_name = "\images"
dir_path = application_path + file_name

print(dir_path)

root = tk.Tk()
root.geometry("750x600")
root.pack_propagate(True)
root.resizable()

number_frame = tk.Frame(root)
number_frame.pack(side=TOP, anchor=NW, padx=10)

number_label=Label(number_frame, text="Enter number:")
number_label.grid(row=0, column=0)
number_box = Entry(number_frame, width=20)
number_box.focus_set()
number_box.grid(row=0, column=1, padx=10, pady=10)



result_frame = tk.LabelFrame(root, text="Have you won...?")
result_frame.pack(fill=BOTH, expand=True)

result_words = Label(result_frame, text="")
result_words.pack()

result_image = Label(result_frame, image="")
result_image.pack(fill=BOTH, expand=True)

win_img = Image.open(rf"{dir_path}\rafa.jpg").resize((750,500))
win_img = ImageTk.PhotoImage(win_img)
lose_img = Image.open(rf"{dir_path}\loser.png").resize((750,500))
lose_img = ImageTk.PhotoImage(lose_img)



def get_result():
    global number_box
    number = number_box.get()
    if (number=="65032"):
        result_words.configure(text="Congratulations!! You are one of the few winners (in fact, the only one).\n\n Your AWESOME prize will soon (or late) be credited to your account")
        result_image.configure(image=win_img)

        gmail_user = 'cortlotto1@gmail.com'
        gmail_password = 'CORTlotto1'

        sent_from = gmail_user
        to = ['pablolucas1740@gmail.com']
        subject = 'We have a winner'
        body = "Do the transfer, quickly!"

        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)


        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

    else:
        result_words.configure(text="Oh, I am sooo sorry, unfortunately, and unexpectedly, you have lost :(")
        result_image.configure(image=lose_img)
check_button = Button(number_frame, text="CHECK", command=get_result)
check_button.grid(row=0, column=2)

root.mainloop()
    