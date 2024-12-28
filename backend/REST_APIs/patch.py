#Python application ~ GUI based API requests || PATCH request patch.py v1.0
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

#PATCH request body

#PATCH is used for modify capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource.

def patch_request(base_url):
    print("\nInside PATCH request func")
    patchrequest_title = "PATCH request Successful!"

    try:

        #method that calls PUT request on the server, you might have to add or remove '/patch' depending upon how the server is configured to respond to the requests
        #adjust the params and data accordingly

        patch_response = requests.patch(base_url+'/patch', data={"name": "qwe123"})
        print(patch_response.status_code)                                                                               #prints the status code of the response, 200 usually means response was successful
        post_response_messageBody = patch_response.json()                                                               #parses the response body into json format


        if patch_response.status_code == 200:
            #post_response_sc = 0
            print('PATCH request successful')

            userconfirm = confirm_box.resp_body(patchrequest_title,patch_response.status_code,patch_response.elapsed,post_response_messageBody)     #displays the response body in a pop-up via a function

            if userconfirm == 'Retry':
                patch_request(base_url)
                return

            else:
                return

        else:
            print('API failed!')
            print('Status Code:',   patch_response.status_code )


    except Exception as e:

        print('\nException Caught')
        print(e)


        confresp = pyautogui.confirm(title='Error', text=
        '                                   API Failed! \nPlease retry or check the url and internet connection',
                                     buttons=['Retry', 'Main Menu'])

        if confresp == 'Retry':
            patch_request(base_url)
            return

        if confresp == 'Main Menu':
            return

        else:
            print('\nUser closed the PATCH request Error pop-up')                                 #prints the user action, can be used for event driven analytics
            return
