import tkinter
import random
from tkinter import messagebox



window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

#-----------------function to add data to text file----------------------#
def add_to_file():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) ==0 or len(username)==0 or len(password)==0:
        messagebox.showwarning(title="left fields empty", message='u left some fields empty')
    else:
        message = messagebox.askokcancel(title="entered details", 
                                     message=f'these are the entered credentials for {website} , username:{username} and password:{password}')
        if message:
            with open(file="Python/Tkinter/Password_Manager/passwords.txt", mode='a') as passwords_file:
                passwords_file.write( f"{website} ' | ' {username} ' | ' {password} \n")

def clear():
    website_entry.delete(0, tkinter.END)
    password_entry.delete(0, tkinter.END)
#-----------------function to generate new password ----------------------#
def generate_password():
    big_letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    small_letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-']

    big_letters_count = random.randint(2,4) 
    small_letters_count = random.randint(8,10) 
    numbers_count = random.randint(2,5) 
    symbols_count = random.randint(3,5)
    password_generated=[]
    for _ in range(big_letters_count):
        password_generated.append(random.choice(big_letters_list))
    for _ in range(small_letters_count):
        password_generated.append(random.choice(small_letters_list))
    for _ in range(numbers_count):
        password_generated.append(random.choice(numbers))
    for _ in range(symbols_count):
        password_generated.append(random.choice(symbols))
    random.shuffle(password_generated)
    shuffled_password = ''.join(password_generated)
    password_entry.insert(0,shuffled_password)
    password_entry.clipboard_append(shuffled_password)
    '''import pyperclip
       pyperclip.copy("thing to be copied")''' #other way to copy the generated password to clipboard
canvas = tkinter.Canvas(height=200,width=189)
image1 = tkinter.PhotoImage(file='Python/Tkinter/Password_Manager/logo.png')
canvas.create_image(100,95.5, image=image1)
canvas.grid(row=0,column=1)

website_label = tkinter.Label(text="Website Url:" , font=("consolas",12))
website_label.grid(row=1, column=0)

website_entry =  tkinter.Entry(width=50)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

username_label = tkinter.Label(text='Username:', font=("consolas",12))
username_label.grid(row=2, column=0)

username_entry = tkinter.Entry(width=50)
username_entry.insert(0,"paulanand926@gmail.com")
username_entry.grid(row=2,column=1,columnspan=2, pady=20)

password_label = tkinter.Label(text="Password:", font=("consolas",12))
password_label.grid(row=3,column=0)

password_entry = tkinter.Entry(width=30)
password_entry.grid(row=3,column=1)

generate_button = tkinter.Button(text="Generate Password",width=15, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = tkinter.Button(text='Add to notes',width=43, command=lambda:[add_to_file(), clear()])
add_button.grid(row=4,column=1, columnspan=2, pady=20)

window.mainloop()