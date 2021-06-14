from tkinter import *
from contacts import *

def which_selected():                                               # The 3 main functions that power the program.
    print("At {0}".format(select.curselection()))
    return int(select.curselection()[0])

def add_entry():
    phonelist.append([fname.get(), lname.get(), phonevar.get()])
    contact_display()

def delete_entry():
    del phonelist[which_selected()]
    contact_display()

def main_window():
    global fname, lname, phonevar, select                               #global variables
    win = Tk()

    frame1 = Frame(win)
    frame1.pack()

    Label(frame1, text="First Name").grid(row=0, column=0, sticky=W)
    fname = StringVar()
    fname = Entry(frame1, textvariable=fname)
    fname.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Last Name").grid(row=1, column=0, sticky=W)
    lname = StringVar()
    lname = Entry(frame1, textvariable=lname)
    lname.grid(row=1, column=1, sticky=W)

    Label(frame1, text="Phone").grid(row=2, column=0, sticky=W)
    phonevar = StringVar()
    phone = Entry(frame1, textvariable=phonevar)
    phone.grid(row=2, column=1, sticky=W)

    frame2 = Frame(win)                                 # Clickable buttons
    frame2.pack()
    b1 = Button(frame2, text = "Add", command=add_entry)
    b2 = Button(frame2, text = "Delete", command=delete_entry)
    b1.pack(side=LEFT)
    b2.pack(side=LEFT)

    frame3 = Frame(win)                              # list of names
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
    scroll.config(command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT, fill=BOTH, expand=1)
    return win


def contact_display():
    phonelist.sort(key=lambda record: record[1])
    select.delete(0, END)
    for fname, lname, phone in phonelist:                                       # Simple loop that display relevant information in GUI.
        select.insert(END, "{0}, {1}, {2}".format(lname, fname, phone))



win = main_window()
contact_display()
win.mainloop()