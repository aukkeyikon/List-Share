import tweepy
import settings
import os

if not os.path.isdir('./ID'):
    os.mkdir('./ID')
if not os.path.isdir('./screen_name'):
    os.mkdir('./screen_name')

api = settings.api
print("type owner's screen name")
owner_screen_name=input()
print("type the list name")
listname=input()
print("Choose type id or screen_name")
typ=input()

if typ == 'id':
    os.chdir('./ID')
else:
    os.chdir('./screen_name')
fout = open(listname +".txt", "w")

for user in tweepy.Cursor(api.list_members, owner_screen_name, listname).items():
    if typ == 'id':
        fout.writelines(user.id_str+ "\n")
    else:
        fout.writelines(user.screen_name+ "\n")
fout.close()
print("Finished!")
