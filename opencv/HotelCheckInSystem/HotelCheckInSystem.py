# Python application ~ Hotel CheckIn System v1.0
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

import datetime                                                                                                         #Package used for date time operation
import psycopg2                                                                                                         #Package used for Postgres DB operations
import cv2                                                                                                              #Package used for cv2 utilities

#Importing a file containing the loader animation gif
from '$path_directory' import aniLoader                                                                                 #Replace '$path_directory' with your choice of path

conn = psycopg2.connect(database="postgres",                                                                            #Connecting to a database, readme for more details
                        host="localhost",
                        user="postgres",
                        password="pass",
                        port="5432")
cursor = conn.cursor()                                                                                                  #Cursor object pointed at the DB for sql query execution

#Predeclared texts that will be printed over the videostream
IntroText = 'Please walk toward the camera'
QRcodeScanloc = 'Scan the QR code here'
TryagainText = 'Please try again'

count = 0

wc = cv2.VideoCapture(0)                                                                                                #Intialize a video object for webcam stream
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')                     #Loading the required haar-cascade xml classifier file

cv2.namedWindow('Hotel CheckIn', cv2.WND_PROP_FULLSCREEN)                                                      #Display name for the window
cv2.setWindowProperty('Hotel CheckIn', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)                         #Displaying the window in fullscreen mode

detector = cv2.QRCodeDetector()                                                                                         #Object to detect the QR code

while True:
    ret, frame = wc.read()

    cv2.putText(frame, IntroText, [150, 50], cv2.QT_FONT_NORMAL, 2, (255, 0, 0), 2)

    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)                                       #Intialize a face object for facial detection

    isFace = np.size(faces)                                                                                             #Condition to check if faces are detected in the videostream

    if isFace:                                                                                                          #If faces exist in the videostream

        count = count + 1
        #print('person detected')

        IntroText = ''
        cv2.putText(frame, IntroText, [150, 50], cv2.QT_FONT_NORMAL, 2, (255, 0, 0), 2)

        cv2.putText(frame, QRcodeScanloc, [70, 275], cv2.QT_FONT_NORMAL, 1, (255, 0, 0), 1)

        cv2.rectangle(frame, [75, 300], [400, 600], (255, 0, 0), 5, cv2.LINE_AA)                                        #Draws a rectangle on the specified co-ordinates
        rect = cv2.rectangle(frame, [75, 300], [400, 600], (255, 0, 0), 5, cv2.LINE_AA)                                 #Rectangle object used for scanning the QR code


        cropped_image = frame[300:600, 75:400]                                                                          #Crop the image in specified co-ordinates

        if count > 50:                                                                                                  #Condition for displaying "Try again" text

            count = 0
            cv2.putText(frame, TryagainText, [400, 50], cv2.QT_FONT_NORMAL, 2, (255, 0, 0), 2)

            qrdata, bbox, _ = detector.detectAndDecode(cropped_image)                                                   #Detects and decodes the QR code

        #Added a few Sample QR codes in the SampleQRCodes folder covering 3 use cases

            if qrdata:                                                                                                  #Condition when QR code is decoded and detected

                str_qrdata = str(qrdata)

                if 'BookingId' in str_qrdata:                                                                           #Condition to check the validity of the QR code
                    #print('\nValid QR code')

                    now = datetime.datetime.now()                                                                       #Intialize a date time object
                    #now.time()
                    currentTime = now.time()

                    #Condition to verify if the current time is as per the hotel's check in time policy, set it as per your needs
                    if currentTime > datetime.time(12, 0, 00, 00000) and currentTime < datetime.time(23, 59,0 , 0000):

                        aniLoader.loader()                                                                              #Calling the loader animation

                        print('\nWould you like to check in? Select y to confirm or n to exit')                         #User input, confirmation for check in
                        confstatus = input()

                        if confstatus == 'y':                                                                           #Condition if user selects y and proceeds to check in
                            #print('guest confirmed')

                            print("\nGuest details:")
                            print(qrdata)

                            #Logic to parse guest data(BookingID) from the scanned QR code
                            sepdata = qrdata.split('\n')
                            dictBookingdata = eval(str(sepdata))

                            BookingIDsplit = (dictBookingdata[1].split(' '))
                            BookingID = BookingIDsplit[1]

                            view_BookingIDs = 'SELECT "BookingID" FROM public."HotelCheckIn"'                           #SQL query to view the BookingID column in the DB
                            cursor.execute(view_BookingIDs)                                                             #Executing the query
                            BIDs = str(cursor.fetchall())                                                               #Method to fetch the result of the query and save it in the object as a string

                            if BookingID in BIDs:                                                                       #Condition to check if BookingID exists in the database

                                view_sql = 'SELECT * FROM public."HotelCheckIn" WHERE "BookingID" = %s'                 #SQL query to view the data of the specified guest
                                cursor.execute(view_sql, (BookingID,))                                             #Executing the query
                                guest_details_crude = cursor.fetchone()                                                 #Method to fetch the result of the query and save it in the object

                                #Parsing the crude data from query result
                                GuestName = guest_details_crude[1]
                                BookingDetails = guest_details_crude[2]
                                checkedInStatus = guest_details_crude[4]

                                if checkedInStatus:                                                                     #Condition to check if guest has already checked in
                                    print("\nHello ",GuestName)
                                    print('\nYou have already checked in')
                                    continue

                                else:                                                                                   #Condition if guest has not yet checked in
                                    print("\nHello ",GuestName)
                                    print('\nWelcome to the continental. Enjoy your stay of ' + BookingDetails + '. You will find the elevator to your right.')

                                    isCheckedInTrue = True
                                    isCheckedInFalse = False

                                    cursor.execute('UPDATE public."HotelCheckIn" SET  "isCheckedIn"=%s Where "BookingID"=%s',   #SQL query to set the guest's checked in status
                                                   (isCheckedInTrue, BookingID))

                                    conn.commit()                                                                       #Commit method to permanently save the database


                                    print('\nSuccessfully checked in')
                                    continue

                                    # After Successfully checking in, the guest receives a digital key to their mobile number and email - reach out for customization as per your needs
                                    # Email: kaushal.shastry@outlook.com // kaushal19.shastry@gmail.com
                                    # LinkedIn: www.linkedin.com/in/kaushal-shastry/

                                continue

                            else:                                                                                       #If BookingID is not found in the database
                                print('\nBooking not found')
                                continue

                        if confstatus == 'n':                                                                           #Condition if user selects n and chooses to exit
                            continue

                        else:                                                                                           #Condition if user selects neither y nor n
                            print('\nPlease select either y or n. Rescan to check in')
                            continue

                    else:                                                                                               #Condition if current time is not as per hotel check in time policy
                        aniLoader.loader()                                                                              #Calling the loader animation gif
                        print('\nCheck Ins allowed only after 12 pm.')
                        continue

                else:                                                                                                   #Condition if guests scan an Invalid QR code
                    aniLoader.loader()                                                                                  #Calling the loader animation gif
                    print('\nInvalid QR code')
                    continue

    else:                                                                                                               #Condition if there are no faces/humans in the frame
        #print('System is free')
        displaytext = 'Please walk toward the camera'
        cv2.putText(frame, displaytext, [150, 50], cv2.QT_FONT_NORMAL, 2, (255, 0, 0), 2)

    cv2.imshow('Hotel CheckIn', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit()

cv2.destroyAllWindows()
