import mytube as mt 
import os
import pyglet
from pytube.helpers import safe_filename

def line(char='█'):
	print(char*100)






def getSize(ss):
    fsize= ss/1000000
    return round(fsize,2)
    
line()
text= input("Enter Video Name:- ")
line()
videos= mt.search_youtube(text)
line()
for i in range(len(videos)):
	print('(',(i+1),') [',videos[i].duration,'] ',videos[i].title)

line()
indexText= input("Enter Video index:- ")
line()
index= int(indexText)
index-=1

v= videos[index]
print("Downloading ",v.title)
line()

link= v.url

ress= mt.getAllStreams(link)

# for r in ress:
#     print(r.mime_type)
#     print(r.resolution)
#     print(r.type)

print('Available type and resolution')
line()

types= set()
for r in ress:
    types.add(r.type)

for type in types:
    print(type)
    line()
    for i in range(len(ress)):
        r= ress[i]
        if(r.type==type):
            print('(',(i+1),') ',r.mime_type,' ',r.resolution,'  ',getSize(r.filesize),'MB')
    line('=')

rit= input("Enter index:- ")
ri= int(rit)
r= ress[ri-1]











print("FileSize:- ",getSize(r.filesize),'MB')

fpath=""
if(r.type=='video'):
    mt.downloadV(r)
    fpath= str(os.path.join('Videos',safe_filename(videos[index].title)))+'.'+ress[ri-1].subtype
else:
    mt.downloadM(r)
    fpath= str(os.path.join('Musics',safe_filename(videos[index].title)))+'.'+ress[ri-1].subtype

line("_")
sPlay= input("Do you want to play is (y/n)")
if(sPlay=='y'):
    song= pyglet.resource.media(fpath,streaming=False)
    song.play()
    pyglet.app.run()



print("-------------See You---------------")
line('^')

