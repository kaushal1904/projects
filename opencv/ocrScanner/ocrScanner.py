# Python application ~ OCR scanner v1.0
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

import cv2                                                                             #Opencv package
import pytesseract                                                                     #OCR package for character recognition

pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

scan_text_loc = "Scan text here"

wc = cv2.VideoCapture(0)                                                               #intialize a video object for webcam stream

#fullscreens the webcam stream
cv2.namedWindow('OCR', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('OCR', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    ret, frame = wc.read()
    frame = cv2.resize(frame, (1920, 1080))

    cv2.rectangle(frame, [75, 300], [800, 600], (255, 0, 0), 5, cv2.LINE_AA)
    rect = cv2.rectangle(frame, [75, 300], [800, 600], (255, 0, 0), 5, cv2.LINE_AA)

    cv2.putText(frame, scan_text_loc, [320, 275], cv2.QT_FONT_NORMAL, 1, (255, 0, 0), 1)

    #[y:y + h, x:x + w]  formula to crop the image in specified co-ordinates
    cropped_image = frame[300:600, 75:800]


    text = pytesseract.image_to_string(cropped_image,lang='eng')                         #Recognizes the text in the specified area
    print(text)                                                                          #Prints the recognized text


    cv2.namedWindow('OCR', cv2.WINDOW_FULLSCREEN)
    cv2.imshow('OCR', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
