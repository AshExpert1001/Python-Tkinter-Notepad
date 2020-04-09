from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    _root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = None

    else:
        _root.title(os.path.basename(file) + "- Notepad")
        TextArea.delete(1.0, END)
        f = open(file, 'r')
        TextArea.insert(1.0, f.read())
        f.close()

def saveAs():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, 'w')
            f.write(TextArea.get(1.0, END))
            f.close()

        _root.title(os.path.basename(file)+"- Notepad")
        print("File Saved")

    else:
        f = open(file, 'w')
        f.write(TextArea.get(1.0, END))
        f.close()

def exitApp():
    _root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(('<<Paste>>'))

def about():
    showinfo("About Notepad", "Notepad by AshExpert")

if __name__ == '__main__':
    _root = Tk()
    _root.geometry("720x520")
    _root.minsize(220, 200)
    _root.title("Untitled - Notepad")
    _root.wm_iconbitmap("icon/icon.ico")

    # Add TextArea
    TextArea = Text(_root, font="Consolas 12", bg="#000", fg="green")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # MenuBar here
    MenuBar = Menu(_root)
    # File menu
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New File", command=newFile)
    FileMenu.add_command(label="Open File", command=openFile)
    FileMenu.add_command(label="Save As", command=saveAs)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=exitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    # Edit menu
    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    # Help Menu
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    _root.config(menu=MenuBar)

    # Scrollbar add
    ScrollY = Scrollbar(TextArea)
    ScrollY.pack(side=RIGHT, fill=Y)
    ScrollY.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=ScrollY.set)

    _root.mainloop()