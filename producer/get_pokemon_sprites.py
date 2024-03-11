# -*- coding: utf-8 -*-
import requests
import json

# change index to start downloading from a certain id
start_index = 1024
# last id to be downloaded
last_poke_index = 1025
url_main_type =  'https://pokeapi.co/api/v2/pokemon/'
relative_path = "data"

file_extesions_to_download = [".png",".svg",".ogg"]

def get_response(url):
    try:
        response = requests.get(url)
    except:
        response=('erro')
    return response

# define info based on url file
def define_file(url, extension):
    file = ""
    if('sprites' in url):
        subject = "sprites"
    else:
        subject = "cries"

    url_split = url.split('/')
    last_occurence=len(url_split)-url_split[::-1].index(subject)-1
    #print(url_split[last_occurence:])

    folder = url_split[last_occurence:][0]

    for k in url_split[last_occurence+1:]:
        file = file + k +"_"

    filename = relative_path+"/"+folder+"/"+file[:-1]

    return filename


# main
for i in range(last_poke_index+1):
    if(i> start_index):
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

            pokemon_text_split  = pokemon.text.split('"')
            for i in pokemon_text_split:
                for j in file_extesions_to_download:
                    if(j in i):
                        filename = define_file(i,j)
                        print('downloading '+i+' into '+filename)

                        img_data = requests.get(i).content
                        with open(filename, 'wb') as handler:
                            handler.write(img_data)
            print()
        #quit()
print('done.')
