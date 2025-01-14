# Python application ~ 7up7down game Home_page.py v1.0
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

from nicegui import ui
from outcome_logic import random_die, player_bet

@ui.page('/home_page')

def home_page():
    ui.audio('Assets/Audio/casino-walk-around_bgm.mp3', autoplay=True).set_visibility(False)
    with ui.image('Assets/Images/casinobanner.jpg'):
        with ui.card().classes('fixed-center'):
            ui.image('Assets/Images/casinobannergif.webp').tailwind.border_radius('md')

            with ui.row():
                with ui.card() as sevendown:
                        sevendown.tailwind.background_color('red-700')
                        ui.image('Assets/Images/7num.jpg')
                        ui.icon('arrow_downward').tailwind.text_color('orange-300').font_size('3xl').align_self('center')
                        b1 = ui.button('Bet',icon='paid',color='purple-600',on_click = lambda : (ui.audio('Assets/Audio/bet.mp3',autoplay=True,loop=False).set_visibility(False),sevendown.tailwind.animation('bounce'),b1.props('disable'),player_bet('sevendown'),ui.notify('You bet on 7 down'),b2.props('disable'),b3.props('disable'),rd.props(remove='disable')))
                        b1.tailwind.align_self('center').text_color('orange-300')

                with ui.card() as sevenequal:
                    sevenequal.tailwind.background_color('red-700')
                    ui.image('Assets/Images/7num.jpg')
                    ui.icon('sync_alt').tailwind.text_color('orange-300').font_size('3xl').align_self('center')
                    b2 = ui.button('Bet', icon='paid', color='purple-600', on_click=lambda: (ui.audio('Assets/Audio/bet.mp3',autoplay=True,loop=False).set_visibility(False),sevenequal.tailwind.animation('bounce'),b2.props('disable'), player_bet('sevenequal'),ui.notify('You bet on 7'),b1.props('disable'),b3.props('disable'),rd.props(remove='disable')))
                    b2.tailwind.align_self('center').text_color('orange-300')

                with ui.card() as sevenup:
                    sevenup.tailwind.background_color('red-700')
                    ui.image('Assets/Images/7num.jpg')
                    ui.icon('arrow_upward').tailwind.text_color('orange-300').font_size('3xl').align_self('center')
                    b3 = ui.button('Bet', icon='paid', color='purple-600', on_click=lambda: (ui.audio('Assets/Audio/bet.mp3',autoplay=True,loop=False).set_visibility(False),sevenup.tailwind.animation('bounce'),b3.props('disable'), player_bet('sevenup'),ui.notify('You bet on 7 up'),b1.props('disable'),b2.props('disable'),rd.props(remove='disable')))
                    b3.tailwind.align_self('center').text_color('orange-300')

            rd = ui.button('Roll dice',color='purple-600',icon='casino',on_click = lambda :(random_die(),playagain(),rd.props('disable'),sevendown.tailwind.animation('none'),sevenup.tailwind.animation('none'),sevenequal.tailwind.animation('none'))).props('disable')

            rd.tailwind.align_self('center').text_color('orange-300')

            def playagain():
                pa = ui.button('Play again!', icon='sync', color='purple-600',
                                on_click=lambda: ui.navigate.to('home_page'))
                pa.tailwind.align_self('center').text_color('orange-300')

    ui.run()
home_page()



