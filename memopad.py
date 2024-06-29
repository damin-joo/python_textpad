import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox

from tkinter import *
from tkinter import filedialog

#INITIAL SETTINGS
root = Tk()
root.title("Untitled")
root.geometry("640x480+350+200")        # w x h + x + y
root.resizable(True, True)       # resize (x, y)

#
filename = "mynote.txt"

#FUNCTIONS
def new_window():
    
    if os.path.isfile(filename):
        open(filename, "r", encoding="utf8")

def open_file():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))

def save_as():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))

def save_all():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))

def undo():
    pass

def cut():
    pass

def copy():
    pass

def paste():
    pass

def delete():
    pass

def find():
    pass

def find_next():
    pass

def find_prev():
    pass

def replace():
    pass

def go_to():
    pass

def select_all():
    pass

def time_date():
    pass

def font():
    pass

def zoom_in():
    pass

def zoom_out():
    pass

def zoom_restore():
    pass

def status_bar():
    pass

def word_wrap():
    pass

#MENU BAR
menu = Menu(root)

##File menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New tab", command=new_window)
menu_file.add_command(label="New window", command=new_window)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_command(label="Save as", command=save_as)
menu_file.add_command(label="Save all", command=save_all)
menu_file.add_separator()
menu_file.add_command(label="Page setup", command=0)
menu_file.add_command(label="Print", command=0)
menu_file.add_separator()
menu_file.add_command(label="Close tab", command=root.quit)
menu_file.add_command(label="Close window", command=root.quit)
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

#Edit menus
menu_edit = Menu(menu, tearoff=0)
menu_edit.add_command(label="Undo", command=0, state="disable")
menu_edit.add_separator()
menu_edit.add_command(label="Cut", command=0, state="disable")
menu_edit.add_command(label="Copy", command=0, state="disable")
menu_edit.add_command(label="Paste", command=0)
menu_edit.add_command(label="Delete", command=0, state="disable")
menu_edit.add_separator()
menu_edit.add_command(label="Find", command=0, state="disable")
menu_edit.add_command(label="Find next", command=0, state="disable")
menu_edit.add_command(label="Find previous", command=0, state="disable")
menu_edit.add_command(label="Replace", command=0, state="disable")
menu_edit.add_command(label="Go to", command=0)
menu_edit.add_separator()
menu_edit.add_command(label="Select all", command=0)
menu_edit.add_command(label="Time/Date", command=0)
menu_edit.add_separator()
menu_edit.add_command(label="Font", command=0)
menu.add_cascade(label="Edit", menu=menu_edit)

#Niew menus
menu_view = Menu(menu, tearoff=0)
menu_view_zoom = Menu(menu, tearoff=0)
menu_view_zoom.add_command(label="Zoom in", command=0)
menu_view_zoom.add_command(label="Zoom out", command=0)
menu_view_zoom.add_command(label="Restore deafult zoom", command=0)
menu_view.add_cascade(label="Zoom", menu=menu_view_zoom)
menu_view.add_checkbutton(label="Status bar")
menu_view.add_checkbutton(label="Word wrap")
menu.add_cascade(label="View", menu=menu_view)

#COMBOBOX
opt_darkmode = ["Normal Mode", "Dark Mode"]
darkmode_opt = ttk.Combobox(root, values=opt_darkmode, state="readonly")
darkmode_opt.current(0)
darkmode_opt.pack(side="top", padx=5)

def dark_mode(event):
    current_mode = darkmode_opt.get()
    if current_mode == "Normal Mode":
        root.configure(bg='white')
        txt.configure(bg='white', fg='black')
    else:
        root.configure(bg='black')
        txt.configure(bg='black', fg='white')

darkmode_opt.bind("<<ComboboxSelected>>", dark_mode)

#SCROLLBAR
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")


#TEXTBOX
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="right", fill="both", expand=True)

#
scrollbar.config(command=txt.yview)
root.config(menu=menu)
root.mainloop()