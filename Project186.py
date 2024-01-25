import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import simplecrypt as crypt

root = tk.Tk()
root.title('Text Editor w/ Encryption & Decryption')
root.minsize(650, 650)
root.configure(background = 'mistyrose1')

def getImg(imgName):
    return ImageTk.PhotoImage(Image.open(imgName))

def readLine(file):
    return file.readline().rstrip() 

def encrypt(text):
    ciphercode = crypt.encrypt('AIM', text)
    hexStr = ciphercode.hex()
    
    print('Encryption:\n' + str(hexStr))
    return(hexStr)

def decrypt(hexStr):
    byteStr = bytes.fromhex(hexStr)
    oriText = crypt.decrypt('AIM', byteStr)
    finalText = oriText.decode('utf-8')
    
    print('Decryption:\n' + str(finalText))
    return(finalText)

lblFileName = tk.Label(root, text = 'File Name:', bg = 'light blue', fg = 'black')
lblFileName.place(relx = 0.5, rely = 0.05, anchor = tk.CENTER)

entFileName = tk.Entry(root)
entFileName.place(relx = 0.5, rely = 0.1, anchor = tk.CENTER)

myTxt = tk.Text(root, height = 25, width = 60)
myTxt.place(relx = 0.5, rely = 0.3, anchor = tk.N)

# Buttons
imgs = []
for i in range(2):
    imgs.append(getImg(f'Class158+/Icons/Icon { i }.png'))

def openFile(name):  
    try:
        FILE = open(f'Project186+/{ name }.txt', 'r')
        myTxt.delete(1.0, tk.END)
        data = decrypt(FILE.read())
        myTxt.insert(tk.END, data)
        FILE.close()
    except (FileNotFoundError):
        messagebox.showerror('Hey!', 'Invalid File Name')

def saveFile(name):
    FILE = open(f'Project186+/{ name }.txt', 'w')
    data = encrypt(myTxt.get('1.0', tk.END))
    FILE.write(data)
    messagebox.showinfo('Info', 'Saved Successfully')

btnOpen = tk.Button(root, bg = 'salmon', command = lambda: openFile(entFileName.get()))
btnOpen.place(relx = 0.45, rely = 0.2, anchor = tk.CENTER)
btnOpen['image'] = imgs[0]

btnSave = tk.Button(root, bg = 'salmon', command = lambda: saveFile(entFileName.get()))
btnSave.place(relx = 0.55, rely = 0.2, anchor = tk.CENTER)
btnSave['image'] = imgs[1]

root.mainloop()