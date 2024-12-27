#Python application that performs CRUD operations on a DB Readme v1.1

# Author: Kaushal Shastry
# Email: kaushal.shastry@outlook.com // kaushal19.shastry@gmail.com
# LinkedIn: www.linkedin.com/in/kaushal-shastry/
# PayPal: kaushal.shastry@outlook.com
#-----------------------------------------------------------------------------------------------------------------------


Used pycharm to build, test and run the application on MacOS 15.1
Application will run in any python IDE as long as the supported packages and binaries are installed 

Used a Postgres DB for CRUD operations. Pycharm supports a wide range of DBMS, configure one that suits your needs. Packages and drivers may vary for different DMBS. 

Either create a DB manually or run a create query in the DBMS

Create a DB with the following columns:
  1. ID - varchar
  2. Name - text 
  3. Mobile_number - bigint
  4. isValidated - boolean

Add more columns if you want, make sure to tweak the code accordingly. 

Connect pycharm IDE to the DB by adding the following code (already added in DB_CRUD_operations.py): 

      conn = psycopg2.connect(database="$dbname",
                              host = "$hostname",
                              user="$username",
                              password="$password",
                              port="$portnumber")
      
      Replace $dbname, $hostname, $username, $password, $portnumber with your DB configuration values.

The code is accompanied with detailed comments for novice programmers 

This application can be used in any software that needs a database to store, retrieve and update data. Make sure queries and the db are as per required. 


# Reach out via GitHub or Email for any communication
# Mentions and donations will be appreciated
