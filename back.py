import sqlite3						#pip install db-sqlite3
from datetime import datetime		#pip install DateTime

dbase = sqlite3.connect('My_data.db') # Open a database File
cur = dbase.cursor()

real_date=datetime.now()
real_datemonth=int(real_date.strftime("%m"))
#print(real_datemonth,type(real_datemonth))
month_dict={1:'exp_jan',2:'exp_feb',3:'exp_mar',4:'exp_apr',5:'exp_may',6:'exp_jun',7:'exp_jul',8:'exp_aug',9:'exp_sep',10:'exp_oct',11:'exp_nov',12:'exp_dec'}
#print(month_dict)

month=month_dict[real_datemonth]					# in case you want to check the working of this code for next and upcomming months
previous_month=month_dict[real_datemonth-1]			# then just increment these index values by one (+1) everything should work just fine.
#print(month)


year=datetime.now().year


month_table='{}_{}'.format(month,year)


dbase.execute(''' CREATE TABLE IF NOT EXISTS '{}'(
		'ID' INTEGER NOT NULL,
		'Date' TEXT NOT NULL,
		'Title' TEXT NOT NULL,
		'Recived' INTEGER NOT NULL,
		'Spent' INTEGER NOT NULL,
		'Opening_Balance' INTEGER NOT NULL
		) '''.format(month_table))



def previous_bal():
	global previous_month,year
	v='{}_{}'.format(previous_month,year)
	#print(v)
	val = cur.execute('SELECT SUM(Recived),SUM(Opening_Balance),SUM(Spent) FROM {}'.format(v)).fetchone()
	#print(val)
	savE=val[0]+val[1]-val[2]
	#print(savE)
	return savE


def recived(date,title,amount):
	global month_table
	#print(month)

	try:
		last_row = cur.execute('select * from {}'.format(month_table)).fetchall()[-1][0]
	except IndexError:
		last_row=0

	dbase.execute(f''' INSERT INTO {month_table}
	        VALUES({last_row+1},'{date}','{title}',{amount},0,0
	        )
	''')

	dbase.commit()
	#dbase.close()


	'''print(date,title,amount)
	l=list()
	l=date.split("/")
	d=datetime.now()
	print(l,d)
	print(d.strftime("%m"))'''

def spent(date,title,amount):
	global month_table
	#print(month)

	try:
		last_row = cur.execute('select * from {}'.format(month_table)).fetchall()[-1][0]
	except IndexError:
		last_row=0

	dbase.execute(f''' INSERT INTO {month_table}
	        VALUES({last_row+1},'{date}','{title}',0,{amount},0
	        )
	''')

	dbase.commit()

def open_b(amount):
	global month_table
	#print(month)
	
	dbase.execute(f''' UPDATE {month_table}
		SET Opening_Balance={amount}
		WHERE ID= 1
	''')

	dbase.commit()

def bal():
	savE=0
	val = cur.execute('SELECT SUM(Recived),SUM(Opening_Balance),SUM(Spent) FROM {}'.format(month_table)).fetchone()
	#print(val)
	savE=val[0]+val[1]-val[2]
	return savE


try:
	last_row = cur.execute('select * from {}'.format(month_table)).fetchall()[-1][0]
except IndexError:
	last_row=0


try:
	#print(last_row)
	if last_row==0:
		dbase.execute(f'''INSERT INTO {month_table}
			VALUES(1,0,0,0,0,{previous_bal()})
			''')
		dbase.commit()
except sqlite3.OperationalError:
	dbase.execute(f'''INSERT INTO {month_table}
			VALUES(1,0,0,0,0,0)
			''')
	dbase.commit()