from tkinter import *
from os import path

def register():
    global register_screen
    global username
    global password
    global username_entry
    global password_entry
    global access_level
    register_screen = Toplevel(main_screen) 
    register_screen.title("Register")
    register_screen.geometry("300x300")
 
    # Set text variables
    username = StringVar()
    password = StringVar()
    # Set label for user's instruction
    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()
    # Set username label
    username_label = Label(register_screen, text="Username * ")
    username_label.pack()
    # Set username entry
    # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    # Set password label
    password_label = Label(register_screen, text="Password * ")
    password_label.pack()
    # Set password entry
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    # Create access level buttons
    access_level = IntVar()
    admin_button = Radiobutton(register_screen, text=" Administrator", variable=access_level, val=1)
    admin_button.pack()
    user_button = Radiobutton(register_screen, text="Visitor\t", variable=access_level, val=2)
    user_button.pack()
    Label(register_screen, text="").pack()
    # Set register button
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()

def register_user():
    # get username and password
    path = "userinfo.txt"
    username_info = username.get()
    password_info = password.get()
    access_info = access_level.get()
    # Open file
    file = open(path, "a")
    # write username and password information into file
    file.write(username_info + ",")
    file.write(password_info + ",")
    file.write(str(access_info) + "\n")
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    access_level.set(0)
 
    # set a label for showing success information on screen 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry
    
    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()

def login_verify():
    file_path = "userinfo.txt"
    #get username and password
    username1 = username_verify.get()
    password1 = password_verify.get()
    # this will delete the entry after login button is pressed
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END) 
    #The method listdir() returns a list containing the names of the entries in the directory given by path.
    if path.exists(file_path):
        list_of_users = [line.rstrip('\n') for line in open(file_path)]
    else:
        user_not_found()
    
    #defining verification's conditions
    for user in list_of_users:
        user_info_list = user.split(",")
        if username1 == user_info_list[0]:
            if password1 == user_info_list[1]:
                login_success(user_info_list[2])
                return
            else:
                password_not_recognised()
                return

    user_not_found()


def login_success(access_level):
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
 
    # create OK button
    Button(login_success_screen, text="OK", command=lambda: delete_login_success(access_level)).pack()

def delete_login_success(access_level):
    login_success_screen.destroy()
    if(access_level == "1"):
        admin_level_interface()
    else:
        visitor_level_interface()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def delete_data_container():
    data_container.destroy()
    
def admin_level_interface():
    global admin_level_interface_screen
    admin_level_interface_screen = Toplevel(login_screen)
    admin_level_interface_screen.geometry("400x300")
    display_users(True)
    register_button = Button(admin_level_interface_screen, text="Create User", command=register)
    register_button.pack()
    delete_button = Button(admin_level_interface_screen, text="Delete User", command=remove_user)
    delete_button.pack()
    reload_buttton = Button(admin_level_interface_screen, text="Reload", command=reload_page)
    reload_buttton.pack()
    
def visitor_level_interface():
    global visitor_level_interface_screen
    visitor_level_interface_screen = Toplevel(login_screen)
    visitor_level_interface_screen.geometry("400x300")
    display_users(False)
    
def display_users(is_admin):
    global data_container
    file_path = "userinfo.txt"
    index = 0
    Label(
         (admin_level_interface_screen if is_admin else visitor_level_interface_screen),
         text="Welcome " + ("Admin" if is_admin else "Visitor")
         ).pack()
    list_of_users = [line.rstrip('\n') for line in open(file_path)]
    data_container = Frame((admin_level_interface_screen if is_admin else visitor_level_interface_screen), width=400, height=300)
    data_container.pack()
    for user in list_of_users:
        index += 1
        user_info_list = user.split(",")
        Label(
             data_container,
             text= str(index) + ") User: " + user_info_list[0] + ", Password: " + (user_info_list[1] if is_admin else "N/A")
                     + ", Access Level: " + ("Admin" if is_admin else "Visitor")
             ).pack()
    #Scrollbar(data_container, orient=VERTICAL).pack(side=RIGHT)

def remove_user():
    delete_screen = Toplevel(admin_level_interface_screen) 
    delete_screen.title("Delete User")
    delete_screen.geometry("350x300")
    line = StringVar()
    Label(delete_screen, text="Input the line number of the record you want deleted").pack()
    line_entry = Entry(delete_screen, textvariable=line)
    line_entry.pack()
    Label(delete_screen, text="").pack()
    delete_button = Button(delete_screen, text="Delete", command=lambda: delete(int(line.get())))
    delete_button.pack()

def delete(line_number):
    src = "userinfo.txt"
    dest = "tempfile.txt"
    counter = 1
    with open(src, "r") as input:
        with open(dest, "w") as output: 
            for line in input:
                if counter != line_number:
                    output.write(line)
                counter += 1

    with open(dest, "r") as input:
        with open(src, "w") as output: 
            for line in input:
                output.write(line)
    remove_user.destroy()
        
def reload_page():
    delete_data_container()
    display_users(True)

def main_account_screen():
    global main_screen
    main_screen = Tk() 
    main_screen.geometry("300x250") 
    main_screen.title("Login/Register") 
    # create a Form label 
    Label(text="Choose Login Or Register", bg="white", width="300", height="2", font=("Calibri", 13)).pack() 
    Label(text="").pack()
    # create Login Button 
    Button(text="Login", height="2", width="30", command=login).pack() 
    Label(text="").pack() 
    # create a register button
    Button(text="Register", height="2", width="30", command=register).pack()
    # start the GUI
    main_screen.mainloop() 
     
#main function
main_account_screen()
