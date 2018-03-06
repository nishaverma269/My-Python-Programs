import pyodbc 
import csv

def main():
                  # *******  Part 1: Getting values from csv file *******
  # Variables
  firstName = [] 
  lastName = []
  address = []
  phone = []
  email = []
  uid = []
  
  csvData = open("Program_1/data.csv", newline='')  #Open file
  reader = csv.reader(csvData)    #Read data from file
  for row in reader:   #Retreiving data from file
    firstName.append(row[0])
    lastName.append(row[1])
    address.append(row[2])
    phone.append(row[3])
    email.append(row[4])
    uid.append(row[5])
  
                 # *******  Part 2: Inserting values into database *******
  server = 'KJAIT2017\SQLEXPRESS' 
  database = 'AddressBook' 
  username = 'sa' 
  password = 'KJAit2017' 
  # Connecting database with above information
  conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
  # Creating a cursor
  cursor = conn.cursor()
  # Executing cursor to insert values in database table
  for i in range(len(firstName)):
    cursor.execute("INSERT Personnel (FirstName, LastName, Address, Phone, Email, Id) VALUES (?, ?, ?, ?, ?, ?)", firstName[i], lastName[i], address[i], phone[i], email[i], uid[i])
  print("Record Inserted")
  # Make sure data is committed to the database
  conn.commit()
  # Close database connection
  conn.close()

if __name__ == "__main__":
    main()

# Resources:
# 1. https://docs.python.org/3/library/csv.html
# 2. https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc
# 3. https://www.pythonanywhere.com/forums/topic/5433/
# 4. https://stackoverflow.com/questions/20199569/pyodbc-insert-into-sql
# 5. https://stackoverflow.com/questions/16150984/inserting-variable-as-sql-value-in-python
