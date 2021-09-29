from tkinter import *
from tkinter import filedialog
import os
from PIL import ImageTk,Image
root = Tk()
root.minsize(650,650)
root.maxsize(650,650)

open_image = ImageTk.PhotoImage(Image.open('open.png'))
save_image = ImageTk.PhotoImage(Image.open('save.png'))
exit_image = ImageTk.PhotoImage(Image.open('exit.jpg'))

label_file_name = Label(root,text='File Name:')
label_file_name.place(relx=0.28,rely=0.03,anchor=CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.5,rely=0.03,anchor=CENTER)

my_text = Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.5,anchor=CENTER)

name = ''
def openFile():
    global name
    my_text.delete(1.0,END)
    input_file_name.delete(0,END)
    text_file = filedialog.askopenfilename(title='Open Text File',filetypes=(('text files','*.txt'),))
    print(text_file)
    name = os.path.basename(text_file)
    formatted_name = name.split('.')[0]
    input_file_name.insert(END,formatted_name)
    root.title(formatted_name)
    text_file = open(name,'r')
    paragraph = text_file.read()
    my_text.insert(END,paragraph)
    text_file.close()
    
def saveFile():
    input_name = input_file_name.get()
    file = open(input_name + ".txt",'w')
    data = my_text.get('1.0',END)
    print(data)
    file.write()
    input_file_name.delete(0,END)
    my_text.delete(1.0,END)
    messagebox.showinfo('Update:','Your file has been saved successfully!')
    
def exitFile():
    root.destroy()

openBtn = Button(root,image=open_image,text = 'Open File',command=openFile)
saveBtn = Button(root,image=save_image,text = 'Save File',command=saveFile)
exitBtn = Button(root,image=exit_image,text = 'Exit File',command=exitFile)

openBtn.place(relx=0.1,rely=0.03,anchor=CENTER)
saveBtn.place(relx=0.15,rely=0.03,anchor=CENTER)
exitBtn.place(relx=0.2,rely=0.03,anchor=CENTER)

root.mainloop()
