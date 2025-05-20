#create a CSV file to store student data (Rollno, Name, Marks).
#Obtain data from user and write five records into the file. Again open this CSV file to read its records and display them.

def write():
    import csv
    file = open("studata.csv","w")
    stuwriter = csv.writer(file)
    stuwriter.writerow(['Roll Number','Name','Marks'])

    for i in range(5):
        print("Student Record", i+1,":")
        rolln = int(input("Enter roll number: "))
        name = input("Enter name: ")
        mrks = float(input("Enter marks: "))
        studentrec = [rolln, name, mrks]
        stuwriter.writerow(studentrec)

    file.close()



def readagain():
    import csv
    file = open("studata.csv","r")
    studntreader = csv.reader(file)
    for recrd in studntreader:
        print(recrd)



write()
readagain()





