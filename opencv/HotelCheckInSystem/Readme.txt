#Python application ~ Hotel Check In system Readme v1.0

# Author: Kaushal Shastry
# Email: kaushal.shastry@outlook.com // kaushal19.shastry@gmail.com
# LinkedIn: www.linkedin.com/in/kaushal-shastry/
# PayPal: kaushal.shastry@outlook.com
#-----------------------------------------------------------------------------------------------------------------------


This application can be used for check ins in hotels as an interactive kiosk, which reduces waiting times, queue formation and cost in the reception area.

Used pycharm to build, test and run the application on MacOS 15.1 (24B83)
Application will run in any python IDE as long as the supported libraries and binaries are installed 
Refer to qrcodeScanner.py ~ https://github.com/kaushal1904/projects/blob/main/opencv/qrcodeScanner/Readme.txt for detailed description of similar code 

Application has to be connected to a database for guest details verification.
Pycharm supports a wide range of DBMS, configure one that suits your needs. Packages and drivers may vary for different DMBS. 

Either create a DB manually or run a create query in the DBMS

Create a DB with the following columns:

  1. BookingID - varchar
  2. Name - varchar 
  3. Bookingdetails - varchar
  4. Mobile_number - bigint
  5. isCheckedIn - boolean


Add more columns if you want, make sure to tweak the code accordingly. 

Connect pycharm IDE to the DB by adding the following code (already added in hotelCheckIn.py) 

      conn = psycopg2.connect(database="$dbname",
                              host = "$hostname",
                              user="$username",
                              password="$password",
                              port="$portnumber")
      
      Replace $dbname, $hostname, $username, $password, $portnumber with your DB configuration values.


The qrcode scanner function cv2.QRCodeDetector() has a good recognition rate, make sure to use a decent camera with good lighting 
Built a few custom QR codes using https://www.the-qrcode-generator.com/  which worked with the application. Added a few QR codes to the sample QR codes folder

The QR codes that I use have two parameters/identifiers in the QR code; Name and BookingId, add more if you want and tweak the QR code recognition logic accordingly

After QR code recognition, logic queries the guest details from the database. The database has 5 columns add more if you want and adjust the business logic accordingly

The application uses speech recognition to make check in a hassle free experience. Speech recognition uses pocketsphinx package for user input, ambient noise might interfere with the user input
Recognition rate is decent, user is expected to respond only in monosyllable which works fine 


# Reach out via GitHub or Email for any communication
# Mentions and donations will be appreciated
