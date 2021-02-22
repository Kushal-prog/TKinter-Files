from tkinter import *


root = Tk()
#Size for the calculator
root.geometry('660x760')
#MIN_Size for the calculator
root.minsize(660, 760)
root.maxsize(660, 760)
#MAX_Size for the calculator
#Set the Title
root.title('Calculator')

root.iconbitmap('Dtafalonso-Android-Lollipop-Calculator.ico')


Entry1 = Entry(root, bg = 'orange', font = ('Arial 40 bold'), bd = 30, justify = RIGHT,width = 20)
Entry1.grid(row = 0, column = 0, columnspan = 5)

if len(Entry1.get()) == 0:
        Entry1.insert(END, '0')

def insert_numbers(num):
    Entry1.insert(END,num)
    Equal_to['state'] = ACTIVE

def Backspace():
    e = Entry1.get()
    Entry1.delete(len(e) - 1)


def RESULT_num():
    a = Entry1.get()

    a1 = a.replace('X', '*').replace('÷', '/')

    if a1 == '0/1':
        Entry1.insert(END, '0')


    


    try:
        a1.lstrip('0')
        RESULT_ev = eval(a1)
        

    except ZeroDivisionError:
        Entry1.delete(0, END)
        Entry1.insert(END, 'Cannot divide by zero')


    except SyntaxError:
        Entry1.delete(0, END)
        Entry1.insert(END, 'Wrong input entered')

    else:
        Entry1.delete(0, END)
        a1.lstrip('0')
        Entry1.insert(END, RESULT_ev)



       
# def sqrt():
#     e = Entry1.get()
#     e = e.replace('√', '**(1/2)')
#     s = '**(1/2)'
#     n = [i for i in e]
#     s, n = n, s
#     n, s = n, s



def Clear():
    Entry1.delete(0, END)




Num_7 = Button(root, anchor = CENTER, text = '7', font = ('Arial 20 bold'), padx = 50, pady = 30, bd = 8,command = lambda: insert_numbers(7), bg = 'cyan',activebackground = 'red')
Num_7.grid(row = 1, column = 0,ipadx =5)

Num_8 = Button(root, anchor = CENTER, text = '8', font = ('Arial 20 bold'), padx = 50, pady = 30, bd = 8, command = lambda: insert_numbers(8), bg = 'cyan',activebackground = 'red')
Num_8.grid(row = 1, column = 1,ipadx =5)

Num_9 = Button(root, anchor = CENTER, text = '9', font = ('Arial 20 bold'), padx = 50, pady = 30, bd = 8, command = lambda: insert_numbers(9), bg = 'cyan',activebackground = 'red')
Num_9.grid(row = 1, column = 2,ipadx =5)

Num_add = Button(root, anchor = CENTER, text = '+', font = ('Arial 20 bold'), padx = 50, pady = 30, bd = 8, command = lambda: insert_numbers('+'), bg = 'cyan',activebackground = 'red')
Num_add.grid(row = 1, column = 3,ipadx =5)

Num_4 = Button(root, anchor = CENTER, text = '4', font = ('Arial 20 bold'), padx = 50, pady = 30, bd = 8, command = lambda: insert_numbers(4), bg = 'cyan',activebackground = 'red')
Num_4.grid(row = 2, column = 0,ipadx =5)

Num_5 = Button(root, anchor = CENTER, text = '5', font = ('Arial 20 bold'), padx = 50, pady = 30, bd = 8, command = lambda: insert_numbers(5), bg = 'cyan',activebackground = 'red')
Num_5.grid(row = 2, column = 1,ipadx =5)

Num_6 = Button(root, anchor = CENTER, text = '6', font = ('Arial 20 bold'), padx = 50, pady = 30, bd = 8, command = lambda: insert_numbers(6), bg = 'cyan',activebackground = 'red')
Num_6.grid(row = 2, column = 2,ipadx =5)

Num_sub = Button(root, anchor = CENTER, text = '-', font = ('Arial 22 bold'), padx = 50, pady = 30, bd = 8, command = lambda: insert_numbers('-'), bg = 'cyan',activebackground = 'red')
Num_sub.grid(row = 2, column = 3,ipadx =5)

Num_1 = Button(root, anchor = CENTER, text = '1', font = ('Arial 20 bold'), padx = 50, pady = 30, bd = 8, command = lambda: insert_numbers(1), bg = 'cyan',activebackground = 'red')
Num_1.grid(row = 3, column = 0,ipadx =5)

Num_2 = Button(root, anchor = CENTER, text = '2', font = ('Arial 20 bold'), padx = 50, pady = 30, bd = 8, command = lambda: insert_numbers(2), bg = 'cyan',activebackground = 'red')
Num_2.grid(row = 3, column = 1,ipadx =5)

Num_3 = Button(root, anchor = CENTER, text = '3', font = ('Arial 20 bold'), padx = 50, pady = 30, bd = 8, command = lambda: insert_numbers(3), bg = 'cyan',activebackground = 'red')
Num_3.grid(row = 3, column = 2,ipadx =5)

Num_Multiply = Button(root,anchor = CENTER,text = 'X', font = ('Arial 20 bold'),padx = 50, pady = 30, bd = 8, command = lambda: insert_numbers('X'), bg = 'cyan',activebackground = 'red')
Num_Multiply.grid(row = 3, column = 3,ipadx =5)


Num_0 = Button(root, anchor = CENTER, text = '0', font = ('Arial 20 bold'), padx = 50, pady = 30, bd = 8, command = lambda: insert_numbers(0), bg = 'cyan',activebackground = 'red')
Num_0.grid(row = 4, column = 0,ipadx =5)

Clear_Button = Button(root, anchor = CENTER, text = 'C', font = ('Arial 20 bold'), padx = 50, pady = 30, bd = 8, command = Clear, bg = 'cyan',activebackground = 'red')
Clear_Button.grid(row = 5, column = 0,ipadx =5)

Equal_to = Button(root,anchor = CENTER,text = '=', font = ('Arial 20 bold'),padx = 50, pady = 30, bd = 8,command = RESULT_num, state = DISABLED, bg = 'cyan',activebackground = 'red')
Equal_to.grid(row = 4, column = 2,ipadx =5)


Num_divide = Button(root,anchor = CENTER,text = '÷', font = ('Arial 20 bold'),padx = 50, pady = 30, bd = 8, command = lambda: insert_numbers('÷'), bg = 'cyan',activebackground = 'red')
Num_divide.grid(row = 4, column = 3,ipadx = 5)

point = Button(root,anchor = CENTER,text = '.', font = ('Arial 20 bold'),padx = 50, pady = 30, bd = 8, command = lambda: insert_numbers('.'), bg = 'cyan',activebackground = 'red')
point.grid(row = 4, column = 1, ipadx = 5)

# Backspace_img = Image.open('Backspace.png')
# resized = Backspace_img.resize((300, 225), Image.ANTIALIAS)
# Backspace_img = ImageTk.PhotoImage(file = 'Backspace.png')

Backspace_Key = Button(root, anchor = CENTER, text = "Backspace" ,font = ('Arial 10 bold'),padx = 35, pady = 45, bd = 8, command = Backspace, bg = 'cyan',activebackground = 'red')
Backspace_Key.grid(row = 5, column = 1, ipadx = 5, sticky = W)

Num_square_root = Button(root, anchor = CENTER, text = '√x',font = ('Arial 10 bold'),padx = 55, pady = 45, bd = 8, command = lambda: insert_numbers('**(1/2)'), bg = 'cyan',activebackground = 'red')
Num_square_root.grid(row = 5, column = 2, ipadx = 5, sticky = W)

Num_square = Button(root, anchor = CENTER, text = 'x²' ,font = ('Arial 10 bold'),padx = 55, pady = 45, bd = 8, command = lambda: insert_numbers('**2'), bg = 'cyan',activebackground = 'red')
Num_square.grid(row = 5, column = 3, ipadx = 5,sticky = W)

root.mainloop()

