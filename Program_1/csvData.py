import pyodbc 
import csv

def main():
                  # *******  Part 1: Getting values from csv file *******

  csvData = open("Program_1/ArrestData.csv", newline='')  #Open file
  reader = csv.reader(csvData)    #Read data from file

                 # *******  Part 2: Inserting values into database *******
  server = 'KJAIT2017\SQLEXPRESS' 
  database = 'AddressBook' 
  username = 'sa' 
  password = 'KJAit2017' 
  # Connecting database with above information
  conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
  # Creating a cursor
  cursor = conn.cursor()
  # # Executing cursor to insert values in database table
  i=0
  for row in reader:   #Retreiving data from file
   cursor.execute("INSERT ArrestData (_id, PK, CCR, AGE, GENDER, RACE, ARRESTTIME, ARRESTLOCATION, OFFENSES, INCIDENTLOCATION, INCIDENTNEIGHBORHOOD, INCIDENTZONE, INCIDENTTRACT, COUNCIL_DISTRICT, PUBLIC_WORKS_DIVISION, X, Y) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16])
   conn.commit()
   print("Record inserted "+str(i))
   i=i+1
  # Make sure data is committed to the database
 
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
