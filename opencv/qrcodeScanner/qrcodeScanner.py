# Python application ~ QR-code scanner v1.0
#-----------------------------------------------------------------------------------------------------------------------


# Readme file for more details
# Refer to barcodeScanner.py ~ https://github.com/kaushal1904/projects/blob/main/opencv/barcodeScanner/barcodeScanner.py for detailed description of similar code 
# Feel free to use the code
# Mentions and donations will be appreciated
# Reach out via GitHub or Email for any communication
#-----------------------------------------------------------------------------------------------------------------------

# Author: Kaushal Shastry
# Email: kaushal.shastry@outlook.com // kaushal19.shastry@gmail.com
# LinkedIn: www.linkedin.com/in/kaushal-shastry/
# PayPal: kaushal.shastry@outlook.com
#-----------------------------------------------------------------------------------------------------------------------


import time
import cv2
from gtts import gTTS, gTTSError
from playsound3 import playsound
import os

success_text = "QR code successfully scanned"
qr_scan_text_loc = "Scan the QR code here"

detector = cv2.QRCodeDetector()                         #object to detect the QR code

wc = cv2.VideoCapture(0)

cv2.namedWindow('QR code Scanner', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('QR code Scanner', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    ret, frame = wc.read()
    frame = cv2.resize(frame, (1920, 1080))

    cv2.rectangle(frame, [75, 300], [500, 700], (255, 0, 0), 5, cv2.LINE_AA)
    rect = cv2.rectangle(frame, [75, 300], [500, 700], (255, 0, 0), 5, cv2.LINE_AA)

    cv2.putText(frame, qr_scan_text_loc, [100, 275], cv2.QT_FONT_NORMAL, 1, (255, 0, 0), 1)

    # [y:y + h, x:x + w]  formula to crop the image in specified co-ordinates
    cropped_image = frame[300:700, 75:500]

    qrdata, bbox, _ = detector.detectAndDecode(cropped_image)               # detects and decodes the QR code


    if qrdata:

        print('\nQR code Scanned!')  # success text

        # ---- TTS needs internet connection ----------
        try:                                                                # wrapping a try block to catch exception during no internet
            TTS_obj = gTTS(text=success_text, slow=False)                   # TTS object creation
            TTS_obj.save('success_text.mp3')                                # saves the TTS as an mp3 file
            playsound("success_text.mp3")                                   # plays the TTS mp3 file
            os.remove("success_text.mp3")                                   # deletes the TTS mp3 file


        except gTTSError as e:                                              # Exception block to parse the caught exception
            print('\nTTS needs internet connection')                        # prints when exception is raised
            continue

        finally:                                                            # Finally block to execute the code irrespective of the try/except block
          
            # takes a screenshot of the frame when qrcode is detected
            cv2.imwrite("$save_path/$filename.jpg",frame)                   # replace $save_path with your choice of path and $filename.jpg with your choice of filename


            print("\nQR code data:")
            print(qrdata)
            time.sleep(1)                                                   # pauses the execution of the application for the desired amount of sec


    cv2.namedWindow('QR code Scanner', cv2.WINDOW_FULLSCREEN)
    cv2.imshow('QR code Scanner', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
