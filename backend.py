import sqlite3


class database():
	def __init__(self):
		self.conn=sqlite3.Connection('books2.db')
		self.cur=self.conn.cursor()
		self.cur.execute('Create table if not exists book(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Year INTEGER, ISBN INTEGER)')
		self.conn.commit()

	def insert(self,title,author,year,isbn):
		self.cur.execute('insert into book values(NULL,?,?,?,?)',(title,author,year,isbn))
		self.conn.commit()
	
	def search(self,title="",author="",year="",isbn=""):
		self.cur.execute('select * from book where title=? or author=? or year=? or isbn=?',(title,author,year,isbn))
		rows=cur.fetchall()
		return rows

	def delete(self,id):
		self.cur.execute('delete from book where id=?',(id,))
		self.conn.commit()

	def update(self,id,title,author,year,isbn):
		self.cur.execute('update book set title=?,author=?,year=?,isbn=? where id=?',(title,author,year,isbn,id))
		rows=cur.fetchall()
		self.conn.commit()
		return rows	


	def view(self):
		self.cur.execute('select * from book')
		rows=self.cur.fetchall()
		return rows

	def __del__(self):
		self.cur.close()	

