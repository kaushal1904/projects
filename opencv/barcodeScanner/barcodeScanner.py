# Python application ~ Bar-code scanner v1.1
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


import cv2                                          #opencv library
from gtts import gTTS, gTTSError                    #TTS library, needs internet connection
from playsound3 import playsound                    #Audio player library
import os                                           #Library used to remove the generated audio clip
from pyzbar.pyzbar import decode                    #library to scan a barcode
import time                                         #time library to control the execution of the application


success_text = "Barcode successfully scanned"       #TTS text, confirmation text to be played as audio
bc_scan_text_loc = "Scan the barcode here"          #Text for the Location of the scanner

wc = cv2.VideoCapture(0)                            #intialize a video object for webcam stream

cv2.namedWindow('Barcode Scanner', cv2.WND_PROP_FULLSCREEN)                                 #display name for the window
cv2.setWindowProperty('Barcode Scanner', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)    #displaying the window in fullscreen mode


while True:
    ret, frame = wc.read()                          #reads the webcam stream 
    frame = cv2.resize(frame, (1920, 1080))         #resizes the webcam stream to a specified resolution 


    cv2.rectangle(frame, [75, 300], [800, 600], (255, 0, 0), 5, cv2.LINE_AA)            #draws a rectangle on the specified co-ordinates
    rect = cv2.rectangle(frame, [75, 300], [800, 600], (255, 0, 0), 5, cv2.LINE_AA)     #rectangle object used for scanning the bar-code

    cv2.putText(frame, bc_scan_text_loc, [250, 275], cv2.QT_FONT_NORMAL, 1, (255, 0, 0), 1)   #draws the text on the specified co-ordinates

    #[y:y + h, x:x + w]  formula to crop the image in specified co-ordinates
    cropped_image = frame[300:600, 75:800]

    gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)              #converts the specified area into gray scale image for easier detection
    barcode = decode(gray)                                              #decodes the barcode data

    if barcode:

        #print(barcode)           #prints the crude data read from the barcode
        
        print('\nBarcode Scanned!')                                         #success text

        # ---- TTS needs internet connection ----------
        try:                                                                #wrapping a try block to catch exception during no internet
            TTS_obj = gTTS(text=success_text, slow=False)                   #TTS object creation
            TTS_obj.save('success_text.mp3')                                #saves the TTS as an mp3 file
            playsound("success_text.mp3")                                   #plays the TTS mp3 file
            os.remove("success_text.mp3")                                   #deletes the TTS mp3 file


        except gTTSError as e:                                              #Exception block to parse the caught exception
            print('\nTTS needs internet connection')                        #prints when exception is raised
            continue


        finally:                                                           #Finally block to execute the code irrespective of the try/except block

            #takes a screenshot of the frame when barcode is detected
            cv2.imwrite("$save_path/$filename.jpg", frame)                 #replace $save_path with your choice of path and $filename.jpg with your choice of filename
            
            for barcode in barcode:                                        #parsing barcode crude data
                barcode_data = barcode.data.decode("utf-8")                #saves the barcode data in an object
                barcode_type = barcode.type                                #saves the barcode type in an object

            print('\nBarcode Data:', barcode_data)                           #prints the barcode data
            print('Barcode Type:',barcode_type)                            #prints the barcode type
            time.sleep(1)                                                  #pauses the execution of the application for the desired amount of sec


    cv2.namedWindow('Barcode Scanner', cv2.WINDOW_FULLSCREEN)              #names the window and displays it in fullscreen
    cv2.imshow('Barcode Scanner', frame)                                   #displays the objects; webcam stream and the objects drawn over it

    if cv2.waitKey(1) & 0xFF == ord('q'):                                  #condition(q key) to exit from the application
        break                                                              #breaks out from the while loop and closes the application
