from tkinter import *					#pip install tkintertable
from tkcalendar import DateEntry		#pip install tkcalendar
import back								#importing backend python script
from tkinter import messagebox
import os
import subprocess						#pip install subprocess.run

#download DB Brouser for sqlite3 ( https://sqlitebrowser.org/dl/ )


def send_recived():
	a=ie1.get() #date
	b=ie2.get()	#title
	c=int(ie3.get()) #amount
	back.recived(a,b,c)

def send_spent():
	a=ee1.get() #date
	b=ee2.get()	#title
	c=int(ee3.get()) #amount
	back.spent(a,b,c)

def send_open():
	a=messagebox.askquestion("HELLO","Do You Want To Add!!")
	#print(a)
	if a == 'yes':
		a=oe1.get()
		back.open_b(a)
	else:
		i=messagebox.showinfo(message='Will not add')

def closE():
	global t1
	t1.destroy()
	balwin()

def open_db():
	i=messagebox.showinfo(message='Root window will work till DB Browser is closed.')
	subprocess.call(['C:/Program Files/DB Browser for SQLite/DB Browser for SQLite.exe', 'My_data.db'])


def inwin():
	global ie1,ie2,ie3

	t=Toplevel()
	t.title("The Expence")
	t.geometry('600x400')
	t.resizable(False,False)

	fr= LabelFrame(t,	text="Income!!! ",
		font=("Comic Sans MS",15,"bold"),		
		bd=3,width=500,height=300)
	fr.pack()

	l1= Label(fr,	text="Date",
		font=("Comic Sans MS",13,"bold"))
	l1.grid(row=0,sticky="E",padx=10)

	fr1=Frame(fr,height=75,width=100)
	fr1.grid(row=1)

	l2= Label(fr,	text="Title",
		font=("Comic Sans MS",13,"bold"))		
	l2.grid(row=1,sticky="E",padx=10)
	
	fr2=Frame(fr,height=75,width=100)
	fr2.grid(row=2)

	l3= Label(fr,	text="Amount",
		font=("Comic Sans MS",13,"bold"))
	l3.grid(row=2,sticky="E",padx=10)
	
	fr3=Frame(fr,height=75,width=100)
	fr3.grid(row=0,column=1)

	ie1=DateEntry(fr,width=25)
	ie1.grid(row=0,column=1)
	
	fr4=Frame(fr,height=75,width=200)
	fr4.grid(row=1,column=1)

	ie2=Entry(fr,width=30)
	ie2.grid(row=1,column=1)
	
	fr5=Frame(fr,height=75,width=200)
	fr5.grid(row=2,column=1)

	ie3=Entry(fr,width=30)
	ie3.grid(row=2,column=1)

	b= Button(fr,	text="Add!!",
		font=("Comic Sans MS",10,"bold"),
		width=13,bd=5,command=send_recived)					#to connect externally ------------------
	b.grid(row=3,columnspan=2,pady=10)

	b1= Button(t,	text="Close!!",
		font=("Comic Sans MS",10,"bold"),
		width=15,bd=5,command=t.destroy)
	b1.pack(pady=10)

def exwin():

	global ee1,ee2,ee3

	t=Toplevel()
	t.title("The Expence")
	t.geometry('600x400')
	t.resizable(False,False)

	fr= LabelFrame(t,	text="Spent!!! ",
		font=("Comic Sans MS",15,"bold"),
		bd=3,width=500,height=300)
	fr.pack()

	l1= Label(fr,	text="Date",
		font=("Comic Sans MS",13,"bold"))
	l1.grid(row=0,sticky="E",padx=10)

	fr1=Frame(fr,height=75,width=100)
	fr1.grid(row=1)

	l2= Label(fr,	text="Title",
		font=("Comic Sans MS",13,"bold"))
	l2.grid(row=1,sticky="E",padx=10)
	
	fr2=Frame(fr,height=75,width=100)
	fr2.grid(row=2)

	l3= Label(fr,	text="Amount",
		font=("Comic Sans MS",13,"bold"))
	l3.grid(row=2,sticky="E",padx=10)
	
	fr3=Frame(fr,height=75,width=100)
	fr3.grid(row=0,column=1)

	ee1=DateEntry(fr,width=25)
	ee1.grid(row=0,column=1)
	
	fr4=Frame(fr,height=75,width=200)
	fr4.grid(row=1,column=1)

	ee2=Entry(fr,width=30)
	ee2.grid(row=1,column=1)
	
	fr5=Frame(fr,height=75,width=200)
	fr5.grid(row=2,column=1)

	ee3=Entry(fr,width=30)
	ee3.grid(row=2,column=1)

	b= Button(fr,	text="Add!!",
		font=("Comic Sans MS",10,"bold"),
		width=13,bd=5,command=send_spent)							#to connect externally ------------------
	b.grid(row=3,columnspan=2,pady=10)

	b1= Button(t,	text="Close!!",
		font=("Comic Sans MS",10,"bold"),
		width=15,bd=5,command=t.destroy)
	b1.pack(pady=10)

def balwin():
	global t1
	t1=Toplevel()
	t1.title("The Expence")
	t1.geometry('600x400')
	t1.resizable(False,False)

	fr= LabelFrame(t1,	text="Balance!! ",
		font=("Comic Sans MS",15,"bold"),bd=3)
	fr.pack(pady=10)

	b2= Button(fr,	text="refresh",
		font=("Comic Sans MS",8,"bold"),bd=5,command=closE)
	b2.grid(row=0,column=1,sticky="E",padx=10)

	var = StringVar()
	var.set(back.bal())

	l= Label(fr,	textvariable = var,
		font=("Comic Sans MS",14,"bold"),
		height=3,width=30,bg="red",bd=10)
	l.grid(row=1,padx=10,pady=10,columnspan=2)

	

	l1= Label(fr,	text="To open Balance Sheet",
		font=("Comic Sans MS",15,"bold"))
	l1.grid(row=2,pady=10,sticky="E")

	b= Button(fr,	text="Click Here!!!",
		font=("Comic Sans MS",10,"bold"),bd=5,command=open_db)
	b.grid(row=2,column=1,sticky="W",padx=10,pady=10)

	b1= Button(t1,	text="Close!!",
		font=("Comic Sans MS",10,"bold"),
		width=15,bd=5,command=t1.destroy)
	b1.pack(pady=10)

def open_bal():
	global oe1
	i=messagebox.showinfo(message='Only for first time user')
	t=Toplevel()
	t.title("The Expence")
	t.geometry('350x250')
	t.resizable(False,False)

	fr= LabelFrame(t,	text="Opening Balance!! ",
		font=("Comic Sans MS",15,"bold"),bd=3)
	fr.pack(pady=10)

	l1= Label(fr,	text="Enter Balance",
		font=("Comic Sans MS",13,"bold"))
	l1.grid(row=0,sticky="E",padx=10,pady=20)

	oe1=Entry(fr,width=25)
	oe1.grid(row=0,column=1,pady=20,padx=10)

	b= Button(fr,	text="Add!!",
		font=("Comic Sans MS",10,"bold"),
		width=13,bd=5,command=send_open)							#to connect externally ------------------
	b.grid(row=1,columnspan=2,pady=10)


	b1= Button(t,	text="Close!!",
		font=("Comic Sans MS",10,"bold"),
		width=15,bd=5,command=t.destroy)
	b1.pack(pady=10)


root=Tk()
root.title("The Expence")
root.geometry('600x400')
root.resizable(False,False)

fr= LabelFrame(root,text="The Expence",
	font=("Comic Sans MS",10,"bold"),bd=3)
fr.pack()

l1= Label(fr,	text="For Income",
	font=("Comic Sans MS",15,"bold"))
l1.grid(row=0,sticky="E",padx=10)

fr1=Frame(fr,height=75,width=200)
fr1.grid(row=1)

l2= Label(fr,	text="For Expence",
	font=("Comic Sans MS",15,"bold"))
l2.grid(row=1,sticky="E",padx=10)

fr2=Frame(fr,height=75,width=200)
fr2.grid(row=2)

l3= Label(fr,	text="For Balance",
	font=("Comic Sans MS",15,"bold"))
l3.grid(row=2,sticky="E",padx=10)


fr2_1=Frame(fr,height=75,width=200)
fr2_1.grid(row=3)

l4= Label(fr,	text="For Opening Balance",
	font=("Comic Sans MS",15,"bold"))
l4.grid(row=3,sticky="E",padx=10)


fr3=Frame(fr,height=75,width=200)
fr3.grid(row=0,column=1)

b1= Button(fr,	text="Click Here!!!",
	font=("Comic Sans MS",10,"bold"),
	bd=5, command=inwin)
b1.grid(row=0,column=1,sticky="W",padx=10)

fr4=Frame(fr,height=75,width=200)
fr4.grid(row=1,column=1)

b2= Button(fr,	text="Click Here!!!",
	font=("Comic Sans MS",10,"bold"),
	bd=5, command=exwin)
b2.grid(row=1,column=1,sticky="W",padx=10)

fr5=Frame(fr,height=75,width=200)
fr5.grid(row=2,column=1)

b3= Button(fr,	text="Click Here!!!",
	font=("Comic Sans MS",10,"bold"),
	bd=5, command=balwin )
b3.grid(row=2,column=1,sticky="W",padx=10)


fr6=Frame(fr,height=75,width=200)
fr6.grid(row=3,column=1)

b4= Button(fr,	text="Click Here!!!",
	font=("Comic Sans MS",10,"bold"),
	bd=5,command=open_bal)
b4.grid(row=3,column=1,sticky="W",padx=10)


b5= Button(root,	text="Close!!",
	font=("Comic Sans MS",10,"bold"),
	width=15,bd=5,command=root.destroy)
b5.pack(pady=10)

root.mainloop()