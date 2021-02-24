import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('kushalrakesh019@gmail.com', 'Kushal@2001')


root = tk.Tk()

def Data():

    try:
        CustomerData = {
            'Name': Name_Entry.get(),
            'Product': Products.get(),
            'Quantity': Quantity_Entry.get(),
            'Email-id': Email_Entry.get()
            }
        

        Order = tk.messagebox.askquestion(title='Order Conformation', message=f"Do you want to confirm your order for {Quantity_Entry.get()} {Products.get()}")


        if Order == 'yes':
            confirmed = tk.messagebox.showinfo(title='Order Confirmed', message='Order Confirmed')
            server.sendmail('kushalrakesh019@gmail.com', Email_Entry.get(),f"Dear Customer, your order for {Quantity_Entry.get()} {Products.get()} is confirmed \n Customer Name {Name_Entry.get()}")
            Customer = open('CustomerDetails', 'a')
            Customer.write(str(CustomerData) + '\n')
        

    except smtplib.SMTPRecipientsRefused:
        Email_error = tk.messagebox.showerror(title = 'invalid email',message= 'Invalid E-mail')
        Email_Entry.delete(0, tk.END)
        Data()

    if confirmed == 'ok':
        Name_Entry.delete(0, tk.END)
        Products.delete(0, tk.END)
        Quantity_Entry.delete(0, tk.END)
        Email_Entry.delete(0, tk.END)


    



font_f = ('Arial 20')
Name_label = ttk.Label(root, text = 'Name:', font = font_f)
Product_label = ttk.Label(root, text = 'Product:', font = font_f)
Quantity_label = ttk.Label(root, text = 'Quantity', font = ('arial 20'))
Email_label = ttk.Label(root, text = 'Email-id:', font = font_f)

Name_Entry = tk.Entry(root, font = ('arial 15'))
Name_Entry.grid(row=0, column =1, padx = 5, sticky = 'W')
Products_spices = ['Chilli Powder', 'Haldi Powder', 'Dhaniya Powder']
variable = tk.StringVar(root)
variable.set('Chilli Powder')
Products = ttk.Combobox(root, values = Products_spices, font = ('arial 15'))
Products.grid(row=1, column=1, padx = 5, sticky='W')
Quantity_Entry = tk.Entry(root, width = 5, font = ('arial 15'))
Quantity_Entry.grid(row=1,column=2,padx = 110, sticky = 'W')
Email_Entry = tk.Entry(root, font = ('arial 15'), width = 40)
Email_Entry.grid(row=3, column= 1, padx = 2)


Name_label.grid(row=0, column=0, pady = 20, rowspan=1)
Product_label.grid(row=1, column=0, pady = 20)
Quantity_label.grid(row=1, column=2, pady = 20,sticky='w',rowspan = 2)
Email_label.grid(row=3, column = 0)
Submit_btn = ttk.Button(root, text = 'Submit', command = Data)
Submit_btn.grid(row=4, column = 1)
root.mainloop()