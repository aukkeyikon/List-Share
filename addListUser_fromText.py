# coding: UTF-8
import tweepy
import settings
import os
import sys

api = settings.api
myinfo = api.me()

os.chdir('./screen_name')

print("Type the old list name")
oldlistname=input()

#ディレクトリ内にoldlistname+".txt"のファイルがあるか調べる
if not os.path.isfile('./' + oldlistname + '.txt') :
    #ないなら、IDにディレクトリ移動、ファイルがあるか調べる
    os.chdir('../ID')
    if not os.path.isfile('./' + oldlistname + '.txt') :
        #そこでもファイルがなければエラーメッセージ(getListUserAll.pyを実行してくれ)を返して処理を終了
        print("Please exe 'getListUserAll.py'")
        sys.exit()
    else:
        #ファイルがあればそれを読み込んでconvertの処理
        data = open(oldlistname+'.txt')
        IDs = data.readlines()
        data.close()

        os.chdir('../screen_name')
        output = open(oldlistname+'.txt', 'w')

        for ID in IDs:
            try:
                user=api.get_user(ID)
                output.write(user.screen_name+'\n')
            except:
                print('User'+ID+'は存在しません')
        output.close()

print("Type new list name")
newlistname=input()

print("Choose type 'make new list' or 'add to some list' ? (make/add)")
flag=input()

if(flag == 'make'):
    try:
        api.create_list(name=newlistname,mode="private",description="by Tweepy")
        print("create new list!")
    except:
        print("This list has already been prepared. /n Add this list? (Y/n)")
        makelist=input()
        if(makelist == 'n'):
            sys.exit()

f = open(oldlistname+'.txt')
users =f.readlines()
f.close()

for i in users:
    #行末の改行文字を取り除く
    username=i.rstrip("\n")
    try:
        api.add_list_member(screen_name=username, slug=newlistname, owner_screen_name=myinfo.screen_name)
    except:
        print(username+'　に　ゃ　ー　ん　')
