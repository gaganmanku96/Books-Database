from tkinter import *
from backend import database

db = database()


def view_comm():
	viewdb.delete(0,END)
	for row in db.view():
		viewdb.insert(END,row)

def search_comm():
	viewdb.delete(0,END)
	for row in db.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
		viewdb.insert(END,row)

def insert_comm():
	viewdb.delete(0,END)
	db.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())	
	viewdb.insert(END,'Insert Successfully')
	clear()	


def get_selected_row(Event):
	try:
		global selected_tuple
		index=viewdb.curselection()[0]
		selected_tuple=viewdb.get(index)
		clear()
		title_e.insert(END,selected_tuple[1])
		author_e.insert(END,selected_tuple[2])
		year_e.insert(END,selected_tuple[3])
		ISBN_e.insert(END,selected_tuple[4])
	except:
		pass
	
def clear():
	title_e.delete(0,END)
	ISBN_e.delete(0,END)
	year_e.delete(0,END)
	author_e.delete(0,END)

def display():
	title_e.insert(END,title_e.get())
	ISBN_e.insert(END,ISBN_e.get())
	year_e.insert(END,year_e.get())
	author_e.insert(END,author_e.get())

def delete_comm():
	db.delete(selected_tuple[0])
	viewdb.delete(0,END)
	clear()
	view_comm()

def update_comm():
	db.update(selected_tuple[0],title_e.get(),author_e.get(),year_e.get(),ISBN_e.get())
	viewdb.delete(0,END)
	view_comm()


window=Tk()

title=Label(window,text="  Title")
title.grid(row=0,column=1)

title_text=StringVar()
title_e=Entry(window, textvariable=title_text)
title_e.grid(row=0,column=2)

author=Label(window,text="  Author")
author.grid(row=0,column=3)

author_text=StringVar()
author_e=Entry(window,textvariable=author_text)
author_e.grid(row=0,column=4)

year=Label(window,text="  Year")
year.grid(row=1,column=1)

year_text=StringVar()
year_e=Entry(window,textvariable=year_text)
year_e.grid(row=1,column=2)

ISBN=Label(window,text="  ISBN")
ISBN.grid(row=1,column=3)

isbn_text=StringVar()
ISBN_e=Entry(window,textvariable=isbn_text)
ISBN_e.grid(row=1,column=4)

viewAllBt=Button(window,text="View All",width=10,command=view_comm)
viewAllBt.grid(row=2,column=4)

searchEntBt=Button(window,text="Search Entry",width=10,command=search_comm)
searchEntBt.grid(row=3,column=4)

delEntBt=Button(window,text="Delete Entry",width=10,command=delete_comm)
delEntBt.grid(row=4,column=4)
updateEntBt=Button(window,text="Update Entry",width=10,command=update_comm)
updateEntBt.grid(row=5,column=4)
addBt=Button(window,text="Add Entry",width=10,command=insert_comm)
addBt.grid(row=6,column=4)
clearBt=Button(window,text="Clear",width=10,command=clear)
clearBt.grid(row=7,column=4)



viewdb=Listbox(window,height=6,width=35)
viewdb.grid(row=3,column=1,rowspan=4,columnspan=2)

sc=Scrollbar(window)
sc.grid(row=3,column=3,rowspan=4)

viewdb.configure(yscrollcommand=sc.set)
viewdb.bind('<<ListboxSelect>>',get_selected_row)
sc.configure(command=viewdb.yview)




window.mainloop()
