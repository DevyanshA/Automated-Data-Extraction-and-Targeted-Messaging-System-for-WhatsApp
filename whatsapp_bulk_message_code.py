# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 12:53:49 2024

@author: DELL
"""

import keyboard as k
import pyautogui
import time
import pandas as pd
import webbrowser as web
from urllib.parse import quote

def send_whatsapp(data_file_excel,message_file_text,x_cord=864,y_cord=966):
    df = pd.read_excel(data_file_excel,dtype={"Contact":str})
    name = df['Name'].values
    contact = df['Contact'].values
    files = message_file_text
    
    with open (files) as f:
        file_data = f.read()
    zipped = zip(name, contact)
    
    counter = 0
    
    for (a, b) in zipped:
        msg = file_data.format(a)
        
        web.open(f"https://web.whatsapp.com/send?phone={b}&text={quote(msg)}")
        
        time.sleep(15)
        pyautogui.click(x_cord, y_cord)
        time.sleep(2)
        k.press_and_release('enter')
        time.sleep(2)
        
        k.press_and_release('ctrl+w')
        time.sleep(1)
        counter+=1
        
        