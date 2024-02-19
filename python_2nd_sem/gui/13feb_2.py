from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("password manager")
window.config(padx=50, pady=50)



# canvas = Canvas(width=200, height=224,  highlightthickness=0)
# pass_img = PhotoImage(file="pass.jpg")
# canvas.create_image(100, 112, image=pass_img)
# canvas.grid(column=1, row=1)




#save
def save():
    website = Website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    messagebox.showinfo(title="saved", message=f"saved details for {website}")

    with open("password.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        
        Website_entry.delete(0, END)
        password_entry.delete(0, END)



#labels 

Website_label = Label(text="Website Name: ")
email_label = Label(text="Email/username: ")
password_label = Label(text="Password: ")

Website_label.grid(row=1, column=1)

email_label.grid(row=2, column=1)

password_label.grid(row=3, column=1)

#entry

Website_entry = Entry(width=35)
Website_entry.grid(row=0, column=1, columnspan=2)
Website_entry.focus()



email_entry = Entry(width=35)
email_entry.grid(row=1, column=1, columnspan=2)
email_entry.insert(0, "sanskar1@gmail.com")


password_entry = Entry(width=35)
password_entry.grid(row=2,column=1,columnspan=2)

#button

button = Button(text="Add Password" , command=save)
button.grid(row=5, column=1, columnspan=2)
# add_button = Radiobutton(text="Add")
# add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()