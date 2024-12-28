#Python application ~ GUI based REST API requests v1.0
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

import get                                                                     #file that has GET request code
import post                                                                    #file that has POST request code
import put                                                                     #file that has PUT request code
import delete                                                                  #file that has DELETE request code
import patch                                                                   #file that has PATCH request code

import requests                                                                #package used for API requests
import pyautogui                                                               #package used for GUI application

global status_code
status_code = 0

base_url = "https://httpbin.org/"                                               #base_url on which API requests are called, you can change it to a different url make sure to tweak the API requests accordingly


#health-check function body for the base url

def base_url_healthCheck(base_url_str):
    print('\nVerifying base URL .../' , base_url_str)

    global status_code
    while status_code != 200:

        try:
            base_url_req = requests.get(base_url_str)
            status_code = base_url_req.status_code
            print(f"Base URL is up with status code:", str(status_code))

        except Exception as e:

            print("\nConnection Error! ")
            alertresp = pyautogui.confirm(
                '                         Connection Error! \nPlease check the internet connection and the base URL.',
                buttons=['Retry', 'Close'])
            baseurl_str = ''


            if alertresp == 'Retry':
                print('\nin retry', baseurl_str)
                base_url_healthCheck(base_url)
                return

            if alertresp == 'Close':
                exit(0)

            else:
                print('\nUser closed the connection error pop-up')         #prints the user action, can be used for event driven analytics
                return

        return

base_url_healthCheck(base_url)                                             #function verifying health of the base url


#GUI based menu for API requests

while True:
    user_input = pyautogui.confirm('\nPlease select either of the following API requests\n',
                      'API Requests',
                      buttons=['GET request', 'POST request','PUT request','DELETE request','PATCH request','Close'])

    if user_input == 'GET request':

        get.get_request(base_url)
        continue

    if user_input == 'POST request':

        post.post_request(base_url)
        continue

    if user_input == 'PUT request':

        put.put_request(base_url)
        continue

    if user_input == 'DELETE request':

        delete.delete_request(base_url)
        continue

    if user_input == 'PATCH request':

        patch.patch_request(base_url)
        continue

    if user_input == 'Close':

        confresp = pyautogui.confirm(title='Confirmation', text='Are you sure you want to exit?', buttons = ['Yes','Back'])
        if confresp == 'Yes':
            print('\nExiting the application /..')
            print('User exited')                                                    #prints the user action, can be used for event driven analytics
            exit(0)

        if confresp == 'Back':
            continue

        else:
            print('\nUser closed the exit confirmation pop-up')                     #prints the user action, can be used for event driven analytics
            continue

    else:
        print('\nUser closed the main menu')                                        #prints the user action, can be used for event driven analytics
        exit(0)
