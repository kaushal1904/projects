#Python application ~ GUI based API requests || POST request post.py v1.0
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

import confirm_box                                                  #file that has custom-built confirm box for parsing API requests' response


#POST request body

#POST request method requests that a web server accepts the data enclosed in the body of the request message,
#most likely for storing it. It is often used when uploading a file or when submitting a completed web form.

def post_request(base_url):
    print("\nInside POST request func")
    postrequest_title = "POST request Successful!"

    try:

        #method that calls POST request on the server, you might have to add or remove '/post' depending upon how the server is configured to respond to the requests
        #adjust the params and data accordingly

        post_response = requests.post(base_url+'/post', params={"ads":"123"},data={"name": "qwe123"})
        print(post_response.status_code)                                                                                #prints the status code of the response, 200 usually means response was successful
        post_response_messageBody = post_response.json()                                                                #parses the response body into json format

        if post_response.status_code == 200:

            print('POST request successful')

            userconfirm = confirm_box.resp_body(postrequest_title,post_response.status_code,post_response.elapsed,post_response_messageBody)        #displays the response body in a pop-up via a function

            if userconfirm == 'Retry':
                post_request(base_url)
                return

            else:
                return

        else:
            print('API failed!')
            print('Status Code:',   post_response.status_code )


    except Exception as e:

        print('\nException Caught')
        print(e)

        confresp = pyautogui.confirm(title='Error', text=
        '                                   API Failed! \nPlease retry or check the url and internet connection',
                                     buttons=['Retry', 'Main Menu'])

        if confresp == 'Retry':
            post_request(base_url)
            return

        if confresp == 'Main Menu':
            return

        else:
            print('\nUser closed the POST request Error pop-up')                     #prints the user action, can be used for event driven analytics
            return
