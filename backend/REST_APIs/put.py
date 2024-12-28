#Python application ~ GUI based API requests || PUT request put.py v1.0
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

import confirm_box                                                        #file that has custom-built confirm box for parsing API requests' response


#PUT request body

#The PUT method requests that the enclosed entity be stored under the supplied URI.
#If the URI refers to an already existing resource, it is modified and if the URI does not point to an existing resource, then the server can create the resource with that URI.

def put_request(base_url):
    print("\nInside PUT request func")
    put_request_title = "PUT request Successful!"

    try:

        #method that calls PUT request on the server, you might have to add or remove '/put' depending upon how the server is configured to respond to the requests
        #adjust the params and data accordingly

        put_response = requests.put(base_url+'/put', params={'id': 1}, data={"name": "qwe123"})
        print(put_response.status_code)                                                                                 #prints the status code of the response, 200 usually means response was successful
        put_response_messageBody = put_response.json()                                                                  #parses the response body into json format

        if put_response.status_code == 200:
            print('PUT request successful')

            userconfirm = confirm_box.resp_body(put_request_title,put_response.status_code,put_response.elapsed,put_response_messageBody)       #displays the response body in a pop-up via a function

            if userconfirm == 'Retry':
                put_request(base_url)
                return

            else:
                return

        else:
            print('API failed!')
            print('Status Code:',   put_response.status_code )

    except Exception as e:

        print('\nException Caught')
        print(e)

        confresp = pyautogui.confirm(title='Error', text=
        '                                   API Failed! \nPlease retry or check the url and internet connection',
                                     buttons=['Retry', 'Main Menu'])

        if confresp == 'Retry':
            put_request(base_url)
            return

        if confresp == 'Main Menu':
            return

        else:
            print('\nUser closed the PUT request Error pop-up')                             #prints the user action, can be used for event driven analytics
            return
