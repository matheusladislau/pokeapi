# -*- coding: utf-8 -*-
import requests
import json

last_poke_index = 1025
url_main_type =  'https://pokeapi.co/api/v2/pokemon/'
relative_path = "data/pokemon"

def get_response(url):
    try:
        response = requests.get(url)
    except:
        response=('erro')
    return response

# main
for i in range(last_poke_index+1):
    print('downloading '+str(i)+" of "+str(last_poke_index))

    pokemon = get_response(url_main_type+str(i))

    if(pokemon.text!="Not Found"):
        str_int = ""
        if(i<1000):
            str_int = str_int+"0"
        if(i<100):
            str_int = str_int+"0"
        if(i<10):
            str_int = str_int+"0"
        str_int=str_int+str(i)

        pokemon_json = json.loads(pokemon.text)
        data = pokemon_json

        filename = relative_path+"/pokemon_"+str_int+'.json'

        with open(filename, 'w') as f:
            json.dump(data, f)
