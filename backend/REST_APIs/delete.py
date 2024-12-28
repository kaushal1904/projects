#Python application ~ GUI based API requests || DELETE request delete.py v1.0
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


#DELETE request body

#The DELETE method deletes the specified resource. As with a PUT request, you need to specify a particular resource for this operation.

def delete_request(base_url):
    print("\nInside DELETE request func")
    delete_response_title = "DELETE request Successful!"

    try:

        #method that calls DELETE request on the server, you might have to add or remove '/delete' depending upon how the server is configured to respond to the requests
        #adjust the params and data accordingly

        delete_response = requests.delete(base_url+'/delete',params={"ads":"123"},data={"name": "qwe123"})
        print(delete_response.status_code)                                                                              #prints the status code of the response, 200 usually means response was successful
        delete_response_messageBody = delete_response.json()                                                            #parses the response body into json format

        if delete_response.status_code == 200:
            print('DELETE request successful')

            userconfirm = confirm_box.resp_body(delete_response_title,delete_response.status_code,delete_response.elapsed,delete_response_messageBody)     #displays the response body in a pop-up via a function

            if userconfirm == 'Retry':
                delete_request(base_url)
                return

            else:
                return

        else:
            print('API failed!')
            print('Status Code:',   delete_request.status_code )

    except Exception as e:

        print('\nException Caught')
        print(e)

        confresp = pyautogui.confirm(title='Error', text=
        '                                   API Failed! \nPlease retry or check the url and internet connection',
                                     buttons=['Retry', 'Main Menu'])

        if confresp == 'Retry':
            delete_request(base_url)
            return

        if confresp == 'Main Menu':
            return

        else:
            print('\nUser closed the DELETE request Error pop-up')                                 #prints the user action, can be used for event driven analytics
            return
