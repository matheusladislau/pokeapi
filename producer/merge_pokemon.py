# -*- coding: utf-8 -*-
import os
import json

#folder = 'D:\\PROJETOS\\vgc\\data\\pokemon\\'
#files = os.listdir(folder)

folder = os.getcwd()+"/data/pokemon/"
merged_file_name = "all_pokemon.json"

print("Current Directory is: ", folder)

files = os.listdir(folder)

c = 0
content = []
for i in range(len(files)):
    file = files[i]
    if(file!=merged_file_name):
        print('opening '+str(i+1)+" of "+str(len(files))+" "+folder+file)

        text = open(folder+file)
        content.append(json.load(text))

file_to_write = open(folder+merged_file_name, "w")
print('writing merged file '+merged_file_name)
json.dump(content, file_to_write, indent=4)
print('done')
