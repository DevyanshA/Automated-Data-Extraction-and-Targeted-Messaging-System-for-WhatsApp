# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 18:21:17 2024

@author: DELL
"""

import pandas as pd
import pywhatkit

def send_whatsapp_message(data_file_excel):
    
    df = pd.read_excel(data_file_excel,dtype={"Contact":str})
    
    phone_number = df['Contact'].values
    
    # with open (files) as f:
    #     file_data = f.read()
    # zipped = zip(name, contact)
    
    # counter = 0
    zipped = zip(phone_number)
    counter=0
    i=1
    for (i) in zipped(phone_number):
        
        
        pywhatkit.sendwhatmsg("a","test meassege for bulk send", h, m )
        
        counter+=1
        i+=1
 

       

