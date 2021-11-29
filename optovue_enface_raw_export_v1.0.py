"""
Steps:
The following steps are performed manually by the operator

1   Select patient session (1st volume should load automatically)
2   Open python script in IDLE, & run it

The remaining steps are performed automatically by the script

Script: OptoVue - Export of OCTA enface raw image files
Version: v1.0
Author: m4cd4r4 - Physiology & Pharmacology
Date: 26/11/2021
"""

import pyautogui
import time
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()
num_of_vols = simpledialog.askinteger(title="OptoVue EAW Image Export",
prompt="How many volumes in current session?")

vol_selection = 514  
save_location = ("C:\\Users\\svc_DigitalPhotograp\\Documents\\Python-Optovue_Export_Raw\\Exported_Images\\") 


for i in range(num_of_vols):

    pyautogui.click(x=103, y=vol_selection) # Click volume at these x,y pixel coordinates
    time.sleep(6.5)
    pyautogui.click(x=1850, y=108) # close quickvue
    time.sleep(.2)
    pyautogui.click(x=985, y=116) # Click "Export Angio"
    time.sleep(.4)
    pyautogui.click(x=1442, y=704) # Click into whitespace of "File name" text-box
    time.sleep(.05)
    pyautogui.press('home')
    time.sleep(.05)
    pyautogui.write(save_location)
    pyautogui.click(x=1419, y=774) # "Save" button
    vol_selection += 32 # y-axis pixels

tk.messagebox.showinfo('Complete')


