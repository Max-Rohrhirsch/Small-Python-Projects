#!/bin/python3.9
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
import os

#define beginning
root = Tk()
root.title("Text Editor")
root.geometry("1200x660")
textFile = ""
global zwischen
global openStatusFile
openStatusFile = False
global selected
selected = False


#----------------Define menu buttons-----------------
def newFile():
    text.delete("1.0", END)
    root.title("New File")
    status.config(text="New File    ")
    global openStatusFile
    openStatusFile = False

def openFile(e):
    text.delete("1.0", END)
    global zwischen
    textFile = filedialog.askopenfilename(initialdir="/home/max/Schreibtisch/", title="Open File")
    #, filetypes=(("Text Files", "*.txt"), ("HTML Files"), "*.html"), ("Python Files", "*.py"), ("All Files", "*.*"))
    zwischen = textFile
    if textFile:
        global openStatusFile
        openStatusFile = textFile
    name = textFile
    status.config(text=name)
    root.title(f'{name} - Text Editor')
    textFile = open(textFile, 'r')
    stuff = textFile.read()
    text.insert(END, stuff)
    textFile.close()

def saveAs():
    textFile = filedialog.asksaveasfilename(defaultextension=".*",  initialdir="/home/max/Schreibtisch/", title="Save File")
    global zwischen
    if textFile:
        zwischen = textFile
        name = zwischen
        name = name.replace("/home/max/Schreibtisch/", "")
        root.title(f'{name} - Text Editor')
        status.config(text=name)
        textFile = open(textFile, 'w')
        textFile.write(text.get(1.0, END))
        textFile.close()

def saveFile(e):
    global openStatusFile
    if openStatusFile:
        textFile = open(openStatusFile, 'w')
        textFile.write(text.get(1.0, END))
        textFile.close()
    else:
        saveAs()

def cutText(e):
    global selected
    if text.selection_get():
        selected = text.selection_get()
        text.delete("sel.first", "sel.last")

def copyText(e):
    global selected
    if text.selection_get():
        selected = text.selection_get()

def pasteText(e):
    if selected:
        position = text.index(INSERT)
        text.insert(position, selected)



#----------Text Decoration------------
def boldIt():
    boldFont = font.Font(text, text.cget("font"))
    boldFont.configure(weight="bold")
    text.tag_configure("bold", font=boldFont)
    currentTags = text.tag_names("sel.first")
    if "bold" in currentTags:
        text.tag_remove("bold", "sel.first", "sel.last")
    else:
        text.tag_add("bold", "sel.first", "sel.last")

def kursivIt():
    kursivFont = font.Font(text, text.cget("font"))
    kursivFont.configure(slant="italic")
    text.tag_configure("italic", font=kursivFont)
    currentTags = text.tag_names("sel.first")
    if "italic" in currentTags:
        text.tag_remove("italic", "sel.first", "sel.last")
    else:
        text.tag_add("italic", "sel.first", "sel.last")

def textColor():
    myColor = colorchooser.askcolor()[1]
    if myColor:
        colorFont = font.Font(text, text.cget("font"))
        text.tag_configure("colored", font=colorFont, foreground=myColor)
        currentTags = text.tag_names("sel.first")
        if "colored" in currentTags:
            text.tag_remove("colored", "sel.first", "sel.last")
        else:
            text.tag_add("colored", "sel.first", "sel.last")

def bgColor():
    myColor = colorchooser.askcolor()[1]
    if myColor:
        text.config(bg=myColor)

def allColor():
        myColor = colorchooser.askcolor()[1]
        if myColor:
            text.config(fg=myColor)



#-----------------------programming things------------------------
def printCommand(e):
    position = text.index(INSERT)
    print(position)
    text.insert(position, "print")


def klammerCommand(e):
    position = text.index(INSERT)
    text.insert(position, ")")

def runPython(e):
    global openStatusFile
    if openStatusFile:
        os.system("python "+zwischen)
    else:
        saveAs()
        runPython()

def runNode(e):
    global openStatusFile
    if openStatusFile:
        os.system("node "+zwischen)
    else:
        saveAs()
        runNode()

def betterColors(e):
    text.config(bg="#222222")
    text.config(fg="white")

#------------------------Define Tkinter things--------------------
tollbarFrame = Frame(root)
tollbarFrame.pack(fill=X)
frame = Frame(root).pack(fill="both")
scrolls = Scrollbar(frame)
scrolls.pack(side=RIGHT, fill=Y)
hScroll = Scrollbar(frame,orient='horizontal' )

text = Text(frame, width=97, height=25, font=("Helvetica", 16), selectbackground="orange", yscrollcommand=scrolls.set, wrap="none", xscrollcommand=hScroll.set)



text.pack(fill="both")
hScroll.config(command=text.xview)
scrolls.config(command=text.yview)
menue = Menu(root)
root.config(menu=menue)

status = Label(root, text='Ready  ', anchor=E)
status.pack(fill=X, side=BOTTOM, ipady=5)

#----------------Menu Buttons--------------------
file_menu = Menu(menue, tearoff=False)
menue.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command = newFile)
file_menu.add_command(label="Open", command = openFile)
file_menu.add_command(label="Save", command= saveFile)
file_menu.add_command(label="Save As", command = saveAs)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(menue, tearoff=False)
menue.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cutText(False), accelerator="(Ctrl+x)")
edit_menu.add_command(label="Copy", command=lambda: copyText(False), accelerator="(Ctrl+c)")
edit_menu.add_command(label="Paste", command=lambda: pasteText(False), accelerator="(Ctrl+v)")
edit_menu.add_command(label="Undo", command=text.edit_undo, accelerator="(Ctrl+z)" )
edit_menu.add_command(label="Redo", command=text.edit_redo, accelerator="(Ctrl+y)" )

color_menu = Menu(menue, tearoff=False)
menue.add_cascade(label="Colors", menu=color_menu)
color_menu.add_command(label="Change selected Color", command = textColor)
color_menu.add_command(label="Change all Color", command = allColor)
color_menu.add_command(label="Change bg", command = bgColor)

boldbutton = Button(tollbarFrame, text="Bold", command=boldIt)
boldbutton.grid(row=0, column=0, sticky=W, pady=5)
boldbutton = Button(tollbarFrame, text="Italic", command=kursivIt)
boldbutton.grid(row=0, column=1, sticky=W, pady=5)
colorButton = Button(tollbarFrame, text="Text Color", command=textColor)
colorButton.grid(row=0, column=2, sticky=W, pady=5)



#------------------Spezial Things------------------
root.bind('<Control-Key-s>', saveFile)
root.bind('<Control-Key-t>', saveAs)
root.bind('<Control-Key-o>', openFile)
root.bind('<Control-Key-p>', runPython)
root.bind('<Control-Key-b>', printCommand)
root.bind('<Shift-8>', klammerCommand)
root.bind('<Control-Key-f>', betterColors)
root.bind('<Control-Key-n>', runNode)








root.mainloop()
