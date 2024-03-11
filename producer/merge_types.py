# -*- coding: utf-8 -*-
import os
import json

#folder = 'D:\\PROJETOS\\vgc\\data\\types\\'
#files = os.listdir(folder)
merged_file_name = "all_types.json"
folder = os.getcwd()+"/data/types/"
print("Current Directory is: ", folder)
files = os.listdir(folder)

c = 0
content = []
for i in range(len(files)):
    file = files[i]
    print('opening '+str(i+1)+" of "+str(len(files))+" "+folder+file)

    if(file!="unknown.json" and file!='shadow.json'):
        text = open(folder+file)
        content.append(json.load(text))

file_to_write = open(folder+merged_file_name, "w")
print('writing merged file '+merged_file_name)
json.dump(content, file_to_write, indent=4)
print('done')
