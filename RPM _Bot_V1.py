#Made by Javier Diez
#http://github.com/Javier-Diez

import webbrowser #Library used to open Google Chrome.
import pyautogui #Library used to interact with the compputer.
import time #Library used to pause the program.
from subprocess import Popen #Library used to close the tabs so your RAM doesn't run out.

shorte_link_youtube = "http://corneey.com/wKXHJw" #Replace with your link.
shorte_link_google = "http://corneey.com/wKXHTm" #Replace with your link.
shorte_link_yahoo = "http://corneey.com/wKXHL6" #Replace with your link.
click_position_x = 1804 #To get the coordinates where you want all of your movements to happen type in console: "pyautogui.position()".
click_position_y = 154 #That will give you the postion of your mouse.

#Note that if you have a 1920x1080 display and Google Chrome you will not need to do the step above.

for i in range(20): #A loop just to repeat it

    webbrowser.open(shorte_link_youtube, new=2, autoraise=True) #Opens a tab and sets it to the front.
    pyautogui.moveTo(1901, 118, duration=2) #Moves to coordinates in 2 seconds.
    pyautogui.click(x=1901, y=118, clicks=1, button='left') #Left clicks the coordinates.

    time.sleep(20) #Pauses the program for 20 seconds.

    pyautogui.moveTo(click_position_x, click_position_y, duration=2) #Moves to coordinates in 2 seconds.
    pyautogui.click(x=click_position_x, y=click_position_y, clicks=1, button='left') #Left clicks the coordinates.

    time.sleep(3) #Pauses the program for 3 seconds.

    webbrowser.open(shorte_link_yahoo, new=2, autoraise=True) #Opens a tab and sets it to the front.

    time.sleep(20) #Pauses the program for 20 seconds.

    pyautogui.moveTo(click_position_x, click_position_y, duration=1) #Moves to coordinates in 2 seconds.
    pyautogui.click(x=click_position_x, y=click_position_y, clicks=1, button='left') #Left clicks the coordinates.

    time.sleep(3) #Pauses the program for 3 seconds.

    webbrowser.open(shorte_link_google, new=2, autoraise=True) #Opens a tab and sets it to the front.

    time.sleep(20) #Pauses the program for 20 seconds.

    pyautogui.moveTo(click_position_x, click_position_y, duration=1) #Moves to coordinates in 2 seconds.
    pyautogui.click(x=click_position_x, y=click_position_y, clicks=1, button='left') #Left clicks the coordinates.

    time.sleep(3) #Pauses the program for 3 seconds.

    Popen('taskkill /F /IM chrome.exe', shell=True) #Kills ALL Google Chrome tabs.

    time.sleep(5) #Pauses the program for 5 seconds.
