from tkinter import *
def get_selected_row(event):
    pass

def view_command():
    pass

def search_command():
    pass

def add_command():
    pass

def delete_command():
    pass

def update_command():
    pass

window=Tk()
window.configure(background="dodger blue")
window.wm_title("Secondhand Trading Platform")

l1=Label(window,text="Product Name",bg="dodger blue")
l1.grid(row=0,column=0)

l2=Label(window,text="Price",bg="dodger blue")
l2.grid(row=0,column=2)

l3=Label(window,text="Year",bg="dodger blue")
l3.grid(row=0,column=4)

l4=Label(window,text="Seller Name",bg="dodger blue")
l4.grid(row=1,column=0)

l5=Label(window,text="Phone",bg="dodger blue")
l5.grid(row=1,column=2)

l6=Label(window,text="Email",bg="dodger blue")
l6.grid(row=1,column=4)

l7=Label(window,text="Address",bg="dodger blue")
l7.grid(row=1,column=6)


product_text=StringVar()
e1=Entry(window,textvariable=product_text)
e1.grid(row=0,column=1)

price_value=DoubleVar()
e2=Entry(window,textvariable=price_value)
e2.grid(row=0,column=3)

year_value=IntVar()
e3=Entry(window,textvariable=year_value)
e3.grid(row=0,column=5)

name_text=StringVar()
e4=Entry(window,textvariable=name_text)
e4.grid(row=1,column=1)

phone_text=StringVar()
e5=Entry(window,textvariable=phone_text)
e5.grid(row=1,column=3)

email_text=StringVar()
e6=Entry(window,textvariable=email_text)
e6.grid(row=1,column=5)

address_text=StringVar()
e7=Entry(window,textvariable=address_text)
e7.grid(row=1,column=7)

""" Commands Below"""
boxlabel=Label(window,text="Search Results:",fg="red",font = "Helvetica 16 bold italic")
boxlabel.grid(row=2,column=0)
list1=Listbox(window, height=6,width=35)
list1.grid(row=3,column=1,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

#buttons=Frame(window)
#buttons.grid(row=3,column=3)
b1=Button(window,text="View all Products", width=12,command=view_command)
b1.grid(row=2,column=3)
#b1.pack(fill="x")
b2=Button(window,text="Search Product", width=12,command=search_command, bg="goldenrod1")
b2.grid(row=3,column=3)
#b2.pack(fill="x")
b3=Button(window,text="Add Product", width=12,command=add_command, bg="lime green")
b3.grid(row=4,column=3)
#b3.pack(fill="x")
b4=Button(window,text="Update selected", width=12,command=update_command,bg="purple")
b4.grid(row=5,column=3)
#b4.pack(fill="x")
b5=Button(window,text="Delete selected", width=12,command=delete_command,bg="yellow")
b5.grid(row=6,column=3)
#b5.pack(fill="x")
b6=Button(window,text="Exit", width=12,command=window.destroy, bg="gray24")
b6.grid(row=7,column=3)
#b6.pack(fill="x")
window.mainloop()