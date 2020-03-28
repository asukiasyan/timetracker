#!/usr/local/bin/python
import random
import string
import sys
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import backend_functions
from getpass import getpass
import time

# ============== Global Variables ==================

backgroundColor = '#1E2434'# '#222936'
labelTextColor = '#273244' # '#9ABCB7'
textColor = '#7F8798' #'#4E5C75'



# ================== Functions =======================

def clear():
    task.delete(0,END)
    start.delete(0,END)
    end.delete(0,END)
    note.delete(0,END)

def addData():
    if(len(task.get()) !=0):
        backend_functions.add_entry(start.get(), end.get(), task.get(), note.get())
        listbox.delete(0,END)
        listbox.insert(END, (start.get(), end.get(), task.get(), note.get()))
    clear()
    viewAllData()

def record(event):
    global sd
    searchEntry = listbox.curselection()[0]
    sd = listbox.get(searchEntry)

    task.delete(0,END)
    task.insert(END,sd[1])
    start.delete(0,END)
    start.insert(END,sd[2])
    end.delete(0,END)
    end.insert(END,sd[3])
    note.delete(0,END)
    note.insert(END,sd[4])

def deleteData():
    if(len(task.get()) !=0):
        backend_functions.delete_entry(sd[0])
        clear()
        viewAllData()

def searchData():
    listbox.delete(0,END)
    for row in backend_functions.search_entry(task.get(), start.get(), end.get(), note.get()):
        listbox.insert(END,row,str(""))

def updateData():
    if(len(task.get()) !=0):
        backend_functions.delete_entry(sd[0])
        backend_functions.add_entry(task.get(), start.get(), end.get(), note.get())
        listbox.delete(0,END)
        listbox.insert(END, (task.get(), start.get(), end.get(), note.get()))


def viewAllData():
    listbox.delete(0,END)
    for row in backend_functions.show_all():
        listbox.insert(END,row,str(""))

def exportData():
    backend_functions.export_all()

def closeWindow():
        quit = messagebox.askyesno ("Time Tracker", "Are you sure you want to quit?")
        if quit > 0:
            backend_functions.export_all()
            window.destroy()
        return


# ===================== FrontEnd / Window Configuration =====================



window = Tk()
window.geometry("800x400")
window.title("TimeTracker")
window.config(bg=backgroundColor)
window.resizable(False, False)
window.protocol('WM_DELETE_WINDOW', closeWindow)

task = StringVar()
start = StringVar()
end = StringVar()
note = StringVar()
checkboxValue = BooleanVar()
scalerValue = StringVar()



label_appname = Label(window, text="Easy Time Tracker", font=("Times", 20), fg=textColor, bg=backgroundColor).place(relx=0.6, rely=0.15, anchor='se')
Time = time.strftime("%a: %d/%m/%Y")
Time = Label(window, text=Time, font=("Times", 20), fg=textColor, bg=backgroundColor).place(relx=0.9, rely=0.15, anchor='se')



label_task = Label(window, text="Task", font=("Times", 15), fg=textColor, bg=backgroundColor).place(relx=0.1, rely=0.35, anchor='se')
task = Entry(window, font=("Times", 15), background=labelTextColor, foreground=textColor, highlightthickness=0)
task.place(relx=0.35, rely=0.35, anchor='se')

label_start = Label(window, text="Start Time", font=("Times", 15), fg=textColor, bg=backgroundColor).place(relx=0.1, rely=0.45, anchor='se')
start = Entry(window, font=("Times", 15), background=labelTextColor, foreground=textColor, highlightthickness=0)
start.place(relx=0.35, rely=0.45, anchor='se')

label_end = Label(window, text="End Time", font=("Times", 15), fg=textColor, bg=backgroundColor).place(relx=0.1, rely=0.55, anchor='se')
end = Entry(window, font=("Times", 15), background=labelTextColor, foreground=textColor, highlightthickness=0)
end.place(relx=0.35, rely=0.55, anchor='se')

label_note = Label(window, text="Note", font=("Times", 15), fg=textColor, bg=backgroundColor).place(relx=0.1, rely=0.65, anchor='se')
note = Entry(window, font=("Times", 15), background=labelTextColor, foreground=textColor, highlightthickness=0)
note.place(relx=0.35, rely=0.65, anchor='se')

btnAdd = Button(window, text='Add', highlightbackground=backgroundColor, padx=1, pady=1, width=10, command=addData).place(relx=0.14, rely=0.8, anchor='se')
clear_data = Button(window, text="Clear", highlightbackground=backgroundColor, padx=1, pady=1, width=10, command=clear).place(relx=0.27, rely=0.8, anchor='se')
search = Button(window, text="Search", highlightbackground=backgroundColor, padx=1, pady=1, width=10, command=searchData).place(relx=0.4, rely=0.8, anchor='se')
export_CSV = Button(window, text="Export", highlightbackground=backgroundColor, padx=1, pady=1, width=10, command=exportData).place(relx=0.9, rely=0.9, anchor='se')
delete = Button(window, text="Delete Entry", highlightbackground=backgroundColor, padx=1, pady=1, width=10, command=deleteData).place(relx=0.77, rely=0.9, anchor='se')


listbox = Listbox(window, background=backgroundColor, bd=1, font="Times", fg=textColor, selectbackground=backgroundColor, highlightcolor="Red", relief=FLAT, height=13, width=50)
listbox.bind('<<ListboxSelect>>', record)
listbox.place(relx=0.9, rely=0.8, anchor='se')

scrollbar = Scrollbar(listbox, command=listbox.yview, bg=labelTextColor, troughcolor=labelTextColor, width=1)
listbox.config(yscrollcommand = scrollbar.set)
scrollbar.place(relx=1, rely=0.21, anchor='se')

viewAllData()
window.mainloop()
