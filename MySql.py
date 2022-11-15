import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  password = "password"
)
print("done")
print(mydb)


curser = mydb.cursor()

# curser.execute("create database testme")
curser.execute("show databases")

for x in curser:
  print(x)


mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  password = "password",
  database = 'customer_data'
)

my_cursor = mydb.cursor()
my_cursor.execute("show databases")

for x in my_cursor:
  print(x)

my_cursor.execute("drop table  if exists customers")
my_cursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
my_cursor = mydb.cursor()
my_cursor.execute("show tables")
for x in my_cursor:
  print(x)
sql = "insert into customers (name, address) values (%s, %s)"
values = [
  ("sampath", "Medagoda"),
  ("sampath", "Medagoda"),
  ("sampath", "Medagoda"),
  ("sampath", "Medagoda"),
  ("sampath", "Medagoda")]

# my_cursor.execute(sql, values)
my_cursor.executemany(sql, values)
mydb.commit()
print(my_cursor.rowcount)


# ___________________________________________
my_cursor.execute("select * from customers")
result2 = my_cursor.fetchall()

for d in result2 :
  print(d)

my_cursor.execute("select * from customers")
result = my_cursor.fetchmany(3)
print("----------------------------------------------")
for a in result:
  print(a)
