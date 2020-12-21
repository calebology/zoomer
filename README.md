# zoomer
This script, with many caveats, will enter zoom meetings for you at a time/date which you can specify

# Caveats
- This script only works with the Zoom desktop application
- Zoom must be open in your primary display; pyautogui does not work on secondary displays
- You must be logged into Zoom; I would automate that process but the log-in behaviour with an organizational account (NTU) is too unpredictable
  - The script will not activate until you are logged in (there is a while loop checking for the presence of the "Join" button on the Zoom homepage)

# Dependencies
- meetings.csv - You have to input all zoom meetings in a specific date/time format
- pyautogui
- Windows Task Scheduler - You have to create a new instance of a scheduled task so the script runs on startup and persists in the background. Make sure it's the main.pyw file so that the command prompt doesn't open when the script runs.
