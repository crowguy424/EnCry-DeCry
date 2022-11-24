from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password = code.get()

    if password == "6969":
        screen2 = Toplevel(screen)
        screen2.title("decryption")
        ln_icon = PhotoImage(file="deco.png")
        screen2.iconphoto(False, ln_icon)
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd69")

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPTED", font="arial", fg="white", bg="#00bd69").place(x=10, y=0)
        text2 = Text(screen2, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypt)
    elif password == "":
        messagebox.showerror("encryption", "Input Password")
    elif password != "6969":
        screen2 = Toplevel(screen)
        screen2.title("Error")
        alert_icon = PhotoImage(file="alert.png")
        screen2.iconphoto(False, alert_icon)
        screen2.geometry("200x50")
        screen2.configure(bg="#ed4833")
        Label(screen2, text="Incorrect Key", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)


def encrypt():
    password = code.get()

    if password == "6969":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        en_icon = PhotoImage(file="encrypt.png")
        screen1.iconphoto(False, en_icon)
        screen1.geometry("400x200")
        screen1.configure(bg="#ed4833")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPTED", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt)
    elif password == "":
        messagebox.showerror("encryption", "Input Password")
    elif password != "6969":
        screen1 = Toplevel(screen)
        screen1.title("Error")
        alert_icon = PhotoImage(file="alert.png")
        screen1.iconphoto(False, alert_icon)
        screen1.geometry("200x50")
        screen1.configure(bg="#ed4833")
        Label(screen1, text="Incorrect Key", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)




def main_screen():
    global screen
    global code
    global text1
    screen =Tk()
    screen.geometry("375x398")

    #icon
    image_icon = PhotoImage(file="key.png")
    screen.iconphoto(False, image_icon)
    screen.title("CrptApp")

    def reset():
        code.set("")
        text1.delete(1.0, END)


    Label(text="Enter text for encryption and decryption", fg="black", font=("calbri", 13)).place(x=10, y=10)
    text1=Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter secret key for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=170)
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)
    Button(text="ENCRYPT", height=2, width=23, bg="#ed3838", fg="white", bd=0, command=encrypt).place(x=10, y=260)
    Button(text="DECRYPT", height=2, width=23, bg="#00bd46", fg="white", bd=0, command=decrypt).place(x=200, y=260)
    Button(text="RESET", height=2, width=50, bg="#1029ff", fg="white", bd=0, command=reset).place(x=10, y=300)


    screen.mainloop()


main_screen()