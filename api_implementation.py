# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 18:15:38 2022

@author: User
"""


import json
import requests


url = 'http://127.0.0.1:8000/products_prediction'

input_data_for_model = {
    
    'product_name' : 'Dell Inspiron 15 3511 Laptop',
  
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)

 