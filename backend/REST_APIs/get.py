#Python application ~ GUI based API requests || GET request get.py v1.0
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

import pyautogui
import requests

import confirm_box                                                     #file that has custom-built confirm box for parsing API requests' response


#GET request body

#The GET method is used to retrieve information from the given server using a given URL. The GET method sends the encoded user information appended to the page request

def get_request(base_url):
    print("\nInside GET request func")
    getrequest_title = "GET request Successful!"

    try:

        #method that calls GET request on the server, you might have to add/remove '/get' depending upon how the server is configured to respond to the requests

        get_response = requests.get(base_url+'/get')
        print(get_response.status_code)                                                                                 #prints the status code of the response, 200 usually means response was successful
        get_response_messageBody = get_response.json()                                                                  #parses the response body into json format

        if get_response.status_code == 200:

            print('GET request successful')

            userconfirm = confirm_box.resp_body(getrequest_title,get_response.status_code,get_response.elapsed,get_response_messageBody)        #displays the response body in a pop-up via a function

            if userconfirm == 'Retry':
                get_request(base_url)
                return

            else:
                return

        else:
            print('API failed!')
            print('Status Code:',   get_request.status_code )

    except Exception as e:

        print('\nException Caught')
        print(e)

        confresp = pyautogui.confirm(title='Error', text=
        '                                   API Failed! \nPlease retry or check the url and internet connection',
                                     buttons=['Retry', 'Main Menu'])

        if confresp == 'Retry':
            get_request(base_url)
            return

        if confresp == 'Main Menu':
            return

        else:
            print('\nUser closed the GET request Error pop-up')                                 #prints the user action, can be used for event driven analytics
            return
