from tkinter import *
from PIL import ImageTk, Image

root = Tk()
#Size for the calculator
root.geometry('400x500')
#MIN_Size for the calculator
root.minsize(400, 500)
#MAX_Size for the calculator
root.maxsize(400, 500)
#Set the Title
root.title('Calculator')

#Frame for Entry
f = Frame(root, width = 400, height = 50)
f.pack()
#The entry widget, where the numbers will be inserted
e = Entry(f, width = 400,borderwidth = 5, font = 'Calibri 25 bold')
e.pack(side = TOP, ipady = 10)
#Frame for Numbers
f1 = Frame(root, width = 400, height = 450)
f1.pack()
#Click_number function
def Click_number(num):
    e.insert(END, num)




def Clear():
    e.delete(0, END)

def Clear_ENTRY():
    e.delete(END, 0)

def RESULT_num():
    total = sum(a1)
    e.delete(0, END)
    e.insert(END, str(total))

def Addition():
    global a
    a = e.get()
    
    e.insert(END, ' + ')
    global a1
    a1 = a.split()
    a1 = list(set(a1))
    a1.remove('+')
    a1 = [int(i) for i in a1] 
    print(a1)

#Number Buttons
Num_percentage = Button(f1, text = '%', padx = 25, pady = 25)
Num_percentage.grid(row = 1, column = 0, ipadx = 25)

# file1 = Image.open('2710506.png')
# file1 = Image.resize((450, 350), file1.ANTIALIAS)
# Backspace_key_img = ImageTk.PhotoImage(file1)

Num_ClearEntry = Button(f1, padx =5, pady = 5, command = Clear_ENTRY)
Num_ClearEntry.grid(row = 1, column = 1, ipadx = 5)

Num_Clear = Button(f1, text = 'C', padx =25, pady = 25, command = Clear)
Num_Clear.grid(row = 1, column = 2, ipadx = 25)

Num_7 = Button(f1, text = '7', padx =25, pady = 25,command = lambda: Click_number(7))
Num_7.grid(row = 2, column = 0, ipadx = 25)

Num_8 = Button(f1, text = '8', padx =25, pady = 25,command = lambda: Click_number(8))
Num_8.grid(row = 2, column = 1, ipadx = 25)

Num_9 = Button(f1, text = '9', padx =25, pady = 25,command = lambda: Click_number(9))
Num_9.grid(row = 2, column = 2, ipadx = 25)

Num_4 = Button(f1, text = '4', padx =25, pady = 25,command = lambda: Click_number(4))
Num_4.grid(row = 3, column = 0, ipadx = 25)

Num_5 = Button(f1, text = '5', padx =25, pady = 25,command = lambda: Click_number(5))
Num_5.grid(row = 3, column = 1, ipadx = 25)

Num_6 = Button(f1, text = '6', padx =25, pady = 25,command = lambda: Click_number(6))
Num_6.grid(row = 3, column = 2, ipadx = 25)

Num_1 = Button(f1, text = '1', padx =25, pady = 25,command = lambda: Click_number(1))
Num_1.grid(row = 4, column = 0, ipadx = 25)

Num_2 = Button(f1, text = '2', padx =25, pady = 25,command = lambda: Click_number(2))
Num_2.grid(row = 4, column = 1, ipadx = 25)

Num_3 = Button(f1, text = '3', padx =25, pady = 25,command = lambda: Click_number(3))
Num_3.grid(row = 4, column = 2, ipadx = 25)

Addition_num = Button(f1, text = '+', padx =25, pady = 25, command = Addition)
Addition_num.grid(row = 5, column = 0, ipadx = 25)

RESULT = Button(f1, text = '=', padx =25, pady = 25, command = RESULT_num)
RESULT.grid(row = 5, column = 1, ipadx = 25)

root.mainloop()
