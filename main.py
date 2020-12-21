import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime
from datetime import date
from password import passwd
import sys
import os


#### Navigating to the home page #####
def home_page():
    while True:
        home_button = pyautogui.locateCenterOnScreen(r"C:\Users\WeeKe\Desktop\Python Playground\Zoom Autojoiner\home_button_2.png", grayscale = True, confidence = 0.5)
        # Adding in fail safe to ensure that the user is logged inux
        print(home_button)
        if home_button == None:
            print("Please sign in first, then rerun the script!")
            # Restarts the script
            time.sleep(10)
            continue
        else:
            pyautogui.moveTo(home_button)
            pyautogui.click()
            break



def join_meeting(meet_id, pwd):
    time.sleep(5)
    subprocess.Popen(r'C:\Users\WeeKe\AppData\Roaming\Zoom\bin\zoom.exe')
    time.sleep(5)
    ###### Navigating to the home page ######
    home_page()
    time.sleep(3)
    ###### Navigating to the main join button ######
    main_join_button = pyautogui.locateCenterOnScreen(r"C:\Users\WeeKe\Desktop\Python Playground\Zoom Autojoiner\main_join_button.png", confidence = 0.7)
    pyautogui.moveTo(main_join_button)
    pyautogui.click(main_join_button)
    time.sleep(3)
    ###### Filling in the meeting ID ######
    meeting_id_field = pyautogui.locateCenterOnScreen(r"C:\Users\WeeKe\Desktop\Python Playground\Zoom Autojoiner\meeting_id_field.png", confidence = 0.7)
    pyautogui.moveTo(meeting_id_field)
    pyautogui.click()
    pyautogui.write(meet_id)
    pyautogui.press("enter")
    time.sleep(1)
    ####### Filling in the password #####
    password_field = pyautogui.locateCenterOnScreen(r"C:\Users\WeeKe\Desktop\Python Playground\Zoom Autojoiner\password_field.png")
    pyautogui.moveTo(password_field)
    pyautogui.click()
    pyautogui.write(pwd)
    pyautogui.press("enter")

###### Infinite loop to check if the current time matches any of the meetings in the CSV ######
while True:
    df = pd.read_csv("meetings.csv")
    date_now = date.today().strftime("%Y-%m-%d")
    time_now = datetime.today().time().strftime("%H:%M")
    if date_now in str(df["Date"]) and time_now in str(df["Time"]): 
        date_cond = df["Date"] == date_now
        time_cond = df["Time"] == time_now
        row = df[date_cond & time_cond]
        meeting_id = str(row.iloc[0,2]) # Parses through the filtered dataframe for the meeting id
        password = str(row.iloc[0,3]) # Parses through the filtered dataframe for the password
        join_meeting(meeting_id, password)
        print("Checked into meeting")
        time.sleep(60)


# Make it run on startup and persist in the background with Windows Task Scheduler




######## SIGNING INTO ZOOM ##########
######## Deprecated - Zoom's log-in behaviour with organizational accounts is too unpredictable ####
# def zoom_login():
#     sign_in_button = pyautogui.locateCenterOnScreen(r'C:\Users\WeeKe\Desktop\Python Playground\Zoom Autojoiner\sign_in_button.png', confidence = 0.7)
#     enter_pwd_button = pyautogui.locateCenterOnScreen(r'C:\Users\WeeKe\Desktop\Python Playground\Zoom Autojoiner\password_button.png', confidence = 0.7)
    
#     ## There are some issues with signing in: The NTU website opens in a separate chrome tab
#     if sign_in_button == None and enter_pwd_button != None:
#         # If zoom is directly on the sign-in screen
#         pyautogui.moveTo(sign_in_button)
#         pyautogui.click()
#         time.sleep(5)
#         enter_pwd_button = pyautogui.locateCenterOnScreen(r'C:\Users\WeeKe\Desktop\Python Playground\Zoom Autojoiner\password_button.png', confidence = 0.7)
#         print(enter_pwd_button)
#         pyautogui.moveTo(enter_pwd_button)
#         pyautogui.click()
#         pyautogui.write(passwd)
#         pyautogui.press("enter")
    

#     elif sign_in_button != None:
#         # If zoom still needs to be prompted by clicking "Sign In"
#         print("hello")

#     else:
#         pass
#         print("Rest of the code goes here")