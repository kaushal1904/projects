#Python application ~ GUI based API requests || Confirmation box for response body confirm_box.py v1.0
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

import pyautogui                                                #package used for GUI application

#custom-built confirm box for parsing API requests' response

def resp_body(text,status_code,response_time,messageBody):

    rt_format = str(response_time).split(':')

    #displays the response body and the response time of the server. Response times are a good measure of server performance
    us_but = pyautogui.confirm(title=text, text='\nStatus  is: ' + str(status_code) +'\n\nResponse Body:\n '+str(messageBody) + '\n\nResponse time: ' + str(rt_format[2]) +' sec',buttons=['Main Menu','Retry'])

    if us_but == 'Main Menu':
        return

    if us_but == 'Retry':
        return 'Retry'

    else:
        print('\nUser closed the ' +str(text).split(' ')[0] + ' response body pop-up')                                 #prints the user action, can be used for event driven analytics
        return
