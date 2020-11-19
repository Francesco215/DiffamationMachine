#To use this file put in the folder of the DataExport of Telegram and run it
#To change the target just change the identifier


import json
from shutil import copy2
import os

identifier=4867533164

with open("result.json","r") as read_file:
    data=json.load(read_file)

#Given the name or the id it returs the otherone
def find(x):
    for contact in data['frequent_contacts']['list']:
        if contact['id']==x: return contact['name']
        if contact['name']==x: return contact['id']

#Return a list of the path of the files of the audios sent
def extract_audio(identifier,name,json):
    files=[]
    for chat in data['chats']['list']:
        if chat['id']==identifier:
            for message in chat['messages']:
                if ("media_type" in message) and message['from_id']==identifier and message["media_type"]=="voice_message":
                    files.append(message["file"])
        if chat['type']=='private_group':
            for membri in chat['messages'][0]['members']:
                if membri==name:
                    for message in chat['messages']:
                        if ("media_type" in message) and message['from']==name and message["media_type"]=="voice_message":
                            files.append(message["file"])
                        
    return files           

name=find(identifier)
files=extract_audio(identifier,name,"result.json")


newpath = 'new_folder' 
if not os.path.exists(newpath):
    os.makedirs(newpath)
for file in files:
    copy2(file,'new_folder/')