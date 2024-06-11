from tkinter import *
from tkinter import messagebox
import base64

def main_screen():
    global screen
    global code
    global text1

    # Geometry of Screen
    screen = Tk()
    screen.geometry("375x398")

    # Label for Text
    Label(text="Enter Text for Encryption And Decryption", fg="Black", font=("calibri", 13)).place(x=10, y=10)
    text1 = Text(screen, font=("Roboto", 20), bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    # Label for Secret Key
    Label(text="Enter Secret Key For Encryption And Decryption", fg="black", font=("calibri", 13)).place(x=10, y=170)
    code = StringVar()
    entry = Entry(screen, textvariable=code, width=19, bd=0, font=("arial", 25), show="*")
    entry.place(x=10, y=220)

    # Encrypt function
    def encrypt():
        password = code.get()
        if password == "1234":
            screen1 = Toplevel(screen)
            screen1.title("Encryption")
            screen1.geometry("400x200")
            screen1.configure(bg="#ed3833")
            
            message = text1.get(1.0, END)
            encode_message = message.encode("ascii")
            base64_bytes = base64.b64encode(encode_message)
            encrypted_message = base64_bytes.decode("ascii")

            Label(screen1, text="ENCRYPTED", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
            text2 = Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)
            text2.insert(END, encrypted_message)

        elif password=="":
            messagebox.showerror("encryption","Input Password")
        
        elif password !="1234":
            messagebox.shoerror("encryption","Invalid Password")
        else:
            messagebox.showwarning("Invalid Key", "Invalid secret key!")

    # Decrypt function
    def decrypt():
        password = code.get()
        if password == "1234":
            screen1 = Toplevel(screen)
            screen1.title("Decryption")
            screen1.geometry("400x200")
            screen1.configure(bg="#00bd56")

            message = text1.get(1.0, END)
            base64_bytes = message.encode("ascii")
            decoded_bytes = base64.b64decode(base64_bytes)
            decrypted_message = decoded_bytes.decode("ascii")

            Label(screen1, text="DECRYPTED", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
            text2 = Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)
            text2.insert(END, decrypted_message)
        else:
            messagebox.showwarning("Invalid Key", "Invalid secret key!")

    # Reset function
    def reset():
        code.set("")
        text1.delete(1.0, END)

    # Encrypt Button
    ButtonENPT = Button(text="ENCRYPT", height=2, width=23, bg="#ed3833", fg="white", bd=1, command=encrypt)
    ButtonENPT.place(x=10, y=290)

    # Decrypt Button
    ButtonDECPT = Button(text="DECRYPT", height=2, width=23, bg="#00bd56", fg="white", bd=1, command=decrypt)
    ButtonDECPT.place(x=200, y=290)

    # Reset Button
    ButtonRESET = Button(text="RESET", height=2, width=50, bg="#1089ff", fg="white", bd=1, command=reset)
    ButtonRESET.place(x=10, y=350)

    # Screen Title
    screen.title("EnptMES")
    screen.mainloop()

main_screen()

