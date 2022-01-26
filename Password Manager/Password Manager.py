from tkinter import *
from tkinter import messagebox  #This is not included (amongst other modules) in the import that imports "all" from tkinter
from random import choice, shuffle, randint
import pyperclip    #imported package to copy stuff to the clipboard


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def randomize():
    letters_par.set(randint(0, len(letters)))
    numbers_par.set(randint(0, len(numbers)))
    symbols_par.set(randint(0, len(symbols)))

def gen_pass():

    letters_num = int(letters_par.get())
    numbers_num = int(numbers_par.get())
    symbols_num = int(symbols_par.get())

    if letters_num == 0 and numbers_num == 0 and symbols_num == 0:
        messagebox.showinfo(title= "Oops", message= "No password parameters set, please try again.")
    else:
        #Create 3 lists of 'NUM' randomly genereated letters, numbers, and symbols respectively
        pass_letters = [choice(letters) for i in range(letters_num)]
        pass_numbers = [choice(numbers) for i in range(numbers_num)]
        pass_symbols = [choice(symbols) for i in range(symbols_num)]

        #combines them into a single list and shuffles it
        pass_list = pass_letters + pass_numbers + pass_symbols
        shuffle(pass_list)

        #Takes each item in a list and converts it into a string, joining each item in the list with an empty space in this case
        password = "".join(pass_list)

        pass_entry.delete(0, END)
        pass_entry.insert(0, string = password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(password) == 0 or email == "@gmail.com":
        messagebox.showinfo(title= "Oops", message= "Not all the required fields are filled! Please try again.")
        #A popup which shows a message and makes user click ok
    else:
        confirmation = messagebox.askokcancel(title= website, message= f"These are the details entered: \nEmail/Username: {email} \nPassword: {password} \nWould you like to save these credentials?")
        #This messagebox function returns true or false based on whether the use clicked ok or cancel

        if confirmation:
            with open("data.txt", "a") as data_file:
                data_file.write(f"Website/Platform: {website} | Email/Username: {email} | Password: {password}\n")

                website_entry.delete(0, END)    #This delete() function deletes whats in the entry from the 0th character to the end of the entry
                pass_entry.delete(0, END)

                email_entry.delete(0, END)
                email_entry.insert(0, string="@gmail.com")

                letters_par.set(0)
                numbers_par.set(0)
                symbols_par.set(0)
                
                pyperclip.copy(password)
            
            messagebox.showinfo(title= "Completed", message= "Credentials have been added to the directory and the password has been copied to your clipboard.")
            website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)

canvas = Canvas(width= 200, height= 200, highlightthickness= 0) 
logo = PhotoImage(file= "logo.png")  
canvas.create_image(100, 100, image = logo)
canvas.grid(row= 0, column= 1, columnspan= 3)

website_label = Label(text= "Website/Platform:")
website_label.grid(row= 1, column= 0)
website_entry = Entry()
website_entry.grid(row= 1, column= 1, columnspan= 3, sticky= EW) 
#sticky = EW is used to make the widgets align how you'd think they'd aline dammit >:(
#also helps it span the columns properly... piss me off

website_entry.focus()   #This will have it so when the app is launched, the cursor will be focused on the website entry box
#ie, the cursor will already be in the website entry box, ready for you to start typing




#Emails/Usernames
email_label = Label(text= "Email/Username:")
email_label.grid(row= 2, column= 0)
email_entry = Entry()

email_entry.insert(0, string="@gmail.com") #0 is to enter text at beginning of cursor and END is used to insert it at end of cursor?
#in this case it doesnt matter cause our cursor is gonna start elsewhere all the time (website entry box)

email_entry.grid(row= 2, column= 1, columnspan= 3, sticky= EW)




#Password parameters
par_label = Label(text= "Password Parameters:")
par_label.grid(row = 3, column= 0, )

letters_par = DoubleVar(value=0)    #Set a variable for the spinbox to be equal to (using textvariable = ), such that we can set it later
numbers_par = DoubleVar(value=0)
symbols_par = DoubleVar(value=0)

letters_label = Label(text= "Letters")
letters_label.grid(row= 3, column= 1)
letters_spinbox = Spinbox(from_=0, to= len(letters), textvariable= letters_par)
letters_spinbox.grid(row= 4, column= 1, sticky= EW)

numbers_label = Label(text= "Numbers")
numbers_label.grid(row= 3, column= 2)
numbers_spinbox = Spinbox(from_=0, to= len(numbers), textvariable= numbers_par)
numbers_spinbox.grid(row= 4, column= 2, sticky= EW)

symbols_label = Label(text= "Symbols")
symbols_label.grid(row= 3, column= 3)
symbols_spinbox = Spinbox(from_=0, to= len(symbols), textvariable= symbols_par)
symbols_spinbox.grid(row= 4, column= 3, sticky= EW)


gen_pass_button = Button(text= "Randomize Parameters", command= randomize)
gen_pass_button.grid(row= 4, column= 4, sticky= NSEW)




#Password field
pass_label = Label(text= "Password:")
pass_label.grid(row= 5, column= 0)
pass_entry = Entry()
pass_entry.grid(row= 5, column= 1, sticky= EW, columnspan= 3)

gen_pass_button = Button(text= "Generate Password", command= gen_pass)
gen_pass_button.grid(row= 5, column= 4, sticky= EW)




#Save Credentials
add_pass_button = Button(text= "Add", command= save)
add_pass_button.grid(row= 6, column= 1, columnspan= 3, sticky= EW)






window.mainloop()