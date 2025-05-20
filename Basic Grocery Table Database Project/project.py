import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='store123',database='GeneralStore')
if conn.is_connected():
    print('Successfully Connected.')
c=conn.cursor()
print('Welcome to General Store Management System!')
print('1. Login.')
print('2. Exit.')
choice=int(input('Enter your choice: '))
if choice==1:
    user_name=input('Enter your User Name = ')
    password=input('Enter your Password = ')
    while user_name== 'generalstore' and password=='store123':
        print('\nConnected Successfully.\n')       
        print('This is a General Store.')
        print('1. Add customer details.')
        print('2. Add product details.')
        print('3. Add worker details.')
        print('4. See all customer details.')
        print('5. See all product details.')
        print('6. See all worker details.')
        print('7. See one customer details.')
        print('8. See one product details.')
        print('9. See one worker details.')
        print('10. Stock.')
        print('11. Exit.')
        choice=int(input('Enter the choice: '))
        if choice==1:
            cust_name=input('Enter the name: ')
            phone_no=int(input('Enter the phone number: '))
            sql_insert="insert into customer_details values("+str(phone_no)+",'"+(cust_name)+"')"
            c.execute(sql_insert)
            conn.commit()
            print('Data has been updated.')
        elif choice==2:
            product_name=input('Enter Product Name: ')
            product_cost=float(input('Enter the cost: '))
            sql_insert="insert into product_details values(""'"+(product_name)+"',"+str(product_cost)+")"
            c.execute(sql_insert)
            conn.commit()
            print('Data has been updated.')
        elif choice==3:
            worker_name=input('Enter the name: ')
            worker_work=input('Enter the work-designation: ')
            worker_age=int(input('Enter the age: '))
            worker_salary=float(input('Enter the salary: '))
            phone_no =int(input('Enter the phone number: '))
            sql_insert="insert into worker_details values(" "'"+(worker_name)+"'," "'"+(worker_work)+"',"+str(worker_age)+","+str(worker_salary)+","+str(phone_no)+ ")"
            c.execute(sql_insert)
            conn.commit()
            print('Data has been updated.')
        elif choice==4:
            t=conn.cursor()
            t.execute('select*from customer_details')
            record=t.fetchall()
            for i in record:
                print(i)      
        elif choice==5:
            t=conn.cursor()
            t.execute('select*from product_details')
            record=t.fetchall()
            for i in record:
                print(i)
        elif choice==6:
            t=conn.cursor()
            t.execute('select*from worker_details')
            record=t.fetchall()
            for i in record:
                print(i)       
        elif choice==7:
            a=input('Enter the name: ')
            t='select*from customer_details where cust_name=("{}")'.format(a)
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print(v)
        elif choice==8:
            a=input('Enter the product name: ')
            t='select*from product_details where product_name=("{}")'.format(a)
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print(v)            
        elif choice==9:
            a=input('Enter the name: ')
            t='select*from worker_details where worker_name=("{}")'.format(a)
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print(v)
        elif choice==10:
            print('***')
            f=open('test.txt','r')
            data=f.read()
            print(data)
            f.close()
            print('***')
        elif choice==11:
            exit()               
    else:
        print('Wrong password entered. Please try again.')          
if choice==2:
    exit()
   
         



                                        
                            
                            
                            
                            

