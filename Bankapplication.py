# Create a messagebox from tkinter.
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox



# Returns a dict with information about the user.
def action():
	Information = {
	'Account':37098100000016,
	'Name':'Tobias Nilsson',
	'Amount':10000,
	'Mobile':8534867764,
	'Others':'Students'
	}

# Delete all accounts.
	def clear():
		ac.delete(0,END)
		name.delete(0,END)
		amount.delete(0,END)
		mobile.delete(0,END)
		others.delete(0,END)

# Show an error if the user enters an account number
	if ac.get()=="":
			messagebox.showerror("Error" , "Enter Account Number" , parent = des)
# Returns a list of all information.
	else:
		for i in Information.items():
	# Checks if the account is an account.
			if int(ac.get()) == Information['Account'] and len(ac.get()) == 14:
	# Successfully Find Account Number
				messagebox.showinfo("Success" , "Successfully Find Account Number" , parent = des)
	# Returns a dict with information about the amount and mobile.
				data_name = Information['Name']
				data_amount = Information['Amount']
				data_mobile = Information['Mobile']
				data_others = Information['Others']


                # Creates a name
				name = Label(des , text = "Name :" , font = 'sans-serif 14 bold',bg="#CD5C5C")
				name.place(x=200, y=160,anchor='e')

				
				# Returns a Label with Amount.
				amount = Label(des , text = "Amount :" , font = 'sans-serif 14 bold',bg="#CD5C5C")
				amount.place(x=200 , y=220,anchor='e')

				# Creates a Mobile No label
				mobile = Label(des , text = "Mobile No :" , font = 'sans-serif 14 bold',bg="#CD5C5C")
				mobile.place(x=200 , y=280,anchor='e')

				# Creates a source of funds label
				funds = Label(des , text = "Source Of Funds :" , font = 'sans-serif 14 bold',bg="#CD5C5C")
				funds.place(x=200 , y=330,anchor='e')

				# Creates a Label with others
				others = Label(des , text = "Others :" , font = 'sans-serif 14 bold',bg="#CD5C5C")
				others.place(x=200 , y=470,anchor='e')

				# Creates a new entry with a serif - serif 14 bold.
				name = Entry(des, bd=5,width=40,font = 'sans-serif 14 bold', textvariable = name)
				name.place(x=220 , y= 144)
				name.insert(0,data_name)

				# Create a new Entity and insert a DataAmount into it.
				amount = Entry(des, bd=5,width=40,font = 'sans-serif 14 bold', textvariable = amount)
				amount.place(x=220 , y= 205)
				amount.insert(0,data_amount)

				# Create a new mobile entry.
				mobile = Entry(des, bd=5,width=40,font = 'sans-serif 14 bold', textvariable = mobile)
				mobile.place(x=220 , y= 262)
				mobile.insert(0,data_mobile)



				# Creates a Radio button with a Salary value
				Radio_button_sal = Radiobutton(des,text='Salary', value="salary",font = 'sans-serif 10 bold',variable = var)
				Radio_button_sal .place(x= 220 , y= 320)
				var.set('salary')

				# Creates a vahical Sale radio button
				Radio_button_vah = Radiobutton(des,text='Vahical Sale', value="vahical",font = 'sans-serif 10 bold',variable = var)
				Radio_button_vah .place(x= 220 , y= 350)

				# Creates a Property Sale button
				Radio_button_pro = Radiobutton(des,text='Property Sale', value="property",font = 'sans-serif 10 bold',variable = var)
				Radio_button_pro .place(x= 220 , y= 380)

				# Creates a new Others button
				Radio_button_others = Radiobutton(des,text='Others', value="others",font = 'sans-serif 10 bold',variable = var)
				Radio_button_others .place(x= 220 , y= 410)

				# Creates a new serif 14 - bold entry.
				others = Entry(des, bd=5,width=40,font = 'sans-serif 14 bold', textvariable = others)
				others.place(x=220 , y= 455)
				others.insert(0,data_others)

				# Creates a button with a clear button
				clear = Button(des, text = "Clear" ,font='Verdana 13 bold', command = clear)
				clear.place(x=760, y=85)
				break				
			# Enter Correct Account Number otherwise error
			else:
				messagebox.showerror("Error" , "Enter Correct Account Number" , parent = des)
				break
					


# Scan This Services Coming Soon
def scan():
	messagebox.showinfo("Scan" , "This Services Coming Soon" , parent = des)


# Disable the event.
def disable_event():
    pass	

# Cancel All Services
def cancel():
	messagebox.showinfo("Cancel" , "All Services Cancel" , parent = des)

# functions end

des = Tk()
des.title("Deshboard")	
des.maxsize(width=1200 ,  height=600)
des.minsize(width=1200 ,  height=600)
# des.iconbitmap('icon.jpg')
des.config(bg='yellow')	


# Returns a frame of a cd5c5c frame.
f=Frame(des,height=580,width=1180,bg='#CD5C5C')
f.place(x=10,y=10)


# Converts a string to a java. util. StringVar
ac = StringVar()
name = StringVar()
amount = IntVar(des, value='0')
var= StringVar()
mobile = StringVar()
others = StringVar()

 # Label Name Start 
# Create a new account no
ac_no = Label(des , text = "Account No :" , font = 'sans-serif 14 bold',bg="#CD5C5C")
ac_no.place(x=200 , y=100,anchor='e')	



 # Label Name End

 # Entry Box Start
# Creates a new entry with a des - serif 14 bold entry.
ac = Entry(des, bd=5,width=40,font = 'sans-serif 14 bold',textvariable = ac)
ac.focus()
ac.place(x=220 , y= 85)


# Entry Box End

# Creates a new frame.
a=Frame(des,height=1,width=240,bg="white")
a.place(x=880,y=120)

b=Frame(des,height=330,width=1,bg="white")
b.place(x=880,y=120)

c=Frame(des,height=1,width=240,bg="white")
c.place(x=880,y=450)

d=Frame(des,height=330,width=1,bg="white")
d.place(x=1120,y=120)




# Button Start

# Creates a Scan button with the given text.
enter = Button(des, text = "Enter" ,font='Verdana 13 bold', command = action)
enter.place(x=680, y=85)


scan = Button(des, text = "Scan" ,font='Verdana 13 bold', width=12, height=6,  command = scan)
scan.place(x=930, y=130)

cancel = Button(des, text = "Cancel" ,font='Verdana 13 bold', width=12, height=6,  command = cancel)
cancel.place(x=930, y=295)

des.mainloop()