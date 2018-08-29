import mytube as mt 
import os
import pyglet
from pytube.helpers import safe_filename
import glob
import vlc


def getSize(ss):
    fsize= ss/1000000
    return round(fsize,2)

def is_downloaded(fname):
	fname= safe_filename(fname)
	for file in glob.glob('Videos/*.*'):
		li= file.rindex('.')
		name= file[7:li]
		if(name==fname):
			return file
	return "NO"
 



def playVideo(title, fpath):
	print("Playing",safe_filename(title))
	player = vlc.MediaPlayer(fpath)
	player.play()
	print("Playing")
	while True:
		pass

	

def download(v):
	link= v.url
	ress= mt.getAllStreams(link)
	audio_streams=[]
	for r_stream in ress:
		if(r_stream.type=='video'):
			audio_streams.append(r_stream)
	r= audio_streams[0]
	mt.downloadV(r)
	fpath= str(os.path.join('Videos',safe_filename(v.title)))+'.'+r.subtype
	playVideo(v.title, fpath)

  



text= input("Enter Video Name:- ")

videos= mt.search_youtube(text)

v= videos[0]

bolo= is_downloaded(v.title)
if(bolo=='NO'):
	print("Downloading ",v.title)
	download(v)
else:
	playVideo(v.title, bolo)




