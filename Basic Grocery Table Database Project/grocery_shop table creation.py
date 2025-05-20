import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='store123',database='GeneralStore')
if conn.is_connected():
    print('Successfully Connected.')
c=conn.cursor()
c.execute('create table customer_details(phone_no int(13),cust_name varchar(25),cost float(10))')
print('Table created.')
c.execute('create table product_details(product_name varchar(25),product_cost float(10))')
print('Table created.')
c.execute('create table worker_details(worker_name varchar(25),worker_work varchar(10),worker_age int(3), worker_salary float(10),phone_no int(13))')
print('Table created.')
