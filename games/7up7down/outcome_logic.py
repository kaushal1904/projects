# Python application ~ 7up7down game outcome_logic.py v1.0
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

import random
from nicegui import ui


global playerbet
global gameoutcome

jp_img = 'Assets/Images/jackpotgif.webp'
big_win_img = 'Assets/Images/wingif.webp'
loss_img = 'Assets/Images/lostgif.gif'

def seven_outcome(die):
    if die <7:
        gameoutcome = 'sevendown'
        print('less than 7')
        print(playerbet,gameoutcome)

        if gameoutcome == playerbet:
            sevendown_win_music = ui.audio(
                'Assets/Audio/bigwin.mp3', autoplay=True,
                loop=False).set_visibility(False)

            dialog_win()

        else:
            sevendown_lost_music = ui.audio('Assets/Audio/lost.mp3', autoplay=True,loop=False).set_visibility(False)
            dialog_loss()


    if die == 7:
        gameoutcome = 'sevenequal'
        print('equal 7')
        print(playerbet, gameoutcome)

        if gameoutcome == playerbet:
            jackpot_music = ui.audio('Assets/Audio/jackpotwin.mp3',autoplay=True,loop=False).set_visibility(False)

            dialog_jack_win()

        else:
            sevenequal_lost_music = ui.audio('Assets/Audio/lost.mp3', autoplay=True,loop=False).set_visibility(False)
            dialog_loss()

    if die > 7:
        gameoutcome = 'sevenup'
        print('greater than 7')
        print(playerbet, gameoutcome)

        if gameoutcome == playerbet:

            sevenup_win_music = ui.audio('Assets/Audio/bigwin.mp3',autoplay=True,loop=False).set_visibility(False)

            dialog_win()

        else:
            sevenup_lost_music = ui.audio('Assets/Audio/lost.mp3', autoplay=True,
                                             loop=False).set_visibility(False)
            dialog_loss()

def random_die():
    out1 = random.choice([1,2,3,4,5,6])
    out2 = random.choice([1,2,3,4,5,6])

    print(out1,out2)
    seven_outcome(out1+out2)

def player_bet(plabet):
    global playerbet
    playerbet = plabet


def dialog_win():
    with ui.dialog() as wdialog, ui.card().style('width: 400px;background-color: #fdba74'):
        wdialog.tailwind.text_color('orange-300').font_size('3xl').background_color('orange-300')
        ui.image(big_win_img)
        paw = ui.button('Play again!',icon='sync',color='purple-600', on_click=lambda: ui.navigate.to('home_page'))
        paw.tailwind.align_self('center').text_color('orange-300')
    wdialog.open()

def dialog_jack_win():
    with ui.dialog() as wdialog, ui.card().style('width: 400px;background-color: #fdba74'):
        wdialog.tailwind.text_color('orange-300').font_size('3xl').background_color('orange-300')
        ui.image(jp_img)
        paw = ui.button('Play again!',icon='sync',color='purple-600', on_click=lambda: ui.navigate.to('home_page'))
        paw.tailwind.align_self('center').text_color('orange-300')
    wdialog.open()

def dialog_loss():
    with ui.dialog() as ldialog, ui.card().style('width: 400px;background-color: maroon'):
        ldialog.tailwind.text_color('orange-300').font_size('3xl').background_color('red-400')
        ui.image(loss_img)
        pal = ui.button('Play again!',icon='sync',color='purple-600', on_click=lambda: ui.navigate.to('home_page'))
        pal.tailwind.align_self('center').text_color('orange-300')
    ldialog.open()


