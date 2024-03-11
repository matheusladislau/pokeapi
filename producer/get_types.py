# -*- coding: utf-8 -*-
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql import types as T
import requests
import json

# variveis
url_main_type =  'https://pokeapi.co/api/v2/type'

response = requests.get(url_main_type)
response_types_json = json.loads(response.text)

def get_type(url):
    try:
        response = requests.get(url)
    except:
        response=('erro')
    return response

for i in response_types_json['results']:
    name = i['name']
    #print(name)
    url  = url_main_type+"/"+name
    print('downloading type '+ name+". URL: "+url)

    type_poke = get_type(url)
    type_poke_json = json.loads(type_poke.text)
    data = type_poke_json

    with open('data/types/'+name+'.json', 'w') as f:
        json.dump(data, f)
