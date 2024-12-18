# Custom processing animation function for Python application ~ Hotel CheckIn System v1.1
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

import cv2
playedNumber = 0

def processing():
  
    wc = cv2.VideoCapture('$save_path/loader.gif')                               #Replace $save_path with your choice of path
    #added the loader.gif file to the opencv/HotelCheckInSystem/Resources
    
    cv2.namedWindow('Processing...', cv2.WND_PROP_FULLSCREEN)
    count = 0
    
    global close
    close = False
    global playedNumber

    while True and close == False:
        ret, frame = wc.read()
        bigger = cv2.resize(frame, (300, 300))
        cv2.moveWindow("Processing...", 600, 200)

        cv2.imshow('Processing...', bigger)
        count = count + 1

        if count == 106:
            count = 0
            playedNumber +=1
            #print(playedNumber)
            processing()

        if playedNumber == 1 :
            playedNumber= 0
            close = True
            cv2.destroyWindow('Processing...')
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            exit()
            close = True
