#Python application that performs CRUD operations on a DB v1.0
#-----------------------------------------------------------------------------------------------------------------------

# Readme file for more details
# Feel free to use the code
# Mentions and donations will be appreciated
# Reach out via GitHub or Email for any communication
#-----------------------------------------------------------------------------------------------------------------------

# Author: Kaushal Shastry
# Email: kaushal.shastry@outlook.com // kaushal19.shastry@gmail.com
# LinkedIn: www.linkedin.com/in/kaushal-shastry/
# PayPal: kaushal.shastry@outlook.com
#-----------------------------------------------------------------------------------------------------------------------

import psycopg2                                         #Package used for Postgres DB operations
import maskpass                                         #Package used for masking the password while typing
import re                                               #Package used for regex parsing

conn = psycopg2.connect(database="$dbname",             #DB object created for DB operations replace $dbname, $hostname, $username, $password and $portnumber with your DB configuration values
                        host="$hostname",
                        user="$username",
                        password="$password",
                        port="$portnumber")

cursor = conn.cursor()                                  #Cursor object pointed at the DB for sql query execution


while True:
    print("\n                                 || Main Menu ||")               #Main menu for the selection of CRUD operations

    print('\nEnter either of the following options')
    print("--------------------------------------")

    print('\nEnter 1 to VIEW the entire DB')
    print('Enter 2 to VIEW a specific User')
    print('Enter 3 to CREATE a new User')
    print('Enter 4 to UPDATE User\'s data')
    print('Enter 5 to DELETE a User (needs admin access)')
    print('Enter 6 to EXIT the application')
    user_sel = input()                                                        #Method to take user input


    # -----------          Viewing the entire DB               -----------

    if  user_sel == '1':                                                        #Option to view the entire DB

        cursor.execute('SELECT * FROM public."InviteesDb"')                     #SQL query to view the entire DB
        data = cursor.fetchall()                                                #Method to fetch the result of the query and save it in the object

        if not data:                                                            #If condition to check if DB is empty i.e the query result is null
            print('\n  || DB is empty! ||')

        else:                                                                   #Printing the result of the query
            print('\n  || Entire DB View || \n')                                #Prints the DB in a tabular view using for loop
            for row in data:
                print(row)


    # -----------          Viewing a specific User             -----------

    if user_sel == '2':                                                         #Option to view a specific user data in the DB

        cursor.execute('SELECT "ID" FROM public."InviteesDb"')                          #SQL query to view the ID column in the DB
        q_res = cursor.fetchall()                                                       #Method to fetch the result of the query and save it in the object
        str_q_res = str(q_res)                                                          #Convert the result of the query to a string

        if not q_res:                                                                   #If condition to check if DB is empty i.e the query result is null
            print('\n  || DB is empty! ||')
            continue

        while True:
                    print('\nEnter the User ID whose data you want to view or Select 0 to exit to the main menu')           #Asking for the User ID whose data you would like to view

                    user_ID = input()                                                                       #Method to take user input

                    cursor.execute('SELECT "ID" FROM public."InviteesDb"')                                  #SQL query to view the ID column in the DB
                    q_res = cursor.fetchall()                                                               #Method to fetch the result of the query and save it in the object
                    str_q_res = str(q_res)                                                                  #Convert the result of the query to a string


                    if user_ID == '0':                                                                      #If condition for exiting from User ID view operation
                        break

                    expectedformat_ID = re.search("ID[0-9][0-9][0-9]$", user_ID)                     #Regex to validate the expected format of User ID

                    try:
                       expectedformat_ID.group()                                                            #Wrapping a try block in-case of validation failure

                    except Exception as e:                                                                  #Exception block to catch an exception
                        print(' \n  || User ID should be in IDNNN format || ')                              #Prints in-case of an exception caught
                        continue


                    if user_ID in str_q_res:                                                                #If condition to check if User ID is in the DB

                        print("\n  || ID exists querying results ||\n")

                        view_sql = 'SELECT * FROM public."InviteesDb" WHERE "ID" = %s'                      #SQL query to view the data of the specified user
                        cursor.execute(view_sql, (user_ID,))                                           #Method to execute the query

                        data = cursor.fetchone()                                                            #Method to fetch the result of the query and save it in the object

                        if str_q_res:                                                                       #Condition to check if data exists in the result of the query
                            print(data)
                            continue

                    else:                                                                                   #Condition if User ID does not exist in the DB
                        print('\n  || User ID does not exist || ')
                        continue

        continue


    # -----------          Creating a new User                 -----------

    if user_sel == '3':                                                         #Option to create a new user in the DB

        while True:

            print('\nEnter the values separated by commas (IDNNN,name,mobile number,isValidated) or Select 0 to exit to the main menu')            #Asking user to enter details for the new user
            #sample user data would be ID001, firstuser, 987653123, true

            new_user = input()                                                                               #Method to take user input

            if new_user == '0':                                                                              #If condition for exiting from User ID create operation
                break

            else:
                new_user_val = new_user.split(',')                                                           #Splits the entered string by the specified separator ',' in this case

                expectedformat_ID = re.search("ID[0-9][0-9][0-9]$", new_user_val[0])                 #Regex to validate the expected format of User ID

                try:
                    expectedformat_ID.group()                                                                #Wrapping a try block in-case of validation failure

                except Exception as e:                                                                       #Exception block to catch an exception
                    print('\n  || User ID should be in IDNNN format ||\n')                                   #Prints in-case of an exception caught
                    continue

                if len(new_user_val) < 4:                                                                    #Condition to check if number of entered data elements is 4, exit and print invalid entry otherwise
                    print('\n  || INVALID ENTRY - Enter 4 values separated by commas (IDNNN,name,mobile number,isValidated) ||')
                    continue


                if  not new_user_val[1].isalpha():                                                           #Condition to check if name is alphabetic, exit and print correction message otherwise
                    print('\n  || Name should be a string ||\n')
                    continue

                if not new_user_val[2].isnumeric():                                                          #Condition to check if mobile number is numeric, exit and print correction message otherwise
                    print('\n  || Mobile number should be numeric ||\n')
                    continue

                if new_user_val[3].capitalize() != 'True' and new_user_val[3].capitalize() != 'False':       #Condition to check if isValidated parameter is either True or False, exit and print correction message otherwise
                    print('\n  || isValidated should be either True or False ||\n')
                    continue

                else:                                                                             #If all conditions are met asking user to confirm the data for the new user

                    print('\n  || Entered data for the new user is ||\n')
                    print(new_user_val)

                    print('\nType y to confirm DB entry')                                          #Confirmation message
                    usr_conf = input()                                                             #Method to take user input

                    if usr_conf == 'y':                                                            #Condition if user confirms the entered data
                        print('\nCreating the new user ../')

                        cursor.execute('SELECT "ID" FROM public."InviteesDb"')                     #SQL query to view the ID column in the DB
                        q_res = cursor.fetchall()                                                  #Method to fetch the result of the query and save it in the object
                        str_q_res = str(q_res)                                                     #Convert the result of the query to a string


                        if new_user_val[0] in str_q_res:                                           #Condition to check if User ID already exists in the DB
                            print("\n  || User ID already exists ||\n")                            #Prints incase it exists

                            view_sql = 'SELECT * FROM public."InviteesDb" WHERE "ID" = %s'         #SQL query to view the data of the already existing User
                            cursor.execute(view_sql, (new_user_val[0],))                      #Method to execute the query
                            print(cursor.fetchone())                                               #Prints the result of the query

                            continue

                        else:
                            cursor.execute(('INSERT INTO public."InviteesDb"("ID", "Name", "Mobile_number", "isValidated")'         #SQL query to insert the data for the new user to be created 
                                                'VALUES (%s,%s,%s,%s)'), (new_user_val[0], new_user_val[1], new_user_val[2], new_user_val[3]))

                            conn.commit()                                                                                           #Commit method to permanently save the DB
                            print('\n  || User created! ||\n')                                                                      #Success message


                            view_sql = 'SELECT * FROM public."InviteesDb" WHERE "ID" = %s'                                          #SQL query to view the newly created user
                            cursor.execute(view_sql, (new_user_val[0],))                                                       #Method to execute the query
                            print(cursor.fetchone())                                                                                #Prints the result of the query

                            continue

                    else:                                                                                                           #Condition if user decides to cancel the new user creation
                        print('\n  || DB entry cancelled ||\n')
        continue


    # -----------          Updating User's data                -----------

    if user_sel == '4':                                                     #Option to update user's data in the DB
        cursor.execute('SELECT "ID" FROM public."InviteesDb"')              #SQL query to view the ID column in the DB
        q_res = cursor.fetchall()                                           #Method to fetch the result of the query and save it in the object

        if not q_res:                                                       #If condition to check if DB is empty i.e the query result is null
            print('\n  || DB is empty! ||')

        else:                                                               #Condition if DB has data proceed with the update operation

            while True:
                print('\nEnter Id to update DB entry or Select 0 to exit to the main menu')             #Asking for the User ID whose data you would like to update
                user_ID = input()                                                                       #Method to take user input

                if user_ID == '0':                                                                      #If condition for exiting from User data update operation
                    break

                expectedformat_ID = re.search("ID[0-9][0-9][0-9]$", user_ID)                     #Regex to validate the expected format of User ID

                try:
                   expectedformat_ID.group()                                                            #Wrapping a try block in-case of validation failure

                except Exception as e:                                                                  #Exception block to catch an exception
                    print('\n  || User ID should be in IDNNN format ||')                                #Prints in-case of an exception caught
                    continue

                cursor.execute('SELECT "ID" FROM public."InviteesDb"')                                  #SQL query to view the ID column in the DB
                q_res = cursor.fetchall()                                                               #Method to fetch the result of the query and save it in the object
                str_q_res = str(q_res)                                                                  #Convert the result of the query to a string

                print("\n../ Querying the UserID: {0}".format(user_ID))

                if user_ID  in str_q_res:                                                               #Condition to check if User ID exists in the DB


                    print("\nExisting data of the user")                                                #Prints existing data
                    view_sql = 'SELECT * FROM public."InviteesDb" WHERE "ID" = %s'                      #SQL query to view the updated User ID's data
                    cursor.execute(view_sql, (user_ID,))                                           #Method to execute the query
                    print(cursor.fetchall())                                                            #Prints the result of the SQL query


                    while True:                                                                                        #Menu with specific options for updating user data
                        print("\nUpdating User ID:{0}  \n\nEnter either of the following options".format(user_ID))     #Prints the User ID being updated
                        print('----------------------------------------------')

                        print('\nEnter 1 to update the name')
                        print('Enter 2 to update the mobile number')
                        print('Enter 3 to update the isValidated')
                        print('Enter 4 to update all the columns')
                        print('Enter 5 to view the existing data')
                        print('Enter 6 to EXIT to the previous menu')

                        choice = input()                                                                      #Method to take user input

                        if choice == '6':                                                                     #Option to exit the user data update menu
                            break

                        if choice == '1':                                                                     #Option to update just the name of the User
                            while True:
                                print('\nEnter the new name or Enter 0 to exit to the previous menu')         #Asking for the new name to update or 0 to exit to the previous menu
                                new_name = input()                                                            #Method to take user input

                                if new_name == '0':                                                           #If condition for exiting from name update operation
                                    break

                                if not new_name.isalpha():                                                    #Condition to check if name is alphabetic, exit and print correction message otherwise
                                    print('\n  || Name should be a string || ')
                                    continue

                                if len(new_name) > 0:                                                                   #Condition to check if name is not empty, exit and print correction message otherwise
                                    cursor.execute('UPDATE public."InviteesDb" SET  "Name"=%s Where "ID"=%s',     #SQL query to update the User ID with the new name
                                               (new_name,  user_ID))
                                    conn.commit()                                                                       #Commit method to permanently save the DB

                                    print('\n  || Name updated successfully! || \n')                                    #Success message

                                    view_sql = 'SELECT * FROM public."InviteesDb" WHERE "ID" = %s'                      #SQL query to view the updated User ID's data
                                    cursor.execute(view_sql, (user_ID,))                                           #Method to execute the query
                                    print(cursor.fetchall())                                                            #Prints the result of the SQL query

                                    continue

                                else:                                                                                   #Condition if name entered is empty
                                    print('\n  || Name cannot be empty  || ')
                                    continue

                            continue

                        if choice == '2':                                                                       #Option to update just the mobile number of the User
                            while True:
                                print('\nEnter the new mobile number or Enter 0 to exit to the previous menu')  #Asking for the new mobile number to update or 0 to exit to the previous menu
                                new_mobile_number = input()                                                     #Method to take user input

                                if new_mobile_number == '0':                                                    #If condition for exiting from mobile number update operation
                                    break

                                if not new_mobile_number.isnumeric():                                           #Condition to check if mobile number is numeric, exit and print correction message otherwise
                                    print('\n  || Mobile number should be numeric || ')
                                    continue

                                if len(new_mobile_number) > 0:                                                  #Condition to check if mobile number is not empty, exit and print correction message otherwise
                                    cursor.execute('UPDATE public."InviteesDb" SET  "Mobile_number"=%s Where "ID"=%s',          #SQL query to update the User ID with the new mobile number
                                               (new_mobile_number, user_ID))
                                    conn.commit()                                                                                     #Commit method to permanently save the DB
                                    print('\n  || Mobile number updated successfully! || \n')                                         #Success message

                                    view_sql = 'SELECT * FROM public."InviteesDb" WHERE "ID" = %s'                                    #SQL query to view the updated User ID's data
                                    cursor.execute(view_sql, (user_ID,))                                                         #Method to execute the query
                                    print(cursor.fetchall())                                                                          #Prints the result of the SQL query

                                    continue

                                else:                                                                                                 #Condition if mobile number entered is empty
                                    print('\n  || Mobile number cannot be empty ||')
                                    continue

                            continue

                        if choice == '3':                                                                       #Option to update just the isValidated parameter of the User
                            while True:                                                                         #Menu to update isValidated parameter of the User
                                    print('\nPlease Enter 1 or 2 or 0')
                                    print('------------------------------------')

                                    print('\nEnter 1 to set isValidated to True')
                                    print('Enter 2 to set isValidated to False')
                                    print('Enter 0 to exit to the previous menu')
                                    isValidated = input()                                                       #Method to take user input

                                    isValidatedTrue = True                                                      #for setting isValidated parameter to True
                                    isValidatedFalse = False                                                    #for setting isValidated parameter to False

                                    if isValidated == '1':                                                      #Option to set the isValidated parameter to True

                                        cursor.execute('UPDATE public."InviteesDb" SET  "isValidated"=%s Where "ID"=%s',   #SQL query to update isValidated parameter to True
                                                            (isValidatedTrue, user_ID))
                                        conn.commit()                                                                             #Commit method to permanently save the DB

                                        print('\n  || isValidated is set to True || \n')                                          #Success message

                                        view_sql = 'SELECT * FROM public."InviteesDb" WHERE "ID" = %s'                            #SQL query to view the updated User ID's data
                                        cursor.execute(view_sql, (user_ID,))                                                 #Method to execute the query
                                        print(cursor.fetchall())                                                                  #Prints the result of the SQL query
                                        continue

                                    if isValidated == '2':                                                                         #Option to set the isValidated parameter to False

                                        cursor.execute('UPDATE public."InviteesDb" SET  "isValidated"=%s Where "ID"=%s',     #SQL query to update isValidated parameter to False
                                                            (isValidatedFalse, user_ID))
                                        conn.commit()                                                                              #Commit method to permanently save the DB

                                        print('\n  || isValidated is set to False || \n')                                          #Success message

                                        view_sql = 'SELECT * FROM public."InviteesDb" WHERE "ID" = %s'           #SQL query to view the updated User ID's data
                                        cursor.execute(view_sql, (user_ID,))                                #Method to execute the query
                                        print(cursor.fetchall())                                                 #Prints the result of the SQL query
                                        continue

                                    if isValidated == '0':                                                       #Option to exit to the previous menu
                                        print('exiting to the previous menu')
                                        break

                                    else:                                                                        #Condition for invalid selection apart from 1,2 or 0
                                        print('\n  || INVALID ENTRY || ')
                                        continue
                            continue

                        if choice == '4':                                                                        #Option to update all the values of the user
                            while True:
                                print('\nEnter the values for User ID:{0} all Columns separated by commas (name,mobile number,isValidated) or Enter 0 to exit to the previous menu'.format(user_ID)) #Asking for all values to update or 0 to exit to the previous menu

                                str_new = input()                                                               #Method to take user input
                                ind_str = str_new.split(',')                                                    #Splits the entered string by the specified separator ',' in this case

                                if str_new == '0':                                                              #If condition for exiting from User data update operation
                                    break

                                if len(ind_str) < 3:                                                            #Condition to check if number of entered data elements is 3, exit and print correction message otherwise
                                    print('\n  || INVALID ENTRY - Enter 3 values separated by commas (name,mobile number,isValidated) || ')
                                    continue

                                if not ind_str[0].isalpha():                                                    #Condition to check if name is alphabetic, exit and print correction message otherwise
                                    print('\n  || Name should be a string || ')
                                    continue

                                if not ind_str[1].isnumeric():                                                  #Condition to check if mobile number is numeric, exit and print correction message otherwise
                                    print('\n  || Mobile number should be numeric || ')
                                    continue

                                if ind_str[2].capitalize() != 'True' and ind_str[2].capitalize() != 'False':    #Condition to check if isValidated parameter is either True or False, exit and print correction message otherwise
                                    print('\n  || isValidated should be either True or False || ')
                                    continue

                                else:
                                    cursor.execute('UPDATE public."InviteesDb" SET  "Name" =%s, "Mobile_number"=%s, "isValidated"=%s Where "ID"=%s', #SQL query to update the User ID with the new name, new mobile number and isValidated parameter
                                                   (ind_str[0], ind_str[1],ind_str[2],user_ID))
                                    conn.commit()                                                                           #Commit method to permanently save the DB
                                    print('\n  ||Name, Mobile number and isValidated updated successfully! || \n')          #Success message

                                    view_sql = 'SELECT * FROM public."InviteesDb" WHERE "ID" = %s'                          #SQL query to view the updated User ID's data
                                    cursor.execute(view_sql, (user_ID,))                                               #Method to execute the query
                                    print(cursor.fetchall())                                                                #Prints the result of the SQL query

                                    continue

                            continue

                        if choice == '5':                                                                       #Option to view the current user's data
                            print('\nExisting data of the user:{0}'.format(user_ID))
                            view_sql = 'SELECT * FROM public."InviteesDb" WHERE "ID" = %s'                      #SQL query to view the updated User ID's data
                            cursor.execute(view_sql, (user_ID,))                                           #Method to execute the query
                            print(cursor.fetchall())                                                            #Prints the result of the SQL query
                            continue


                        else:
                            print('\n  || INVALID ENTRY || ')                                                   #Condition if invalid selection from the menu options
                            continue

                    continue

                else:                                                                                           #Condition if User ID is not in the DB
                    print('\n  || User ID does not exist || ')
                    continue

            continue


    # -----------          Deleting a User                     -----------
    if user_sel == '5':                                                                                       #Option to delete a user

        cursor.execute('SELECT "ID" FROM public."InviteesDb"')                                                #SQL query to view the ID column in the DB
        q_res = cursor.fetchall()                                                                             #Method to fetch the result of the query and save it in the object

        if not q_res:                                                                                         #If condition to check if DB is empty i.e the query result is null
            print('\n  || DB is empty! || ')
            continue

        while True:

            print("\nEnter admin password to proceed or Type exit to exit to the Main Menu")                  #Password verification to authorize delete operation limiting to only admins

            password = maskpass.askpass(prompt="\nPassword:", mask="*")                                       #Masking the password while being entered

            if password == 'pass':                                                                            #If condition Password verification

                if not q_res:                                                                                 #If condition to check if DB is empty i.e the query result is null
                    print('\n  || DB is empty! || ')
                    continue

                while True:
                    print('\nEnter the User ID to be deleted or Enter 0 to exit to the previous menu')        #If correct password ask the user for the User ID to be deleted

                    user_ID = input()                                                                         #Method to take user input

                    cursor.execute('SELECT "ID" FROM public."InviteesDb"')                                    #SQL query to view the ID column in the DB
                    q_res = cursor.fetchall()                                                                 #Method to fetch the result of the query and save it in the object
                    str_q_res = str(q_res)                                                                    #Convert the result of the query to a string

                    if not q_res:                                                                             #If condition to check if DB is empty i.e the query result is null
                        print('\n  || DB is empty! || ')
                        break

                    if user_ID =='0':                                                                         #If condition for exiting from User ID delete operation
                        break

                    expectedformat_ID = re.search("ID[0-9][0-9][0-9]$", user_ID)                      #Regex to validate the expected format of User ID

                    try:
                      expectedformat_ID.group()                                                               #Wrapping a try block in-case of validation failure

                    except Exception as e:                                                                    #Exception block to catch an exception
                        print('\n  || User ID should be in IDNNN format ||')                                  #Prints in-case of an exception caught
                        continue

                    if user_ID in str_q_res:                                                                  #If condition to check if User ID is in the DB

                        print('\nDeleting the user:', user_ID)
                        del_sql = 'DELETE FROM public."InviteesDb" WHERE "ID" = %s'                           #SQL query to delete the User ID
                        cursor.execute(del_sql, (user_ID,))                                              #Method to execute the query
                        conn.commit()                                                                         #Commit method to permanently save the DB

                        print('\n  || Updated DB || \n')                                                      #Printing the updated DB
                        cursor.execute('SELECT * FROM public."InviteesDb"')                                   #SQL query to view the entire database
                        data = cursor.fetchall()                                                              #Method to fetch the result of the query and save it in the object


                        if not data:                                                                          #If condition to check if DB is empty i.e the query result is null
                            print('\n  || DB is empty! ||')
                            continue

                        for row in data:                                                                      #Prints the DB in a tabular view using for loop
                            print(row)
                            continue

                    else:                                                                                     #Condition if User ID is not in the DB
                        print('\n  || User ID does not exist || ')
                        continue

            if password != 'pass' and password != 'exit':                                                     #Condition for incorrect password
                print('\n  || Incorrect password ||')
                continue

            if password == 'exit':                                                                            #Condition for exiting from User ID delete operation
                break

        continue


    # -----------          Exiting the application             -----------
    if user_sel == '6':                                                             #Option to exit the application
        break


    # -----------          Incase of other entry              -----------
    else:                                                                           #Condition if invalid selection from the menu options
        continue
