# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 17:01:23 2022

@author: User
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import difflib
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd


app = FastAPI()
origins = [
  

    "http://localhost",
    "http://localhost:3000",
    "http://localhost:4000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    
    product_name: str
        
        
# loading the saved model
products_model = pickle.load(open('products_model.sav', 'rb'))
list_of_all_titles = pickle.load(open('list_of_all_titles.sav', 'rb'))
product_data = pickle.load(open('product_data.sav', 'rb'))

@app.post('/products_prediction')
def products_predd(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    prod = input_dictionary['product_name']
   
   
    
 
    input_list = prod
    
    
    find_close_match = difflib.get_close_matches(input_list, list_of_all_titles)

    close_match = find_close_match[0]

    index_of_the_product = product_data[product_data.name == close_match]['index'].values[0]

    similarity_score = list(enumerate(products_model[index_of_the_product]))

    sorted_similar_products = sorted(similarity_score, key = lambda x:x[1], reverse = True) 

    print('products suggested for you : \n')
  
    list1=[]
    i = 1

    for movie in sorted_similar_products:
        index = movie[0]
        title_from_index = product_data[product_data.index==index]['_id'].values[0]
        if (i<6):
            d = product_data[product_data.index ==index].to_dict(orient='record')
            list1.extend(d)
            print(i, '.',title_from_index)
        
            i+=1
    
    return list1
            
    
   # prediction = diabetes_model.predict([input_list])
    
  #  if (prediction[0] == 0):
    #    return 'The person is not diabetic'
 #   else:
   
    
    
