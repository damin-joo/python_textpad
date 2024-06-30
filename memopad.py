import os
import keyboard
import pyautogui
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox

from tkinter import *
from tkinter import filedialog

#########################
#INITIAL SETTINGS
root = Tk()
root.title("Untitled")
root.geometry("640x480+350+200")        # w x h + x + y
root.resizable(True, True)       # resize (x, y)

#
filename = ""

#########################
#FUNCTIONS
##file
def new_tab():
    pass
keyboard.add_hotkey("Ctrl+N", new_tab)

def new_window():    
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r", encoding="utf8") as file:
                txt.delete("1.0", END)
                txt.insert(END, file.read())
        except IOError as e:
            print("Error opening file: {e}")
keyboard.add_hotkey("Ctrl+Shift+N", new_window)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r", encoding="utf8") as file:
                txt.delete("1.0", END)
                txt.insert(END, file.read())
        except IOError as e:
            print("Error opening file: {e}")
        filename = file_path
keyboard.add_hotkey("Ctrl+O", open_file)

def save_file():
    filename = txt.get("1.0", END)
    if os.path.isfile(filename):
        print("Save File: " + file_path)
        try:
            with open(file_path, "w", encoding="utf8") as file:
                file.write(txt.get("1.0", END))
            with open(file_path, "r", encoding="utf8") as file:
                txt.delete("1.0", END)
                txt.insert(END, file.read())
        except IOError as e:
            print("Error saving file: {e}")
    else:
        file_path = filedialog.asksaveasfilename(title="Save", defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        try:
            open('file.txt', 'w').close()
            with open(file_path, "w", encoding="utf8") as file:
                file.write(txt.get("1.0", END))
        except IOError as e:
            print("Error saving file: {e}")
keyboard.add_hotkey("Ctrl+S", save_file)

def save_as():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        print("Save File: {file_path}")
        try:
            with open(file_path, "w", encoding="utf8") as file:
                file.write(txt.get("1.0", END))
            with open(file_path, "r", encoding="utf8") as file:
                txt.delete("1.0", END)
                txt.insert(END, file.read())
        except IOError as e:
            print("Error saving file: {e}")
keyboard.add_hotkey("Ctrl+Shift+S", save_as)

def save_all():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        print("Save File: {file_path}")
        try:
            with open(file_path, "w", encoding="utf8") as file:
                file.write(txt.get("1.0", END))
            with open(file_path, "r", encoding="utf8") as file:
                txt.delete("1.0", END)
                txt.insert(END, file.read())
        except IOError as e:
            print("Error saving file: {e}")
keyboard.add_hotkey("Ctrl+Alt+S", save_all)

def page_setup():
    pass

def print():
    pass
keyboard.add_hotkey("Ctrl+P", print)

def close_tab():
    root.quit
keyboard.add_hotkey("Ctrl+W", close_tab)

def close_window():
    root.quit
keyboard.add_hotkey("Ctrl+Shift+W", close_window)

##edit
def undo():
    print("undo key pressed")
keyboard.add_hotkey("Ctrl+Z", undo)

def cut():
    pyautogui.hotkey('ctrl', 'x')

def copy():
    pyautogui.hotkey('ctrl', 'c')

def paste():
    pyautogui.hotkey('ctrl', 'v')

def delete():
    pyautogui.hotkey('delete')

finds = []
def find():
    all_text =txt.get("1.0", "end")
    line_number = 1
    found = False
    search = "hello"
    # for line in all_text:
    #     if search in line:
    #        finds.insert(END, f"Line {line_number}: {line}")
    #         found = True
    #     line_number += 1
    
    # if found == 0:
    #     finds.insert(END, "No matching lines found.")

keyboard.add_hotkey("Ctrl+F", find)

def find_next():
    pass
keyboard.add_hotkey("F3", find)

def find_prev():
    pass
keyboard.add_hotkey("Shift+F3", find)

def replace():
    pass
keyboard.add_hotkey("Ctrl+H", find)

def go_to():
    pass
keyboard.add_hotkey("Ctrl+G", find)

def select_all():
    print("select all key pressed")
keyboard.add_hotkey("Ctrl+A", select_all)

def time_date():
    print("time data function pressed")
keyboard.add_hotkey("F5", find)

def font():
    print("font function pressed")

##view
font_index = 1
font_size = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 32, 36, 40, 44, 48]

def zoom_in():
    global font_index
    if font_index < len(font_size) -1:
        font_index += 1
        txt.config(font=("Arial", font_size[font_index]))
keyboard.add_hotkey("Ctrl+plus", zoom_in)

def zoom_out():
    global font_index
    if font_index > 0:
        font_index -= 1
        txt.config(font=("Arial", font_size[font_index]))
keyboard.add_hotkey("Ctrl+-", zoom_out)

def zoom_restore():
    global font_index
    font_index = 2
    txt.config(font=("Arial", font_size[font_index]))
keyboard.add_hotkey("Ctrl+w", zoom_restore)

def status_bar():
    print("status bar function pressed")
keyboard.add_hotkey("Ctrl+F", find)

def word_wrap():
    print("word wrap function")
keyboard.add_hotkey("Ctrl+F", find)

def update_title(event):
    update_filename = txt.get("1.0", "1.30")
    if (root.title != "Untitled") & (update_filename != ''):         #first line is not null
        root.title(update_filename + "*")
keyboard.hook(update_title)

style = ttk.Style()
def dark_mode():
    mode = darkVar.get()
    if mode == 0:               #normal mode
        # root.configure(bg='white')  
        style.configure("TMenubutton", background='white', foreground='#282828')
        txt.configure(bg='white', fg='#3c3c3c')
    elif mode == 1:             #dark mode
        # root.configure(bg='#434343') 
        style.configure("TMenubutton", background='#282828', foreground='white')
        txt.configure(bg='#3c3c3c', fg='white')
        
#########################
#MENU BAR
menu = Menu(root)

##File menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New tab", command=new_tab)
menu_file.add_command(label="New window", command=new_window)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_command(label="Save as", command=save_as)
menu_file.add_command(label="Save all", command=save_all)
menu_file.add_separator()
menu_file.add_command(label="Page setup", command=page_setup)
menu_file.add_command(label="Print", command=print)
menu_file.add_separator()
menu_file.add_command(label="Close tab", command=close_tab)
menu_file.add_command(label="Close window", command=close_window)
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

#Edit menus
menu_edit = Menu(menu, tearoff=0)
menu_edit.add_command(label="Undo", command=undo, state="disable")
menu_edit.add_separator()
menu_edit.add_command(label="Cut", command=cut, state="disable")
menu_edit.add_command(label="Copy", command=copy, state="disable")
menu_edit.add_command(label="Paste", command=paste)
menu_edit.add_command(label="Delete", command=delete, state="disable")
menu_edit.add_separator()
menu_edit.add_command(label="Find", command=find, state="disable")
menu_edit.add_command(label="Find next", command=find_next, state="disable")
menu_edit.add_command(label="Find previous", command=find_prev, state="disable")
menu_edit.add_command(label="Replace", command=replace, state="disable")
menu_edit.add_command(label="Go to", command=go_to)
menu_edit.add_separator()
menu_edit.add_command(label="Select all", command=select_all)
menu_edit.add_command(label="Time/Date", command=time_date)
menu_edit.add_separator()
menu_edit.add_command(label="Font", command=font)
menu.add_cascade(label="Edit", menu=menu_edit)

#View menus
menu_view = Menu(menu, tearoff=0)
menu_view_zoom = Menu(menu, tearoff=0)
menu_view_zoom.add_command(label="Zoom in", command=zoom_in)
menu_view_zoom.add_command(label="Zoom out", command=zoom_out)
menu_view_zoom.add_command(label="Restore deafult zoom", command=zoom_restore)
menu_view.add_cascade(label="Zoom", menu=menu_view_zoom)
statVar = IntVar()
wordVar = IntVar()
darkVar = IntVar()
menu_view.add_checkbutton(label="Status bar", variable=statVar, command=dark_mode)
menu_view.add_checkbutton(label="Word wrap", variable=wordVar, command=dark_mode)
menu_view.add_checkbutton(label="Dark mode", variable=darkVar, command=dark_mode)
menu.add_cascade(label="View", menu=menu_view)
print
#########################
#SCROLLBAR
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

#########################
#TEXTBOX
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="right", fill="both", expand=True)

#
scrollbar.config(command=txt.yview)
root.config(menu=menu)
root.mainloop()