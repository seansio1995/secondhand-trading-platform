from tkinter import *
from tkinter import ttk

import sqlite3
import backend
import time
from time import strftime
from time import gmtime

# Welcome Window

windows = []



def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def center_one(win):
    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    width = 640
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    #print (width)
    #print (height)
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


# Tk objects parts
welcome_window = Tk()
windows.append(welcome_window)
# Tk objects parts ends

# previous page global
# used in back to go to previous page
previous_page = welcome_window

screen_width = welcome_window.winfo_screenwidth()
screen_height = welcome_window.winfo_screenheight()

welcome_width = 800
welcome_height = 400
# welcome_window.geometry('{:d}x{:d}+{:d}+{:d}'.format(welcome_width, welcome_height, int((screen_width - welcome_width)/2), int((screen_height - welcome_height)/2)))
# Tk objects initalization

welcome_window.title("Secondhand Trading Platform")

#welcome_window.geometry('%dx%d' % (frameWidth, frameHeight))
# Tk objects initalization end

# Window display

# Window display ends


# frames
welcomeframe = ttk.Frame(welcome_window, padding="3 3 12 12")
welcomeframe.pack()
welcomeframe.columnconfigure(0, weight=1)
welcomeframe.rowconfigure(0, weight=1)
# frames end

# labesl
welcomelabel = Label(welcomeframe, text = "Welcome to Secondhand Trading Platform", font = (('MS'),26), justify = CENTER)
welcomelabel.pack(side = TOP, pady = 30, expand = YES)

# labesl end


# functions
def onClickSignup():
    global previous_page
    previous_page = welcome_window
    signup_window.deiconify()
    welcome_window.withdraw()

def onClicklogin():
    global previous_page
    previous_page = welcome_window
    login_window.deiconify()
    welcome_window.withdraw()

def onClickabout():
    global previous_page
    previous_page = welcome_window
    about_window.deiconify()
    welcome_window.withdraw()
    signup_window.withdraw()

def onExit():
    for i in windows:
        i.destroy()
# functions end

# buttons
login = Button(welcomeframe, text = "login", font = ('Arial',14),command = onClicklogin)
login.pack(side = TOP, pady = 20, expand = YES)

signup = Button(welcomeframe, text = "signup", font = ('Arial',14),command = onClickSignup)
signup.pack(side = TOP, pady = 20, expand = YES)


about = Button (welcomeframe,text = "  About  ",font = ('Arial',14),command = onClickabout)
about.pack(side = TOP, pady = 20, expand = YES)

exit = Button(welcomeframe, text = "Exit", font = ('Arial',14),command = onExit)
exit.pack(side = RIGHT, pady = 10)
# buttons end
#center(welcome_window)
# Welcome Window Ends



# Welcome Window Ends



# About Window

# Tk objects parts
about_window = Tk()
# Tk objects parts ends

windows.append(about_window)
about_width = 700
about_height = 500
# about_window.geometry('{:d}x{:d}+{:d}+{:d}'.format(about_width, about_height, int((screen_width - about_width)/2), int((screen_height - about_height)/2)))
# Tk objects parts ends

about_window.title("About")

# Tk objects initialization

# Tk objects initialization end

#function
def goto_about():
    for i in windows:
        i.withdraw()
    about_window.deiconify()

def goto_welcome():
    for i in windows:
        i.withdraw()
    welcome_window.deiconify()

# window display
about_window.withdraw()
# window display ends


# frames
frame_about = ttk.Frame(about_window, padding="3 3 12 12")
frame_about.grid(column=0, row=0, sticky=(N, W, E, S))
frame_about.columnconfigure(0, weight=1)
frame_about.rowconfigure(0, weight=1)

ttk.Label(frame_about, text="Developed by UVa students, the second-hand trading platform is an ideal place for people who want to buy or sell their devices",font = ('Arial',20),wraplength=600).grid(column=1, row=1, sticky=E)
Button(frame_about, font = ('Arial', 14),text = "Back", command = lambda :goto_welcome()).grid(column = 3, row = 3, stick = E, padx = 20, pady = 20)


#center(about_window)








# Signup Window


# Tk objects parts
signup_window = Tk()

windows.append(signup_window)
signup_width = 700
signup_height = 400
#signup_window.geometry('{:d}x{:d}+{:d}+{:d}'.format(signup_width, signup_height, int((screen_width - signup_width)/2), int((screen_height - signup_height)/2)))
# Tk objects parts ends


# Tk objects initalization
signup_window.title("Secondhand Trading Platform -- Sign up")
# Tk objects initalization end

# window display
signup_window.withdraw()
# window display ends


# frames
frame_signup = ttk.Frame(signup_window, padding="3 3 12 12")
frame_signup.grid(column=0, row=0, sticky=(N, W, E, S))
frame_signup.columnconfigure(0, weight=1)
frame_signup.rowconfigure(0, weight=1)

#frame_temp = ttk.Frame(signup_window, padding="3 3 12 12")
#Button(frame_signup, text = 'go temp', command = lambda : Tk.controller.show_frame(frame_temp))
# frames end

# input variable
first_name_var = StringVar(signup_window)
last_name_var = StringVar(signup_window)
username_var = StringVar(signup_window)
password_var = StringVar(signup_window)
email_var = StringVar(signup_window)
phone_var = StringVar(signup_window)
address_line_1_var = StringVar(signup_window)
city_var = StringVar(signup_window)
state_var = StringVar(signup_window)
zip_code_var = StringVar(signup_window)
user_type_var = StringVar(signup_window)
credit_var = StringVar(signup_window)

# input variable end

# labesl

ttk.Label(frame_signup, font = ('Arial', 14),text="First Name: ").grid(column=1, row=2, sticky=E)
firstname_input = ttk.Entry(frame_signup, width=20, textvariable=first_name_var)
firstname_input.grid(column=2, row=2, sticky=W)
firstname_input.focus()

ttk.Label(frame_signup, font = ('Arial', 14),text="Last Name: ").grid(column=1, row=3, sticky=E)
lastname_input = ttk.Entry(frame_signup, width=20, textvariable=last_name_var)
lastname_input.grid(column=2, row=3, sticky=W)

ttk.Label(frame_signup, font = ('Arial', 14),text="Username: ").grid(column=1, row=4, sticky=E)
username_input = ttk.Entry(frame_signup, width=20, textvariable=username_var)
username_input.grid(column=2, row=4, sticky=W)

ttk.Label(frame_signup, font = ('Arial', 14),text="Password: ").grid(column=1, row=5, sticky=E)
password_input = ttk.Entry(frame_signup, width=20, textvariable=password_var)
password_input.grid(column=2, row=5, sticky=W)

ttk.Label(frame_signup, font = ('Arial', 14),text="Email address: ").grid(column=1, row=6, sticky=E)
email_input = ttk.Entry(frame_signup, width=20, textvariable=email_var)
email_input.grid(column=2, row=6, sticky=W)

ttk.Label(frame_signup,font = ('Arial', 14), text="Phone Number: ").grid(column=1, row=7, sticky=E)
phone_input = ttk.Entry(frame_signup, width=10, textvariable=phone_var)
phone_input.grid(column=2, row=7, sticky=W)

ttk.Label(frame_signup,font = ('Arial', 14), text="Address Line 1: ").grid(column=1, row=8, sticky=E)
address1_input = ttk.Entry(frame_signup, width=30, textvariable=address_line_1_var)
address1_input.grid(column=2, row=8, sticky=W)

ttk.Label(frame_signup,font = ('Arial', 14), text="City: ").grid(column=1, row=9, sticky=E)
city_input = ttk.Entry(frame_signup, width=20, textvariable=city_var)
city_input.grid(column=2, row=9, sticky=W)
ttk.Label(frame_signup, font = ('Arial', 14),text="State: ").grid(column=3, row=9, sticky=E)
state_input = ttk.Entry(frame_signup, width=2, textvariable=state_var)
state_input.grid(column=4, row=9, sticky=W)
ttk.Label(frame_signup, font = ('Arial', 14),text="Zip Code: ").grid(column=5, row=9, sticky=E)
state_input = ttk.Entry(frame_signup, width=5, textvariable=zip_code_var)
state_input.grid(column=6, row=9, sticky=W)

# https://pythonspot.com/en/tk-dropdown-example/
choices = {'Seller', 'Buyer'}
user_type_var.set('Seller')  # set the default option

popupMenu = OptionMenu(frame_signup, user_type_var, *choices)
ttk.Label(frame_signup, font = ('Arial', 14),text="User Type: ").grid(column=1, row=10, sticky=E)
popupMenu.grid(column=2, row=10)


ttk.Label(frame_signup,font = ('Arial', 14), text="CreditCard: ").grid(column=1, row=11, sticky=E)
credit_input = ttk.Entry(frame_signup, width=30, textvariable=credit_var)
credit_input.grid(column=2, row=11, sticky=W)
ttk.Label(frame_signup,font = ('Arial', 10), text="(Mandatory for Sellers)").grid(column=3, row=11, sticky=W)

# labesl end

# functions


# on change dropdown value
def change_dropdown(*args):
    print(user_type_var.get())



def submit_signup(*args):
    try:
        first_name = str(first_name_var.get())
        print("first name: " + first_name)

        last_name = str(last_name_var.get())
        print("last name: " + last_name)

        username = str(username_var.get())
        print("username: " + username)

        if backend.checkUsernameExist(username):
            print ("username already exists!")
            popupWindow = Toplevel(signup_window)
            popupWindow.title('Info')
            Label(popupWindow, font = ('Arial',13), text="Username already taken!").grid(column=0, row=0, sticky=(E,W,N,S),padx = 30, pady = 30)
            Button(popupWindow,text = "OK", font = ('Arial',13),command = lambda: popupWindow.destroy()).grid(row=1,column=0,padx = 30, pady = 20)

            return
        password = str(password_var.get())
        print("password: " + password)

        email = str(email_var.get())
        print("email: " + email)

        phone = str(phone_var.get())
        print("phone: " + phone)

        address = str(address_line_1_var.get() + ". " + str(city_var.get() + ", " + str(state_var.get()) + " " + str(zip_code_var.get())))

        print("address: " + address)

        is_seller = (str(user_type_var.get()) == 'Seller')

        print("is_seller: " + str(is_seller))

        credit = credit_var.get()

        id = 1

        # backend.createUser(is_seller)
        # print(" created ")

        if is_seller:
            if len(credit) == 0:
                noCredit = Toplevel(signup_window)
                noCredit.title('Info')
                Label(noCredit, font = ('Arial',14), text="Credit Card is mandatory!").grid(column=0, row=0, sticky=(E,W,N,S),padx = 30, pady = 30)
                Button(noCredit,text = "OK", font = ('Arial',14),command = lambda: noCredit.destroy()).grid(row=1,column=0,padx = 30, pady = 20)
                return None
            else:
                backend.insertSeller(first_name, last_name, username, password, email, phone, address, credit)

        else:
            backend.insertBuyer(first_name, last_name, username, password, email, phone, address, None)
        welcome_window.deiconify()
        signup_window.withdraw()

    except ValueError:
        pass

# functions end

# buttons
user_type_var.trace('w', change_dropdown)
signup_window.bind('<Return>', submit_signup)

# link function to change dropdown

Button(frame_signup, font = ('Arial', 14),text="Sign Up", command=submit_signup).grid(column=6, row=12, sticky=E)

# back button
Button(frame_signup, font = ('Arial', 14),text = "Back", command = lambda :goto_welcome()).grid(column = 1, row = 12, sticky=W)
for child in frame_signup.winfo_children(): child.grid_configure(padx=5, pady=5)
# buttons end

#center(signup_window)
# Signup Window Ends
















# Login Window

# Tk objects parts
login_window = Tk()
windows.append(login_window)
login_width = 350
login_height = 160
# login_window.geometry('{:d}x{:d}+{:d}+{:d}'.format(login_width, login_height, int((screen_width - login_width)/2), int((screen_height - login_height)/2)))
login_window.title("Log in")
# Tk objects parts ends


# Tk objects initialization

# Tk objects initialization end

# window display
login_window.withdraw()
# window display ends



# globals
current_user = ""
current_seller = ""
buyer_credit = StringVar()
buyer_info = ""







# frames
frame_login = ttk.Frame(login_window, padding="3 3 12 12")
frame_login.grid(column=0, row=0, sticky=(N, W, E, S))
frame_login.columnconfigure(0, weight=1)
frame_login.rowconfigure(0, weight=1)


username_var_login = StringVar(login_window)
password_var_login = StringVar(login_window)
user_type_var_login = StringVar(login_window)


ttk.Label(frame_login, font = ('Arial', 14), text="Username: ").grid(column=1, row=2)


# username_var_login.set("antzy9")

username_input = ttk.Entry(frame_login,font = ('Arial', 14), width=20, textvariable=username_var_login)
username_input.grid(column=2, row=2, sticky=W)


ttk.Label(frame_login, font = ('Arial', 14), text="Password: ").grid(column=1, row=3)


# password_var_login.set("password")

password_input = ttk.Entry(frame_login, font = ('Arial', 14), width=20, textvariable=password_var_login, show='*')
password_input.grid(column=2, row=3, sticky=W)



# https://pythonspot.com/en/tk-dropdown-example/
choices = {'Seller', 'Buyer'}
user_type_var_login.set('Buyer')  # set the default option

popupMenu = OptionMenu(frame_login, user_type_var_login, *choices)
ttk.Label(frame_login, font = ('Arial', 14), text="User Type: ").grid(column=1, row=4, sticky=E)
popupMenu.grid(column=2, row=4)


def goto_welcome():
    for i in windows:
        i.withdraw()
    welcome_window.deiconify()

def update_user_name_all(username):
    buyer_main_user['text'] = username
    buyer_user_user['text'] = username
    buyer_device_user['text'] = username
    transaction_buyer['text'] = username
    seller_main_user['text'] = username

# on change dropdown value
def change_dropdown(*args):
    print(user_type_var.get())

def submit_login(*args):
    try:

        username = str(username_var_login.get())
        print("username: " + username)

        password = str(password_var_login.get())
        print("password: " + password)


        is_seller = (str(user_type_var_login.get()) == "Seller")

        print("is_seller: " + str(is_seller))

        if authenticate(username, password, is_seller):
            global current_user
            if not is_seller:
                global buyer_info
                # buyer_credit.set(find_credit_num(buyer_id, seller_id)[0])
                # print (buyer_credit.get())
                buyer_info = get_buyer_info(buyer_id)
                current_user = (username)
                # print (current_user)
                update_user_name_all(current_user)
                update_wishlist()
                update_order_history()
                update_result()
                buyer_main_window.deiconify()
                login_window.withdraw()
            else:
                current_user = (username)
                update_user_name_all(current_user)
                # print(current_user)
                update_offered_device()
                seller_main_window.deiconify()
                login_window.withdraw()
        else:
            incorrectPW = Toplevel(login_window)
            incorrectPW.title('Info')
            Label(incorrectPW, font = ('Arial',13), text="Incorrect Password").grid(column=0, row=0, sticky=(E,W,N,S),padx = 30, pady = 30)
            Button(incorrectPW,text = "OK", font = ('Arial',13),command = lambda: incorrectPW.destroy()).grid(row=1,column=0,padx = 30, pady = 20)


    except ValueError:
        pass

    #Got the values from the form.  Would do a query that finds user with username and password

def authenticate(username, password, is_seller):
    conn = sqlite3.connect("secondhand.sqlite3")
    cur = conn.cursor()

    if is_seller:
        query = "SELECT * FROM Seller WHERE username = ? AND password = ?"

    else:
        query = "SELECT * FROM Buyer WHERE username = ? AND password = ?"
    try:
        cur.execute(query, (username, password))
        result = cur.fetchone()
        if result != None:
           user_id = result[0]
           user_name = result[1]
            #go to main page, passing in the user_id to query for results
           print("Welcome user " + user_name + " with id " + str(user_id))
           conn.close()
           return True
        else:
            #Say authentication failed
            print("authentication failed")
            conn.close()
            return False
    except:
        print("table not exists please sign up first")
        conn.close()
        welcome_window.deiconify()
        login_window.withdraw()


# link function to change dropdown
user_type_var_login.trace('w', change_dropdown)


Button(frame_login, font = ('Arial', 12), text="Login", command=submit_login).grid(column=2, row=5, sticky=E)
# back button
Button(frame_login, font = ('Arial', 12),  text = "Back", command = lambda :goto_welcome()).grid(column = 1, row = 5, sticky=W)

for child in frame_login.winfo_children(): child.grid_configure(padx=5, pady=5)

username_input.focus()
login_window.bind('<Return>', submit_login)


#center(login_window)
# buttons end




# Login Window ends











# Buyer_main Window    by Kun Fang

# Tk objects parts
buyer_main_window = Tk()
windows.append(buyer_main_window)
buyer_main_width = 1270
buyer_main_height = 700
# buyer_main_window.geometry('{:d}x{:d}+{:d}+{:d}'.format(buyer_main_width, buyer_main_height, int((screen_width - buyer_main_width)/2), int((screen_height - buyer_main_height)/2)))
buyer_main_window.title("Secondhand Trading Platform -- Buyer")
# Tk objects parts ends


# Tk objects initialization
buyer_main_window.withdraw()
# Tk objects initialization end

# window display

# window display ends


# frames
buyer_main_frame = Frame(buyer_main_window)
buyer_main_frame.grid(row = 0,column = 0)
# frames end

# input variable
searchbar_input = StringVar(buyer_main_window)
# input variable end

# labels

# username info
Label(buyer_main_frame, font = ('Arial', 14), text = "Welcome! " ).grid(column=2,row = 0, sticky = E)
buyer_main_user = Button(buyer_main_frame, font = ('Arial', 14), relief = FLAT, text = current_user, command = lambda :goto_user_detail("buyer_main_window") )
buyer_main_user.grid(column=3,row = 0, sticky = W)
# log out button
Button(buyer_main_frame, font = ('Arial', 14),text = "Log out", command = lambda :log_out()).grid(column = 5, row = 0, stick = E)



search_bar = Entry(buyer_main_frame, font = ('Arial', 14), width = 102, textvariable=searchbar_input)
search_bar.grid(column=0, columnspan = 5, row=1, sticky=W)
search_button = Button(buyer_main_frame, font = ('Arial', 14),text = "Search", command = lambda :update_result())
search_button.grid(column = 5, row  = 1, stick = E)


# All offers posted


ttk.Label(buyer_main_frame, relief=GROOVE,  font = ('Arial', 14), text = "Name").grid(column = 0, row = 2, sticky = W, padx = 3)
ttk.Label(buyer_main_frame, relief=GROOVE,  font = ('Arial', 14), text = "Developer").grid(column = 1, row = 2, sticky = W)
ttk.Label(buyer_main_frame, relief=GROOVE,  font = ('Arial', 14), text = "Condition").grid(column = 2, row = 2, sticky = W)
ttk.Label(buyer_main_frame, relief=GROOVE,  font = ('Arial', 14), text = "Price").grid(column = 3, row = 2, sticky = W)

Button(buyer_main_frame, font = ('Arial', 14), text = "Details", command = lambda :onClickdetails("buyer_main_window")).grid(column = 5, row = 3, sticky = E)
Button(buyer_main_frame, font = ('Arial', 14), text = "Add to wishlist", command = lambda :onClickAddtoWishlist("buyer_main_window")).grid(column = 5, row = 4, sticky = E)
Button(buyer_main_frame, font = ('Arial', 14), text = "Buy", command = lambda :goto_transaction_window("buyer_main_window")).grid(column = 5, row = 5, sticky = E)
buyer_main_exit = Button(buyer_main_frame, text = "Exit", font = ('Arial',14),command = onExit)
buyer_main_exit.grid(column = 5, row = 7, sticky = E)

def onVsb(*args):
        """
        When the scrollbar moves, scroll the listboxes.
        """
        for lb in listboxes:
            lb.yview(*args)

def onMouseWheel(event):
    """
    Convert mousewheel motion to scrollbar motion.
    """
    if (event.num == 4):    # Linux encodes wheel as 'buttons' 4 and 5
        delta = 1
    elif (event.num == 5):
        delta = -1
    else:                   # Windows & OSX
        delta = int((-1)*event.delta/120)
        # print (delta)
    for lb in listboxes:
        lb.yview_scroll(delta, "units")
    # Return 'break' to prevent the default bindings from
    # firing, which would end up scrolling the widget twice.
    return "break"


listboxes = []
i = 0
while i<4:
    list = Listbox(buyer_main_frame, font = ('Arial', 14),height = 25, width = 25)
    list.bind("<MouseWheel>", onMouseWheel)
    list.bind("<Button-4>", onMouseWheel)
    list.bind("<Button-5>", onMouseWheel)
    list.grid(row = 3, column = i, rowspan = 5, sticky = W)
    listboxes.append(list)
    i = i+1
listboxes[0].activate(0)

def update_result(*args):
    conn = sqlite3.connect("secondhand.sqlite3")
    cur = conn.cursor()
    for i in listboxes:
        i.delete(0, END)

    if searchbar_input.get() == "":
        query = '''SELECT name, developer, condition, price FROM device, offer 
            where device.id = offer.device_id AND 
            NOT offer.status = ?'''
        for row in cur.execute(query,('Sold',)):
            j = 0
            for i in listboxes:
                i.insert(END, row[j])
                j = j + 1
    else:

        query = '''SELECT name, developer, condition, price FROM device, offer 
            where device.id = offer.device_id AND 
            NOT offer.status = ?
        '''
        for row in cur.execute(query,('Sold',)):
            temp = str(searchbar_input.get()).lower()
            if temp in str(row[0]).lower() or temp in str(row[1]).lower() or temp in str(row[2]).lower() or temp in str(row[3]).lower():
                j = 0
                for i in listboxes:
                    i.insert(END, row[j])
                    j = j + 1
            else:
                continue


    conn.close()


# store the current selection index
cur_index = 0

def getCurrentDeviceIDinBuyerMainPage():
    conn = sqlite3.connect("secondhand.sqlite3")
    cur = conn.cursor()
    query = '''SELECT device.id as device_id FROM device, offer, seller 
        where device.id = offer.device_id AND 
        offer.seller_id = seller.id AND
        device.name = ? AND
        device.developer = ? AND
        device.condition = ? AND
        offer.price = ?'''
    # print ("cur_index:" + str(cur_index))
    # print (listboxes[0].get(cur_index) + listboxes[1].get(cur_index)+ listboxes[2].get(cur_index)+ listboxes[3].get(cur_index))
    cur.execute(query, (listboxes[0].get(cur_index), listboxes[1].get(cur_index), listboxes[2].get(cur_index), listboxes[3].get(cur_index)))
    result = cur.fetchone()
    conn.close()
    device_id = int(result[0])
    return device_id

def getCurrentSellerIDinBuyerMainPage():
    conn = sqlite3.connect("secondhand.sqlite3")
    cur = conn.cursor()
    query = '''SELECT seller.id as seller_id FROM device, offer, seller 
        where device.id = offer.device_id AND 
        offer.seller_id = seller.id AND
        device.name = ? AND
        device.developer = ? AND
        device.condition = ? AND
        offer.price = ?'''
    # print ("cur_index:" + str(cur_index))
    # print (listboxes[0].get(cur_index) + listboxes[1].get(cur_index)+ listboxes[2].get(cur_index)+ listboxes[3].get(cur_index))
    cur.execute(query, (listboxes[0].get(cur_index), listboxes[1].get(cur_index), listboxes[2].get(cur_index), listboxes[3].get(cur_index)))
    result = cur.fetchone()
    conn.close()
    seller_id = int(result[0])
    return seller_id

def update_selection0(*args):
    global cur_index
    cur_index = listboxes[0].curselection()
    global cur_device_id
    cur_device_id = getCurrentDeviceIDinBuyerMainPage()
    global cur_seller_id
    cur_seller_id = getCurrentSellerIDinBuyerMainPage()
    # print (cur_device_id)
    # print (cur_seller_id)
    #print (cur_index)

def update_selection1(*args):
    global cur_index
    cur_index = listboxes[1].curselection()
    global cur_device_id
    cur_device_id = getCurrentDeviceIDinBuyerMainPage()
    global cur_seller_id
    cur_seller_id = getCurrentSellerIDinBuyerMainPage()
    # print (cur_device_id)
    # print (cur_seller_id)
    #print (cur_index)

def update_selection2(*args):
    global cur_index
    cur_index = listboxes[2].curselection()
    global cur_device_id
    cur_device_id = getCurrentDeviceIDinBuyerMainPage()
    global cur_seller_id
    cur_seller_id = getCurrentSellerIDinBuyerMainPage()
    # print (cur_device_id)
    # print (cur_seller_id)
    #print (cur_index)

def update_selection3(*args):
    global cur_index
    cur_index = listboxes[3].curselection()
    global cur_device_id
    cur_device_id = getCurrentDeviceIDinBuyerMainPage()
    global cur_seller_id
    cur_seller_id = getCurrentSellerIDinBuyerMainPage()
    # print (cur_device_id)
    # print (cur_seller_id)
    #print (cur_index)



update_result()
# conn = sqlite3.connect("secondhand.sqlite3")
# cur = conn.cursor()
#
# query = "SELECT device_name, device_model, device_condition, price FROM device, offer where device.device_id = offer.device_id"
# for row in cur.execute(query):
#     j = 0
#     for i in listboxes:
#         i.insert(END, row[j])
#         j = j + 1
#
#
# conn.close()






listboxes[0].bind('<ButtonRelease-1>', update_selection0)
listboxes[1].bind('<ButtonRelease-1>', update_selection1)
listboxes[2].bind('<ButtonRelease-1>', update_selection2)
listboxes[3].bind('<ButtonRelease-1>', update_selection3)
buyer_main_window.bind('<Return>', update_result)

# labels end
result = None

# functions
def log_out():
    password_var_login.set("")
    # print ("here"+password_var_login.get())
    for i in windows:
        i.withdraw()
    welcome_window.deiconify()

def updateDetailPage(device_id):
    # print (device_id)
    conn = sqlite3.connect("secondhand.sqlite3")
    cur = conn.cursor()

    query = '''SELECT device.id as device_id, name, developer, model, year, condition, price, date, username, email FROM device, offer, seller 
            where device.id = offer.device_id AND 
            offer.seller_id = seller.id AND
            device.id = ?'''

    cur.execute(query, (str(device_id),))
    detail_result = cur.fetchone()
    # print (detail_result)
    detail_ID.set(detail_result[0])
    detail_Name.set(detail_result[1])
    detail_Developer.set(detail_result[2])
    detail_Model.set(detail_result[3])
    detail_Year.set(detail_result[4])
    detail_Condition.set(detail_result[5])
    detail_Price.set(detail_result[6])
    detail_Date.set(detail_result[7])
    detail_username.set(detail_result[8])
    detail_Contact.set(detail_result[9])
    conn.close()
    # center_one(buyer_detail_window)

def getDeviceIDfromBuyermainPage():
    conn = sqlite3.connect("secondhand.sqlite3")
    cur = conn.cursor()
    query = '''SELECT device.id as device_id FROM device, offer, seller 
        where device.id = offer.device_id AND 
        offer.seller_id = seller.id AND
        device.name = ? AND
        device.developer = ? AND
        device.condition = ? AND
        offer.price = ?'''
    # print ("cur_index:" + str(cur_index))
    # print (listboxes[0].get(cur_index) + listboxes[1].get(cur_index)+ listboxes[2].get(cur_index)+ listboxes[3].get(cur_index))
    cur.execute(query, (listboxes[0].get(cur_index), listboxes[1].get(cur_index), listboxes[2].get(cur_index), listboxes[3].get(cur_index)))
    username = str(username_var_login.get())
    #print (str(wishlist.get(curselect)[0]))
    #print (str(wishlist.get(curselect)[1]))
    #print (str(wishlist.get(curselect)[2]))
    #print (str(wishlist.get(curselect)[3]))

    result = cur.fetchone()
    conn.close()
    return int(result[0])

def getSellerIDfromBuyermainPage():
    conn = sqlite3.connect("secondhand.sqlite3")
    cur = conn.cursor()
    query = '''SELECT seller.id as seller_id FROM device, offer, seller 
        where device.id = offer.device_id AND 
        offer.seller_id = seller.id AND
        device.name = ? AND
        device.developer = ? AND
        device.condition = ? AND
        offer.price = ?'''
    # print ("cur_index:" + str(cur_index))
    # print (listboxes[0].get(cur_index) + listboxes[1].get(cur_index)+ listboxes[2].get(cur_index)+ listboxes[3].get(cur_index))
    cur.execute(query, (listboxes[0].get(cur_index), listboxes[1].get(cur_index), listboxes[2].get(cur_index), listboxes[3].get(cur_index)))
    username = str(username_var_login.get())
    #print (str(wishlist.get(curselect)[0]))
    #print (str(wishlist.get(curselect)[1]))
    #print (str(wishlist.get(curselect)[2]))
    #print (str(wishlist.get(curselect)[3]))

    result = cur.fetchone()
    conn.close()
    return int(result[0])

def getDeviceIDfromUserdetailPage():
    conn = sqlite3.connect("secondhand.sqlite3")
    cur = conn.cursor()
    # curselect = wishlist.curselection()
    try:
        curselect = wishlist.curselection()[0]
        # print (curselect)

    except:
        if (wishlist.size() != 0):
            # print ("here")
            curselect = 0
        else:
            conn.close()
            return None

    tempquery = '''SELECT device.id as device_id FROM wish, buyer, device, offer
    where wish.buyer_id = buyer.id AND  
    device.id = offer.device_id AND
    device.id = wish.device_id AND
    buyer.username = ? AND
    device.name = ? AND
    device.developer = ? AND
    device.condition = ? AND
    offer.price = ?'''
    username = str(username_var_login.get())
    #print (str(wishlist.get(curselect)[0]))
    #print (str(wishlist.get(curselect)[1]))
    #print (str(wishlist.get(curselect)[2]))
    #print (str(wishlist.get(curselect)[3]))

    # print ((wishlist.size()))
    if (wishlist.size() != 0):
        cur.execute(tempquery,(username, wishlist.get(curselect)[0], wishlist.get(curselect)[1], wishlist.get(curselect)[2], wishlist.get(curselect)[3]))
        result = cur.fetchone()
        conn.close()
        return int(result[0])
    else:
        conn.close()
        return None


def getSellerIDfromUserdetailPage():
    conn = sqlite3.connect("secondhand.sqlite3")
    cur = conn.cursor()
    try:
        curselect = wishlist.curselection()[0]
        # print (curselect)

    except:
        if (wishlist.size() != 0):
            # print ("here")
            curselect = 0
        else:
            conn.close()
            return None


    tempquery = '''SELECT offer.seller_id as seller_id FROM wish, buyer, device, offer
    where wish.buyer_id = buyer.id AND
    device.id = offer.device_id AND
    device.id = wish.device_id AND
    buyer.username = ? AND
    device.name = ? AND
    device.developer = ? AND
    device.condition = ? AND
    offer.price = ?'''
    username = str(username_var_login.get())
    # print (str(wishlist.get(curselect)[0]))
    #print (str(wishlist.get(curselect)[1]))
    #print (str(wishlist.get(curselect)[2]))
    #print (str(wishlist.get(curselect)[3]))
    if (wishlist.size() != 0):
        cur.execute(tempquery,(username, wishlist.get(curselect)[0], wishlist.get(curselect)[1], wishlist.get(curselect)[2], wishlist.get(curselect)[3]))
        result = cur.fetchone()
        conn.close()
        return int(result[0])
    else:
        conn.close()
        return None

def onClickdetails(wherefrom):
    global previous_page
    global cur_seller_id
    previous_page = buyer_main_window
    if wherefrom == "buyer_main_window":
        cur_seller_id = getSellerIDfromBuyermainPage()
        if cur_seller_id:
            updateDetailPage(getDeviceIDfromBuyermainPage())
            for i in windows:
                i.withdraw()
        else:
            pass
        # buyer_detail_frame.update_idletasks()
        # buyer_detail_window.update_idletasks()
        # buyer_detail_width = buyer_detail_window.winfo_width()
        # buyer_detail_height = buyer_detail_window.winfo_height()
        # print (str(buyer_detail_width)+" "+str(buyer_detail_height))
        # print (str(buyer_detail_frame.winfo_width())+" "+str(buyer_detail_frame.winfo_height()))
        # center(buyer_detail_window)
        buyer_detail_window.deiconify()

    if wherefrom == "user_detail_window":
        cur_seller_id = getSellerIDfromUserdetailPage()
        this_Device_id = getDeviceIDfromUserdetailPage()
        if cur_seller_id != None and this_Device_id != None:
            previous_page = user_detail_window
            updateDetailPage(this_Device_id)
            for i in windows:
                i.withdraw()
            buyer_detail_window.deiconify()
            global cur_device_id
            cur_device_id = int(detail_ID.get())
        else:
            previous_page = buyer_main_window
            pass

        # buyer_detail_frame.update_idletasks()
        # buyer_detail_window.update_idletasks()
        # buyer_detail_width = buyer_detail_window.winfo_width()
        # buyer_detail_height = buyer_detail_window.winfo_height()
        # print (str(buyer_detail_width)+" "+str(buyer_detail_height))
        # print (str(buyer_detail_frame.winfo_width())+" "+str(buyer_detail_frame.winfo_height()))

    # print (cur_device_id)
    # print (cur_seller_id)



def onClickAddtoWishlist(wherefrom):
    if wherefrom == "buyer_main_window":
        time = str(strftime('%m/%d/%Y'))
        # print (time)
        buyerID =  backend.getBuyerIDbyUsername(current_user)
        if buyerID:
            backend.insertWish(getDeviceIDfromBuyermainPage(), buyerID, time)
            update_wishlist()
        else:
            print ("error adding to wish list, device is" + getDeviceIDfromBuyermainPage()+" buyerID is None")
    if wherefrom == "buyer_detail_window":
        time = str(strftime('%m/%d/%Y'))
        backend.insertWish(int(detail_ID.get()), backend.getBuyerIDbyUsername(current_user), time)
        update_wishlist()

# functions end


# buttons

# buttons end

#center(buyer_main_window)
# Buyer_main Window end












# Buyer_moreinfo Window
buyer_detail_window = Tk()
windows.append(buyer_detail_window)
buyer_detail_window.title("Secondhand Trading Platform -- Buyer device detail")
# Tk objects parts ends

# Tk objects initialization
buyer_detail_window.withdraw()
# Tk objects initialization end

# window display

# window display ends


# frames
buyer_detail_frame = Frame(buyer_detail_window)
buyer_detail_frame.pack(side = TOP, expand = YES, fill = BOTH)
# frames end


# labels

# username info
Label(buyer_detail_frame, font = ('Arial', 14), text = "Welcome! ").grid(row = 0, column=1, sticky = E, padx = 10, pady = 30)

buyer_device_user = Button(buyer_detail_frame, font = ('Arial', 14), relief = FLAT, text = current_user, command = lambda :goto_user_detail("buyer_detail_window") )
buyer_device_user.grid(row = 0, column=2, sticky = W, padx = 5, pady = 30)


# buttons
# log out button
Button(buyer_detail_frame, font = ('Arial', 14),text = "Log out", command = lambda :log_out()).grid( row = 0, column = 2,stick = E, padx = 10, pady = 10)
# back button
Button(buyer_detail_frame, font = ('Arial', 14),text = "Back", command = lambda :onClickBack()).grid(row = 3, column = 2, stick = E, padx = 10, pady = 10)
# add to wishlist button
temp = Button(buyer_detail_frame, font = ('Arial', 14),text = "Add to Wishlist", command = lambda :onClickAddtoWishlist("buyer_detail_window"))
temp.grid(row = 4, column = 2, stick = E, padx = 10, pady = 10)
# buy button
Button(buyer_detail_frame, font = ('Arial', 14),text = "Buy", command = lambda :goto_transaction_window("buyer_detail_window")).grid(row = 5, column = 2, stick = E, padx = 10, pady =10)


Button(buyer_detail_frame, text = "Exit", font = ('Arial',14),command = onExit).grid(row = 10, column = 2, sticky = E, padx = 10, pady = 10)

# buttons end


# input variable
detail_ID = StringVar(buyer_detail_window)
detail_Name = StringVar(buyer_detail_window)
detail_Developer = StringVar(buyer_detail_window)
detail_Model = StringVar(buyer_detail_window)
detail_Year = StringVar(buyer_detail_window)
detail_Condition = StringVar(buyer_detail_window)
detail_Price = StringVar(buyer_detail_window)
detail_Date = StringVar(buyer_detail_window)
detail_Condition = StringVar(buyer_detail_window)
detail_username = StringVar(buyer_detail_window)
detail_Contact = StringVar(buyer_detail_window)
# input variable end

# labels
Label(buyer_detail_frame, font = ('Arial', 14), text = "Device ID: ").grid(row = 1, column  = 0, sticky = E, padx = 10, pady = 10)
Label(buyer_detail_frame, font = ('Arial', 14), text = "Device Name: ").grid(row = 2, column  = 0, sticky = E, padx = 10, pady = 10)
Label(buyer_detail_frame, font = ('Arial', 14), text = "Device Developer: ").grid(row = 3, column  = 0, sticky = E, padx = 10, pady = 10)
Label(buyer_detail_frame, font = ('Arial', 14), text = "Device Model: ").grid(row = 4, column  = 0, sticky = E, padx = 10, pady = 10)
Label(buyer_detail_frame, font = ('Arial', 14), text = "Device Year: ").grid(row = 5, column  = 0, sticky = E, padx = 10, pady = 10)
Label(buyer_detail_frame, font = ('Arial', 14), text = "Device Condition: ").grid(row = 6, column  = 0, sticky = E, padx = 10, pady = 10)
Label(buyer_detail_frame, font = ('Arial', 14), text = "Offer Price: ").grid(row = 7, column  = 0, sticky = E, padx = 10, pady = 10)
Label(buyer_detail_frame, font = ('Arial', 14), text = "Offer Date: ").grid(row = 8, column  = 0, sticky = E, padx = 10, pady = 10)
Label(buyer_detail_frame, font = ('Arial', 14), text = "Seller username: ").grid(row = 9, column  = 0, sticky = E, padx = 10, pady = 10)
Label(buyer_detail_frame, font = ('Arial', 14), text = "Seller Contact: ").grid(row = 10, column  = 0, sticky = E, padx = 10, pady = 10)

Label(buyer_detail_frame, font = ('Arial', 14), textvariable = detail_ID).grid(row = 1, column  = 1, sticky = E, padx = 10, pady = 10)
Label(buyer_detail_frame, font = ('Arial', 14), textvariable = detail_Name).grid(row = 2, column  = 1, sticky = E, padx = 10, pady = 10)
Label(buyer_detail_frame, font = ('Arial', 14), textvariable = detail_Developer).grid(row = 3, column  = 1, sticky = E, padx = 10, pady = 10)
Label(buyer_detail_frame, font = ('Arial', 14), textvariable = detail_Model).grid(row = 4, column  = 1, sticky = E, padx = 10, pady = 10)
Label(buyer_detail_frame, font = ('Arial', 14), textvariable = detail_Year).grid(row = 5, column  = 1, sticky = E, padx = 10, pady = 10)
Label(buyer_detail_frame, font = ('Arial', 14), textvariable = detail_Condition).grid(row = 6, column  = 1, sticky = E, padx = 10, pady = 10)
Label(buyer_detail_frame, font = ('Arial', 14), textvariable = detail_Price).grid(row = 7, column  = 1, sticky = E, padx = 10, pady = 10)
Label(buyer_detail_frame, font = ('Arial', 14), textvariable = detail_Date).grid(row = 8, column  = 1, sticky = E, padx = 10, pady = 10)
Label(buyer_detail_frame, font = ('Arial', 14), textvariable = detail_username).grid(row = 9, column  = 1, sticky = E, padx = 10, pady = 10)
Label(buyer_detail_frame, font = ('Arial', 14), textvariable = detail_Contact).grid(row = 10, column  = 1, sticky = E, padx = 10, pady = 10)

# labels end

# functions


def goto_buyer_main():
    for i in windows:
        i.withdraw()
    buyer_main_window.deiconify()


def goto_user_detail(wherefrom):
    global previous_page
    if wherefrom == "buyer_detail_window":
        previous_page = buyer_detail_window
    elif wherefrom == "buyer_main_window":
        previous_page = buyer_main_window
    else:
        return None
    update_wishlist()
    update_order_history()
    for i in windows:
        i.withdraw()
    user_detail_window.deiconify()

# functions end
# buyer_detail_window.update_idletasks()
# # buyer_detail_window.geometry()
# buyer_detail_width = buyer_detail_window.winfo_width()
# buyer_detail_height = buyer_detail_window.winfo_height()
# print (str(buyer_detail_width)+" "+str(buyer_detail_height))
# buyer_detail_window.geometry('{:d}x{:d}+{:d}+{:d}'.format(buyer_detail_width, buyer_detail_height, int((screen_width - buyer_detail_width)/2), int((screen_height - buyer_detail_height)/2)))
# center(buyer_detail_window)
# Buyer_moreinfo Window end

# Buyer_user_detail_page Window
user_detail_window = Tk()

windows.append(user_detail_window)
user_detail_width = 730
user_detail_height = 750
#user_detail_window.geometry('{:d}x{:d}+{:d}+{:d}'.format(user_detail_width, user_detail_height, int((screen_width - user_detail_width)/2), int((screen_height - user_detail_height)/2)))
user_detail_window.title("Secondhand Trading Platform -- Buyer user detail")

user_detail_window.withdraw()

user_detail_frame = Frame(user_detail_window)
user_detail_frame.grid(row = 0,column = 0)
# username info
Label(user_detail_frame, font = ('Arial', 14), text = "Welcome! ").grid(column=1,row = 0, sticky = E, padx = 10, pady = 30)

buyer_user_user = Button(user_detail_frame, relief = FLAT, font = ('Arial', 14), text = current_user )
buyer_user_user.grid(column=2,row = 0, sticky = W, padx = 10, pady = 30)
# log out button
Button(user_detail_frame, font = ('Arial', 14),text = "Log out", command = lambda :log_out()).grid(column = 3, row = 0, sticky = E, padx = 20, pady = 20)
# Order history
Label(user_detail_frame, font = ('Arial', 14), text = "---Order History---").grid(column=0,row = 1, sticky = W, padx = 10, pady = 30)

# Button(user_detail_frame, font = ('Arial', 14),text = "Track").grid(column = 3, row = 2, sticky = E, padx = 20, pady = 20)

orderlist = Listbox(user_detail_frame, font = ('Arial', 14),height = 5, width = 55)
orderlist.grid(row = 2, column = 0, columnspan = 3, rowspan = 3, sticky = W)

# wishlist
Label(user_detail_frame, font = ('Arial', 14), text = "---Wishlist---").grid(column=0,row = 5, sticky = W, padx = 10, pady = 30)
wishlist = Listbox(user_detail_frame, font = ('Arial', 14),height = 15, width = 55)
wishlist.grid(row = 6, column = 0, columnspan = 3, rowspan = 6, sticky = W)
wishlist.activate(0)

Button(user_detail_frame, font = ('Arial', 14),text = "Detail", command = lambda :onClickdetails("user_detail_window")).grid(column = 3, row = 6, sticky = E, padx = 20, pady = 20)

Button(user_detail_frame, font = ('Arial', 14),text = "Buy", command = lambda :goto_transaction_window("user_detail_window")).grid(column = 3, row = 7, sticky = E, padx = 20, pady = 20)

Button(user_detail_frame, font = ('Arial', 14),text = "Delete", command = lambda :delete_wish_item()).grid(column = 3, row = 8, sticky = E, padx = 20, pady = 20)


Button(user_detail_frame, text = "Back", font = ('Arial',14),command = lambda :onClickBack()).grid(column = 3, row = 10, sticky = E, padx = 20, pady = 20)

def update_current_state(*args):
    global cur_device_id
    cur_1 = getDeviceIDfromUserdetailPage()
    if cur_1:
        cur_device_id = cur_1
    # print (cur_device_id)
    global cur_seller_id
    cur_2 = getSellerIDfromUserdetailPage()
    if cur_2:
        cur_seller_id = cur_2
    # print (cur_seller_id)


wishlist.bind('<ButtonRelease-1>', update_current_state)


def update_order_history(*args):
    conn = sqlite3.connect("secondhand.sqlite3")
    cur = conn.cursor()
    orderlist.delete(0, END)
    query = '''SELECT name, developer, condition, price, seller.username, transaction_date FROM device, offer, devicetransaction, buyer, seller 
    WHERE device.id = offer.device_id AND 
    seller.id = offer.seller_id AND
    devicetransaction.device_id = device.id AND 
    buyer.ID = devicetransaction.buyer_id AND 
    buyer.username = ?'''
    # print (current_user)
    username = str(username_var_login.get())
    for row in cur.execute(query, (username,)):
        temp = str(row[0])+ ", "+str(row[1])+ ", "+ str(row[2])+  ", $"+str(row[3])+ ", sold by " + str(row[4])+ ", "+str(row[5])
        # print (temp)
        orderlist.insert(END, temp)

    conn.close()

def update_wishlist(*args):
    conn = sqlite3.connect("secondhand.sqlite3")
    cur = conn.cursor()
    wishlist.delete(0, END)
    tempquery = '''SELECT device.id as device_id, name, developer, condition, price, creation_date FROM wish, buyer, device, offer
    where wish.buyer_id = buyer.id AND
    device.id = offer.device_id AND
    device.id = wish.device_id AND
    buyer.username = ?'''
    username = str(username_var_login.get())
    for row in cur.execute(tempquery,(username,)):
        wishlist.insert(END, row[1:])
    if wishlist.size() != 0:
        wishlist.activate(0)
    conn.close()

def delete_wish_item():
    username = str(username_var_login.get())
    this_DeviceId = getDeviceIDfromUserdetailPage()
    if this_DeviceId:
        backend.deleteWish(this_DeviceId)
        update_wishlist()
    else:
        global previous_page
        previous_page = buyer_main_window

def goto_transaction_window(wherefrom):
    global buyer_id
    global seller_id
    global device_id
    global seller_credit
    global buyer_credit
    global seller_address
    global shipping_address
    global previous_page

    if wherefrom == "buyer_main_window":
        previous_page = buyer_main_window
    elif wherefrom == "buyer_detail_window":
        previous_page = buyer_detail_window
    elif wherefrom == "user_detail_window":
        if wishlist.size() != 0:
            previous_page = user_detail_window
        else:
            # print ("here")
            previous_page = buyer_main_window
            return None
    else:
        pass


    buyer_id = backend.getBuyerIDbyUsername(current_user)
    device_id = cur_device_id
    seller_id = cur_seller_id
    # print (current_user.get())
    # print (buyer_id)
    # print (cur_device_id)
    # print (seller_id)

    device_info = get_device_info(device_id)
    offer_info = get_offer_info(seller_id, device_id)

    transaction_info = find_credit_num(buyer_id, seller_id)
    seller_credit = transaction_info[1]
    buyer_credit = transaction_info[0]
    seller_address = transaction_info[3]
    buyer_address = transaction_info[2]
    # print (buyer_credit)
    # print (seller_credit)
    seller_info = get_seller_info(seller_id)
    credit_card_num.set(buyer_credit)
    shipping_address.set(buyer_address)
    transaction_seller_username.set(seller_info[3])
    transaction_device_name.set(device_info[2])
    transaction_price.set("$" + str(offer_info[4]))

    for i in windows:
        i.withdraw()
    transaction_window.deiconify()


update_order_history()
update_wishlist()

# center(buyer_detail_window)
# center(user_detail_window)
# Buyer_user_detail_page Window end




# Transaction Window

# Tk objects parts
transaction_window = Tk()
windows.append(transaction_window)
transaction_window_width = 500
transaction_window_height = 300
# transaction_window.geometry('{:d}x{:d}+{:d}+{:d}'.format(transaction_window_width, transaction_window_height, int((screen_width - transaction_window_width)/2), int((screen_height - transaction_window_height)/2)))

# Tk objects parts ends


# Tk objects initalization
transaction_window.title("Secondhand Trading Platform -- Transaction")
# Tk objects initalization end

# window display
transaction_window.withdraw()
# window display ends


# frames
frame_transaction = ttk.Frame(transaction_window, padding="3 3 12 12")
frame_transaction.grid(column=0, row=0, sticky=(N, W, E, S))
frame_transaction.columnconfigure(0, weight=1)
frame_transaction.rowconfigure(0, weight=1)

# frames end

def get_buyer_info(buyer_id):
    ret = []
    conn = sqlite3.connect("secondhand.sqlite3")
    cur = conn.cursor()
    # print (buyer_id)
    cur.execute("SELECT * FROM Buyer WHERE id = ?", (int(buyer_id),))

    result = cur.fetchone()
    if result != None:
        ret = result
    conn.commit()
    conn.close()

    return ret

def get_seller_info(seller_id):
    ret = []
    conn = sqlite3.connect("secondhand.sqlite3")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Seller WHERE id = ?", (int(seller_id),))

    result = cur.fetchone()
    if result != None:
        ret = result
    conn.commit()
    conn.close()

    return ret

def get_device_info(device_id):
    # print (device_id)
    ret = []
    conn = sqlite3.connect("secondhand.sqlite3")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Device WHERE id = ?", (int(device_id),))
    # cur.execute("SELECT * FROM Device")
    result = cur.fetchone()
    # print (result)
    if result != None:
        ret = result
    conn.commit()
    conn.close()

    return ret

def get_offer_info(seller_id, device_id):
    ret = []
    conn = sqlite3.connect("secondhand.sqlite3")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Offer WHERE seller_id = ? and device_id = ?", (int(seller_id), int(device_id),))

    result = cur.fetchone()
    # print (result)
    if result != None:
        ret = result
    conn.commit()
    conn.close()

    return ret

def find_credit_num(buyer_id, seller_id):
    conn = sqlite3.connect("secondhand.sqlite3")
    cur = conn.cursor()
    cur.execute("SELECT creditcard, address FROM Buyer WHERE id = ?", (int(buyer_id),))

    result = cur.fetchone()
    num1 = 0
    num2 = 0
    address1 = ""
    address2 = ""
    if result != None:
        num1 = result[0]
        address1 = result[1]
    conn.commit()

    cur.execute("SELECT creditcard, address FROM Seller WHERE id = ?", (int(seller_id),))

    result = cur.fetchone()
    if result != None:
        num2 = result[0]
        address2 = result[1]
    conn.commit()
    conn.close()
    return [num1, num2, address1, address2]

# input variable


# globals
# These data should be passed in from previous screen (buyer_id, seller_id, device_id)
buyer_id = 0
# backend.getBuyerIDbyUsername(current_user)
seller_id = 0
# getSellerIDfromBuyermainPage()
device_id = 0
# getDeviceIDfromBuyermainPage()
seller_credit = ""
date = strftime("%m/%d/%Y", gmtime())
#print (date)





use_curr_card = BooleanVar(transaction_window)
# input variable end

transaction_seller_username = StringVar(transaction_window)
transaction_device_name = StringVar(transaction_window)
transaction_price = StringVar(transaction_window)
transaction_price.set("$")

credit_card_num = StringVar(transaction_window)
shipping_address = StringVar(transaction_window)
# labels
ttk.Label(frame_transaction, font = ('Arial', 14),text="Make Transaction").grid(column=1, row=1, sticky=E)

ttk.Label(frame_transaction, font = ('Arial', 14),text="Buyer: ").grid(column=1, row=2, sticky=E)
transaction_buyer = ttk.Label(frame_transaction,font = ('Arial', 14), text=current_user)
transaction_buyer.grid(column=2, row=2, sticky=E)

ttk.Label(frame_transaction, font = ('Arial', 14),text="Seller: ").grid(column=1, row=3, sticky=E)
ttk.Label(frame_transaction, font = ('Arial', 14),textvariable=transaction_seller_username).grid(column=2, row=3, sticky=E)

ttk.Label(frame_transaction,font = ('Arial', 14), text="Device: ").grid(column=1, row=4, sticky=E)
ttk.Label(frame_transaction,font = ('Arial', 14), textvariable=transaction_device_name).grid(column=2, row=4, sticky=E)

ttk.Label(frame_transaction,font = ('Arial', 14), text="Price: ").grid(column=1, row=5, sticky=E)
ttk.Label(frame_transaction,font = ('Arial', 14), textvariable=transaction_price).grid(column=2, row=5, sticky=E)

ttk.Label(frame_transaction,font = ('Arial', 14), text="Credit Card Number: ").grid(column=1, row=6, sticky=E)
credit_input = ttk.Entry(frame_transaction, width=20, font = ('Arial', 14),textvariable=credit_card_num)
credit_input.grid(column=2, row=6, sticky=W)

ttk.Label(frame_transaction,font = ('Arial', 14), text="Shipping Address: ").grid(column=1, row=7, sticky=E)
shipping_address_input = ttk.Entry(frame_transaction, width=40, font = ('Arial', 14),textvariable=shipping_address)
shipping_address_input.grid(column=2, row=7, sticky=W)
credit_input.focus()

# labels end

# Some queries in case entries don't exist
#backend.createDevice()
#backend.insertDevice("Apple", "iPhone 5c", "5c", "2015", "Good")
#backend.createDeviceTransaction()
#backend.createOffer()
#backend.insertOffer(device_id, seller_id, "Pending", date, 149.99)

# functions

def update_address():
    #print(buyer_id)

    # Update address if user saves it
    try:
        address = shipping_address.get()

        conn = sqlite3.connect("secondhand.sqlite3")
        cur = conn.cursor()
        cur.execute("UPDATE Buyer set address = ? WHERE id = ?", (address, buyer_id,))

        popupWindow = Toplevel(signup_window)
        popupWindow.title('Info')
        Label(popupWindow, font = ('Arial',13), text="Shipping address is saved successfully!").grid(column=0, row=0, sticky=(E,W,N,S),padx = 30, pady = 30)
        Button(popupWindow,text = "OK", font = ('Arial',13),command = lambda: popupWindow.destroy()).grid(row=1,column=0,padx = 30, pady = 20)


        conn.commit()
        conn.close()


    except ValueError:
        pass

def submit_transaction(*args):
    #print(buyer_id)
    update_credit_num()
    credit_num = credit_card_num.get()
    is_number = True
    try:
        int(credit_num)
    except ValueError:
        is_number = False
    if credit_num == "" or not is_number:
        popupWindow = Toplevel(signup_window)
        popupWindow.title('Info')

        Label(popupWindow, font = ('Arial',13), text="Credit card number must be valid!").grid(column=0, row=0, sticky=(E,W,N,S),padx = 30, pady = 30)
        Button(popupWindow,text = "OK", font = ('Arial',13),command = lambda: popupWindow.destroy()).grid(row=1,column=0,padx = 30, pady = 20)

        return None
    #print (buyer_id)
    global date
    date = strftime("%m/%d/%Y", gmtime())
    backend.insertDeviceTransaction(buyer_id, seller_id, seller_credit, credit_num, device_id, date)
    change_offer_status()
    delete_wish_list_if_has()
    print("Transaction successfully made")
    update_order_history()
    update_result()
    for i in windows:
        i.withdraw()
    buyer_main_window.deiconify()

def update_credit_num():

    # Update credit card number if user changes it
    try:
        credit_num = credit_card_num.get()

        conn = sqlite3.connect("secondhand.sqlite3")
        cur = conn.cursor()
        cur.execute("UPDATE Buyer set creditcard = ? WHERE id = ?", (credit_num, buyer_id,))

        conn.commit()
        conn.close()


    except ValueError:
        pass

def delete_wish_list_if_has():
    conn = sqlite3.connect("secondhand.sqlite3")
    cur = conn.cursor()
    wishlist.delete(0, END)
    query = '''SELECT * FROM wish
    where device_id = ?'''
    cur.execute(query, (device_id,))
    result = cur.fetchone()
    conn.close()
    # print (result)
    if result:
        backend.deleteWish(device_id)
        update_wishlist()


def change_offer_status():

    #Updates offer status from "Pending" to "Sold"
    conn = sqlite3.connect("secondhand.sqlite3")
    cur = conn.cursor()
    cur.execute("UPDATE Offer set status = ? WHERE device_id = ? and seller_id = ?", ("Sold", device_id, seller_id,))

    conn.commit()
    conn.close()

# functions end

# buttons
Button(frame_transaction, font = ('Arial', 14),text="Save Address", command=update_address).grid(column=3, row=7, sticky=W)
Button(frame_transaction, font = ('Arial', 14),text="Make Transaction", command=submit_transaction).grid(column=3, row=8, sticky=W)
Button(frame_transaction, font = ('Arial', 14),text="Back", command=lambda :onClickBack()).grid(column=1, row=8, sticky=W)

# buttons end

# Seller_main Window end


for child in frame_transaction.winfo_children(): child.grid_configure(padx=5, pady=5)

credit_input.focus()
transaction_window.bind('<Return>', submit_transaction)


#center(transaction_window)
# Transaction Window End








# Seller parts


# Windows
seller_main_window = Tk()
windows.append(seller_main_window)
seller_main_window.withdraw()
seller_main_window.title("Secondhand Trading Platform -- Seller")

seller_post_window = Tk()
windows.append(seller_post_window)
seller_post_window.withdraw()
seller_post_window.title("Secondhand Trading Platform -- New post")



seller_moreinfo_Window=Tk()
windows.append(seller_moreinfo_Window)
seller_moreinfo_Window.withdraw()
seller_moreinfo_Window.title("Secondhand Trading Platform -- More Info")



edit_device_window=Tk()
edit_device_window.withdraw()
windows.append(edit_device_window)
edit_device_window.title("Secondhand Trading Platform -- Edit Device")
# Windows end

# Frames

#frame display device offer
seller_main_frame = Frame(seller_main_window)
seller_main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
# Frames end


# Seller main windwo top row username
Label(seller_main_frame, font = ('Arial', 14), text = "Welcome! ").grid(row = 0, column=7, sticky = E, padx = 10, pady = 10)
seller_main_user = Label(seller_main_frame, font=('Arial', 14), relief = FLAT, text = current_user )
seller_main_user.grid(row = 0, column=8, sticky = W, padx = 5, pady = 10)


Button(seller_main_frame,font=('Arial', 14),text = "Log out", command = lambda :log_out()).grid( row = 0, column = 9,stick = E, padx = 10, pady = 10)

# top label
ttk.Label(seller_main_frame, font = ('Arial', 14),text="---Manage Your Post---").grid(row=1,column=2, columnspan = 6)

Button(seller_main_frame, font = ('Arial', 12),text = "New post", command = lambda :goto_post_offer()).grid( row = 1, column = 0,stick = W, padx = 10, pady = 10)

Button(seller_main_frame, text = "Exit", font = ('Arial',14),command = onExit).grid(row=1,column=9, stick = E, padx = 10, pady = 10)


# column names of offered device
Label(seller_main_frame, font = ('Arial', 12, 'bold'), text = "Name").grid(row = 2, column=0, sticky = (N, W, E, S), padx = 10, pady = 10)
Label(seller_main_frame, font = ('Arial', 12, 'bold'), text = "Developer").grid(row = 2, column=1, sticky = (N, W, E, S), padx = 10, pady = 10)
Label(seller_main_frame, font = ('Arial', 12, 'bold'), text = "Model").grid(row = 2, column=2, sticky = (N, W, E, S), padx = 10, pady = 10)
Label(seller_main_frame, font = ('Arial', 12, 'bold'), text = "Condition").grid(row = 2, column=3, sticky = (N, W, E, S), padx = 10, pady = 10)
Label(seller_main_frame, font = ('Arial', 12, 'bold'), text = "Price").grid(row = 2, column=4, sticky = (N, W, E, S), padx = 10, pady = 10)
Label(seller_main_frame, font = ('Arial', 12, 'bold'), text = "Offer Date").grid(row = 2, column=5, sticky = (N, W, E, S), padx = 10, pady = 10)
Label(seller_main_frame, font = ('Arial', 12, 'bold'), text = "Status").grid(row = 2, column=6, sticky = (N, W, E, S), padx = 10, pady = 10)
Label(seller_main_frame, font = ('Arial', 12, 'bold'), text = "Operations").grid(row = 2, column=7,  columnspan=3, sticky = (N, W, E, S), padx = 10, pady = 10)



edit_device_id=None





def goto_post_offer():
    name_var.set("")
    developer_var.set("")
    model_var.set("")
    year_var.set("")
    condition_var.set("Good")
    price_var.set("0.0")
    global previous_page
    previous_page = seller_main_window
    for i in windows:
        i.withdraw()
    seller_post_window.deiconify()

def postDevice(*args):
    try:
        seller_id=backend.getSellerIDbyUsername(current_user)
        developer=developer_var.get()
        name=name_var.get()
        model=model_var.get()
        year=year_var.get()
        condition=condition_var.get()
        status="Pending"
        global date
        date = strftime("%m/%d/%Y", gmtime())
        date_this=date
        price=price_var.get()
        if price == "" or float(price)<=0.0 or developer == "" or name == "" or model == "" or year == "":
            incorrectPrice=Toplevel(seller_post_window)
            incorrectPrice.title("Info")
            Label(incorrectPrice, font = ('Arial',14), text="Invalid Fields!").grid(column=0, row=0, sticky=(E,W,N,S),padx = 30, pady = 30)
            Button(incorrectPrice,text = "OK", font = ('Arial',14),command = lambda :incorrectPrice.destroy()).grid(row=1,column=0,padx = 30, pady = 20)
            return None
        #print("hello")
        # print(price)
        try:
            backend.insertDevice(developer,name,model,year,condition)
        except:
            backend.createDevice()
            print("error insert to Device")
        #device_id=selectAllDevicesFromOffer()[0][0]
        device_id=backend.selectDeviceIdByOther(developer,name,model,year,condition)
        # print(device_id)
        try:
            backend.insertOffer(device_id,seller_id,status,date_this,price)
            # print(device_id)
            # print(seller_id)
            # print(status)
            # print(date)
            # print(price)
        except:
            print ("error insert to Offer")
            pass
        afterPost=Toplevel(seller_post_window)
        afterPost.title("Info")
        Label(afterPost, font = ('Arial',14), text="Post Successful!").grid(column=0, row=0, sticky=(E,W,N,S),padx = 30, pady = 30)
        Button(afterPost,text = "OK", font = ('Arial',14),command = lambda s=afterPost: gobackafterpost(s)).grid(row=1,column=0,padx = 30, pady = 20)
        seller_post_window.withdraw()
    except ValueError:
        print("Value Error!")


def gobackafterpost(s):
    s.destroy()
    update_offered_device()
    seller_main_window.deiconify()


def selectAllDevicesFromOffer():
    conn=sqlite3.connect("secondhand.sqlite3")
    seller_id=backend.getSellerIDbyUsername(current_user)
    # print(current_user)
    # print(seller_id)
    cur=conn.cursor()
    cur.execute("""SELECT * FROM Device join offer where device.id = offer.device_id AND 
    NOT offer.status = ? AND 
    offer.seller_id = ?;""",("Sold",seller_id))
    result = cur.fetchall()
    return result

def selectSoldDevicesFromOffer():
    conn=sqlite3.connect("secondhand.sqlite3")
    seller_id=backend.getSellerIDbyUsername(current_user)
    # print(current_user)
    # print(seller_id)
    cur=conn.cursor()
    cur.execute("""SELECT * FROM Device join offer where device.id = offer.device_id AND 
    offer.status = ? AND 
    offer.seller_id = ?;""",("Sold",seller_id))
    result = cur.fetchall()
    return result

# Seller Window


# Tk objects parts
# Tk objects parts ends

# Tk objects initalization

# Tk objects initalization end

# window display
#seller_main_window.withdraw()
# window display ends


# frames
seller_post_frame = ttk.Frame(seller_post_window, padding="3 3 12 12")
seller_post_frame.grid(column=0, row=0, sticky=(N, W, E, S))
seller_post_frame.columnconfigure(0, weight=1)
seller_post_frame.rowconfigure(0, weight=1)
for child in seller_post_frame.winfo_children(): child.grid_configure(padx=5, pady=5)

# frames end

# input variable
name_var = StringVar(seller_post_frame)
developer_var = StringVar(seller_post_frame)
model_var = StringVar(seller_post_frame)
year_var = StringVar(seller_post_frame)
condition_var = StringVar(seller_post_frame)
price_var = DoubleVar(seller_post_frame)


# input variable end

# labesl

ttk.Label(seller_post_frame, font = ('Arial', 14),text="Name: ").grid(column=1, row=2, sticky = (N, W, E, S), padx = 10, pady = 10)
name_input = ttk.Entry(seller_post_frame, width=30, textvariable=name_var)
name_input.grid(column=2, row=2, sticky=W)
name_input.focus()

ttk.Label(seller_post_frame,font = ('Arial', 14), text="Developer: ").grid(column=1, row=3, sticky = (N, W, E, S), padx = 10, pady = 10)
developer_input = ttk.Entry(seller_post_frame, width=30, textvariable=developer_var)
developer_input.grid(column=2, row=3, sticky=W)


ttk.Label(seller_post_frame, font = ('Arial', 14),text="Model: ").grid(column=1, row=4, sticky = (N, W, E, S), padx = 10, pady = 10)
model_input = ttk.Entry(seller_post_frame, width=30, textvariable=model_var)
model_input.grid(column=2, row=4, sticky=W)

ttk.Label(seller_post_frame,font = ('Arial', 14), text="Year: ").grid(column=1, row=5, sticky = (N, W, E, S), padx = 10, pady = 10)
year_input = ttk.Entry(seller_post_frame, width=30, textvariable=year_var)
year_input.grid(column=2, row=5, sticky=W)


condition_var.set('Good')
Condtionchoices = {'Flawless', 'Good', 'Acceptable', 'Fair', 'Poor'}
  # set the default option

popupMenu = OptionMenu(seller_post_frame, condition_var, *Condtionchoices)
ttk.Label(seller_post_frame, font = ('Arial', 14),text="Condition: ").grid(column=1, row=6, sticky = (N, W, E, S), padx = 10, pady = 10)
popupMenu.grid(column=2, row=6, sticky=W)



ttk.Label(seller_post_frame, font = ('Arial', 14),text="Price: ").grid(column=1, row=7, sticky = (N, W, E, S), padx = 10, pady = 10)
price_input = ttk.Entry(seller_post_frame, width=30, textvariable=price_var)
price_input.grid(column=2, row=7, sticky=W)


Button(seller_post_frame,  font = ('Arial', 14),text="Post this Device", command=lambda:postDevice()).grid(column=3, row=8, sticky=E, padx = 10, pady = 10)
Button(seller_post_frame,  font = ('Arial', 14), text="Back", command=lambda:onClickBack()).grid(column=1, row=8, sticky=W, padx = 10, pady = 10)

# https://pythonspot.com/en/tk-dropdown-example/
# choices = {'Seller', 'Buyer'}
# user_type_var.set('Seller')  # set the default option

# popupMenu = OptionMenu(seller_post_frame, user_type_var, *choices)
# ttk.Label(seller_post_frame, text="User Type: ").grid(column=1, row=10, sticky=E)
# popupMenu.grid(column=2, row=10)




def selectDeviceById(thisid):
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute('''select * from Device, offer, devicetransaction, buyer 
    where Device.id = offer.device_id AND 
    Device.id = devicetransaction.device_id AND 
    buyer.id = devicetransaction.buyer_id AND
    Device.id=?;''',(thisid,))
    result=cur.fetchone()
    # print ("transaction result:")
    # print (result)
    if not result:
        cur.execute("select * from Device, offer where Device.id = offer.device_id AND Device.id=?;",(thisid,))
        result=cur.fetchone()
    conn.commit()
    conn.close()
    # print (result)
    return result





# detail_ID2 = StringVar(seller_moreinfo_Window)
detail_Name2 = StringVar(seller_moreinfo_Window)
detail_Developer2 = StringVar(seller_moreinfo_Window)
detail_Model2 = StringVar(seller_moreinfo_Window)
detail_Year2 = StringVar(seller_moreinfo_Window)
detail_Condition2 = StringVar(seller_moreinfo_Window)
detail_Price2 = StringVar(seller_moreinfo_Window)
detail_OfferDate2 = StringVar(seller_moreinfo_Window)
detail_Status2 = StringVar(seller_moreinfo_Window)
detail_Buyer2 = StringVar(seller_moreinfo_Window)
detail_TransDate2 = StringVar(seller_moreinfo_Window)


more_info_frame = Frame(seller_moreinfo_Window)
more_info_frame.grid(row = 0,column = 0)

Label(more_info_frame, font = ('Arial', 14), text = "Device Name: ").grid(row = 2, column  = 0, sticky = W, padx = 30, pady = 5)
Label(more_info_frame, font = ('Arial', 14), text = "Device Developer: ").grid(row = 3, column  = 0, sticky = W, padx = 30, pady = 5)
Label(more_info_frame, font = ('Arial', 14), text = "Device Model: ").grid(row = 4, column  = 0, sticky = W, padx = 30, pady = 5)
Label(more_info_frame, font = ('Arial', 14), text = "Device Year: ").grid(row = 5, column  = 0, sticky = W, padx = 30, pady = 5)
Label(more_info_frame, font = ('Arial', 14), text = "Device Condition: ").grid(row = 6, column  = 0, sticky = W, padx = 30, pady = 5)
Label(more_info_frame, font = ('Arial', 14), text = "Price: ").grid(row = 7, column  = 0, sticky = W, padx = 30, pady = 5)
Label(more_info_frame, font = ('Arial', 14), text = "Offer Date: ").grid(row = 8, column  = 0, sticky = W, padx = 30, pady = 5)
Label(more_info_frame, font = ('Arial', 14), text = "Status: ").grid(row = 9, column  = 0, sticky = W, padx = 30, pady = 5)
Label(more_info_frame, font = ('Arial', 14), text = "Bought by: ").grid(row = 10, column  = 0, sticky = W, padx = 30, pady = 5)
Label(more_info_frame, font = ('Arial', 14), text = "Transaction Date: ").grid(row = 11, column  = 0, sticky = W, padx = 30, pady = 5)


label2=Label(more_info_frame, font = ('Arial', 14), textvariable = detail_Name2)
label2.grid(row = 2, column  = 1, sticky = E, padx = 30, pady = 5)
label3=Label(more_info_frame, font = ('Arial', 14), textvariable = detail_Developer2)
label3.grid(row = 3, column  = 1, sticky = E, padx = 30, pady = 5)
label4=Label(more_info_frame, font = ('Arial', 14), textvariable = detail_Model2)
label4.grid(row = 4, column  = 1, sticky = E, padx = 30, pady = 5)
label5=Label(more_info_frame, font = ('Arial', 14), textvariable = detail_Year2)
label5.grid(row = 5, column  = 1, sticky = E, padx = 30, pady = 5)
label6=Label(more_info_frame, font = ('Arial', 14), textvariable = detail_Condition2)
label6.grid(row = 6, column  = 1, sticky = E, padx = 30, pady = 5)
label7=Label(more_info_frame, font = ('Arial', 14), textvariable = detail_Price2)
label7.grid(row = 7, column  = 1, sticky = E, padx = 30, pady = 5)
label8=Label(more_info_frame, font = ('Arial', 14), textvariable = detail_OfferDate2)
label8.grid(row = 8, column  = 1, sticky = E, padx = 30, pady = 5)
label8=Label(more_info_frame, font = ('Arial', 14), textvariable = detail_Status2)
label8.grid(row = 9, column  = 1, sticky = E, padx = 30, pady = 5)
label8=Label(more_info_frame, font = ('Arial', 14), textvariable = detail_Buyer2)
label8.grid(row = 10, column  = 1, sticky = E, padx =30, pady = 5)
label8=Label(more_info_frame, font = ('Arial', 14), textvariable = detail_TransDate2)
label8.grid(row = 11, column  = 1, sticky = E, padx = 30, pady = 5)

Button(more_info_frame, text = "Go Back", font = ('Arial',14),command = lambda: goback()).grid(column = 1, row = 13, sticky = E,padx = 10, pady = 10)

labels_display=[]

def update_offered_device():
    global labels_display
    for i in labels_display:
        i.destroy()
    devices=selectAllDevicesFromOffer()
    i=3

    s = ttk.Style()
    s.configure('my.TButton', font=('Arial', 10))


    for device in devices:
        # print(device)
        label1=ttk.Label(seller_main_frame, text=device[2])
        label1.grid(row=i,column=0)
        label2=ttk.Label(seller_main_frame, text=device[1])
        label2.grid(row=i,column=1)
        label3=ttk.Label(seller_main_frame, text=device[3])
        label3.grid(row=i,column=2)
        label4=ttk.Label(seller_main_frame, text=device[5])
        label4.grid(row=i,column=3)
        label5=ttk.Label(seller_main_frame, text=device[10])
        label5.grid(row=i,column=4)
        label6=ttk.Label(seller_main_frame, text=device[9])
        label6.grid(row=i,column=5)
        label7=ttk.Label(seller_main_frame, text=device[8])
        label7.grid(row=i,column=6)
        button2=ttk.Button(seller_main_frame, style = 'my.TButton', text="Edit", command = lambda s=device[0] :edit_selling_device(s))
        button2.grid(row=i,column=7)
        button1=ttk.Button(seller_main_frame, style = 'my.TButton', text="More Info", command = lambda s = device[0]: moreinfo_selling_device(s))
        button1.grid(row=i,column=8)
        button3=ttk.Button(seller_main_frame, style = 'my.TButton', text="Delete",command= lambda s=device[0]: delete_selling_device(s))
        button3.grid(row=i,column=9)
        i=i+1
        labels_display.append(label1)
        labels_display.append(label2)
        labels_display.append(label3)
        labels_display.append(label4)
        labels_display.append(label5)
        labels_display.append(label6)
        labels_display.append(label7)
        labels_display.append(button1)
        labels_display.append(button2)
        labels_display.append(button3)

    emptylabel = ttk.Label(seller_main_frame, font = ('Arial', 14),text="")
    emptylabel.grid(row=i,column=2, rowspan = 2)
    labels_display.append(emptylabel)
    i+=2


    solddevicelabel = ttk.Label(seller_main_frame, font = ('Arial', 14),text="---Sold Devices---")
    solddevicelabel.grid(row=i,column=2, columnspan = 6)
    labels_display.append(solddevicelabel)
    i+=1

    emptylabel2 = ttk.Label(seller_main_frame, font = ('Arial', 14),text="")
    emptylabel2.grid(row=i,column=2, rowspan = 2)
    labels_display.append(emptylabel2)
    i+=2
    devices=selectSoldDevicesFromOffer()
    for device in devices:
        # print(device)
        label1=ttk.Label(seller_main_frame, text=device[2])
        label1.grid(row=i,column=0)
        label2=ttk.Label(seller_main_frame, text=device[1])
        label2.grid(row=i,column=1)
        label3=ttk.Label(seller_main_frame, text=device[3])
        label3.grid(row=i,column=2)
        label4=ttk.Label(seller_main_frame, text=device[5])
        label4.grid(row=i,column=3)
        label5=ttk.Label(seller_main_frame, text=device[10])
        label5.grid(row=i,column=4)
        label6=ttk.Label(seller_main_frame, text=device[9])
        label6.grid(row=i,column=5)
        label7=ttk.Label(seller_main_frame, text=device[8])
        label7.grid(row=i,column=6)
        button1=ttk.Button(seller_main_frame, style = 'my.TButton', text="More Info", command = lambda s = device[0]: moreinfo_selling_device(s))
        button1.grid(row=i,column=8)
        i=i+1
        labels_display.append(label1)
        labels_display.append(label2)
        labels_display.append(label3)
        labels_display.append(label4)
        labels_display.append(label5)
        labels_display.append(label6)
        labels_display.append(label7)
        labels_display.append(button1)

def goback():
    update_offered_device()
    for i in windows:
        i.withdraw()
    seller_main_window.deiconify()



def updateMoreInfoPage(thisid):
    result=selectDeviceById(thisid)
    # print ("final result:")
    # print (result)
    # detail_ID2.set(result[0])
    #print(detail_ID2.get())
    #print(detail_Model2.get())
    detail_Name2.set(result[2])
    detail_Developer2.set(result[1])
    detail_Model2.set(result[3])
    detail_Year2.set(result[4])
    detail_Condition2.set(result[5])

    detail_Price2.set("$"+str(result[10]))
    detail_OfferDate2.set(result[9])
    detail_Status2.set(result[8])
    detail_Buyer2.set("None")
    detail_TransDate2.set("None")
    # print (len(result))
    if len(result) > 11:
        detail_Buyer2.set(result[20])
        detail_TransDate2.set(result[16])

def moreinfo_selling_device(x):
    updateMoreInfoPage(x)
    for i in windows:
        i.withdraw()
    seller_moreinfo_Window.deiconify()

    #print(result)




edit_device_frame=Frame(edit_device_window)
developer_var2 = StringVar(edit_device_frame)
name_var2 = StringVar(edit_device_frame)
model_var2 = StringVar(edit_device_frame)
year_var2 = StringVar(edit_device_frame)
condition_var2 = StringVar(edit_device_frame)
status_var2=StringVar(edit_device_frame)
price_var2=DoubleVar(edit_device_frame)
edit_device_frame.grid(row=0,column=0)

ttk.Label(edit_device_frame, font = ('Arial', 14), text="Name: ").grid(column=0, row=0, sticky=E, padx = 10, pady = 10)
name_input = ttk.Entry(edit_device_frame, width=30, textvariable=name_var2)
name_input.grid(column=1, row=0, sticky=W, padx = 10, pady = 10)
name_input.focus()

Label(edit_device_frame, font = ('Arial', 14), text="Developer: ").grid(column=0, row=1, sticky=E, padx = 10, pady = 10)
developer_input = ttk.Entry(edit_device_frame, width=30, textvariable=developer_var2)
developer_input.grid(column=1, row=1, sticky=W, padx = 10, pady = 10)


ttk.Label(edit_device_frame,  font = ('Arial', 14),text="Model: ").grid(column=0, row=2, sticky=E, padx = 10, pady = 10)
model_input = ttk.Entry(edit_device_frame, width=30, textvariable=model_var2)
model_input.grid(column=1, row=2, sticky=W, padx = 10, pady = 10)

ttk.Label(edit_device_frame,  font = ('Arial', 14),text="Year: ").grid(column=0, row=3, sticky=E, padx = 10, pady = 10)
year_input = ttk.Entry(edit_device_frame, width=30, textvariable=year_var2)
year_input.grid(column=1, row=3, sticky=W, padx = 10, pady = 10)

popupMenu = OptionMenu(edit_device_frame, condition_var2, *Condtionchoices)
ttk.Label(edit_device_frame, font = ('Arial', 14),text="Condition: ").grid(column=0, row=4, sticky = E, padx = 10, pady = 10)
popupMenu.grid(column=1, row=4, sticky=W, padx = 10, pady = 10)

ttk.Label(edit_device_frame,  font = ('Arial', 14),text="Price: ").grid(column=0, row=5, sticky=E, padx = 10, pady = 10)
price_input = ttk.Entry(edit_device_frame, width=30, textvariable=price_var2)
price_input.grid(column=1, row=5, sticky=W, padx = 10, pady = 10)


Button(edit_device_frame, font = ('Arial', 14),text="Submit Changes", command=lambda: update_edit_device()).grid(column=2, row=8, sticky=E, padx = 10, pady = 10)
Button(edit_device_frame, font = ('Arial', 14),text="Back", command=lambda:goback()).grid(column=0, row=8, sticky=W, padx = 10, pady = 10)

def edit_selling_device(this_id):
    result = selectDeviceById(this_id)
    # print (result[8])
    if result[8] == 'Sold':
        print ("Device sold, cannot be edited")
        return None
    for i in windows:
        i.withdraw()
    edit_device_window.deiconify()
    global edit_device_id
    edit_device_id=this_id
    name_var2.set(result[2])
    developer_var2.set(result[1])
    model_var2.set(result[3])
    year_var2.set(result[4])
    condition_var2.set(result[5])
    price_var2.set(result[10])

def update_edit_device():
    price = price_input.get()
    name = name_input.get()
    dev = developer_input.get()
    mod = model_input.get()
    yr = year_input.get()
    if price == "" or float(price)<=0.0 or name == "" or dev == "" or mod == "" or yr == "":
        incorrectPrice=Toplevel(edit_device_window)
        incorrectPrice.title("Info")
        Label(incorrectPrice, font = ('Arial',14), text="Invalid Fields!").grid(column=0, row=0, sticky=(E,W,N,S),padx = 30, pady = 30)
        Button(incorrectPrice,text = "OK", font = ('Arial',14),command = lambda :incorrectPrice.destroy()).grid(row=1,column=0,padx = 30, pady = 20)
        return None
    backend.updateDevice(edit_device_id,developer_input.get(),name_input.get(),model_input.get(),year_input.get(),condition_var2.get())
    backend.updateOffer(edit_device_id,price_input.get())
    #print(edit_device_id)
    #print(selectDeviceById(edit_device_id))

    afterChange=Toplevel(edit_device_window)
    afterChange.title("Info")
    Label(afterChange, font = ('Arial',14), text="Update Successful!").grid(column=0, row=0, sticky=(E,W,N,S),padx = 30, pady = 30)
    Button(afterChange,text = "OK", font = ('Arial',14),command = lambda s=afterChange: gobackafterupdate(s)).grid(row=1,column=0,padx = 30, pady = 20)
    edit_device_window.withdraw()


def gobackafterupdate(s):
    s.destroy()
    update_offered_device()
    seller_main_window.deiconify()


def delete_selling_device(this_id):
    result = selectDeviceById(this_id)
    # print (result[8])
    if result[8] == 'Sold':
        print ("Device sold, cannot be deleted")
        return None
    backend.deleteDevice(this_id)
    backend.deleteOffer(this_id)
    afterDelete=Toplevel(seller_main_window)
    afterDelete.title("Info")
    Label(afterDelete, font = ('Arial',14), text="Delete Successful!").grid(column=0, row=0, sticky=(E,W,N,S),padx = 30, pady = 30)
    Button(afterDelete,text = "OK", font = ('Arial',14),command = lambda s=afterDelete: gobackafterdelete(s)).grid(row=1,column=0,padx = 30, pady = 20)


    # for i in windows:
    #     i.withdraw()
    # seller_main_window.deiconify()

def gobackafterdelete(s):
    s.destroy()
    update_offered_device()
    seller_main_window.update_idletasks()




# go back function
def onClickBack():
    global previous_page
    for i in windows:
        i.withdraw()
    previous_page.deiconify()
    if previous_page == buyer_detail_window:
        previous_page = buyer_main_window
    elif previous_page == user_detail_window:
        previous_page = buyer_main_window
    else:
        pass



# mainloop starts

welcome_window.mainloop()
















