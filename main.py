from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#random passward generator

numbers = ["1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","^","&","*","_","-","+","=",",",".","?","/","~","`"]
words = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def generate_passward_function():
    numbers_list = [random.choice(numbers) for _ in range(random.randint(8,10))]
    words_list = [random.choice(words) for _ in range(random.randint(2,4))]
    symbols_list = [random.choice(symbols) for _ in range(random.randint(2,4))]

    passward_list = numbers_list + words_list + symbols_list

    random.shuffle(passward_list)
    passward_to_return = "".join(passward_list)
    passward_entry.insert(END,passward_to_return)
    pyperclip.copy(passward_to_return)
   
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    passward = passward_entry.get()
    if not website or not email or not passward:
        messagebox.showerror(title=f"Oops" , message="Don't leave these field empty")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}", message=f"These are detail entered: \nEmail : {email}"
                                                            f"\nPassward: {passward} \nIs it ok to save?")
        if is_ok:
            with open("C:/Users/sahil/OneDrive\Desktop/100dayPythonChallenge/Day 29/password-manager-start/data.txt",'a') as file:    
                file.write(f"{website:<30}"+ "  |  " + f"{email:<30}" + "  |  " + f"{passward:<20}" + "\n")
                website_entry.delete(0,END)
                email_entry.delete(0,END)
                email_entry.insert(END,"sahilmandalwar30@gmail.com")
                passward_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")

window.config(padx=50,pady=50,bg="white")

canvas = Canvas(width=200, height=200,bg="white",highlightthickness=0)
lock_image = PhotoImage(file="C:/Users/sahil/OneDrive/Desktop/100dayPythonChallenge/Day 29/password-manager-start/logo.png")
canvas.create_image(100,100, image=lock_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:" ,bg="white")
website_label.grid(row=1, column = 0)

website_entry = Entry(width=35)
website_entry.focus()  # will have cursor from start 
website_entry.grid(row=1,column=1,columnspan=2,sticky  = "w")

email_label = Label(text="Email/Username:" ,bg="white")
email_label.grid(row=2, column=0)

email_entry= Entry(width=35)  # width is attribute of entry not of grid
email_entry.insert(END,"sahilmandalwar30@gmail.com")   #END from tkinter Constant for the position at end
# we insert the text in the email_entry
email_entry.grid(row=2, column=1,columnspan=2,sticky  = "w")

passward_label = Label(text="Passward:" ,bg="white")
passward_label.grid(row=3, column=0)

passward_entry=Entry(width=21)
passward_entry.grid(row=3,column=1,sticky  = "w")

generate_passward = Button(text="Generate Passward",command=generate_passward_function)
generate_passward.grid(row=3,column=2)

add_button = Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2,sticky = "w")






window.mainloop()


