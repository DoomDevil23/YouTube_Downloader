from pytube import YouTube
from os import system, name
import sys

#ARRAY FOR MESSAGES
arr_msgs = [    #0                  1                                                                                                                                                                                                                            2                  3               4                       5           6           7               8               9           10                                                          11                      12
            ["By DoomDevil", "YouTube Downloader shows all possible format options a video from YouTube can be downloaded.\nVideos over 720p resolution have no audio.\nVideos and audios downloaded may need a format change to work on certain devices.", "Enter link: ", "Invalid link!", "Press >>Enter<< to finish", "Title", "Options", "Video and Audio", "Only Audio", "Only Video", "Enter selection (Enter number >>0<< to cancel download): ", "Succesful download!", "Aborted download!"],
            ["Por DoomDevil", "YouTube Downloader te muestra todas las opciones de formato para descargar un video de YouTube.\nLos videos con una resolución mayor a 720p vienen sin sonido.\nLos videos y audios que se descargan por separado pueden necesitar un cambio de formato antes de utilizarlos en ciertos dispositivos.", "Ingresa el link: ", "El link no existe o no es válido!", "Presiona >>Enter<< para terminar", "Nombre del Video", "Opciones", "Video y Audio", "Solo Audio", "Solo Video", "Ingresa el número (Ingresa el número >>0<< si no deseas descargar nada): ", "Descarga éxitosa!", "Descarga cancelada!"]
            ]

#METHODS
def read_ints(value):#method to validad the input is integer
    try:
        value = int(value)
        return True
    except Exception:
        print ("Error")
        #input (arr_msgs[lang][4])
        return False

def clear():#method to clear console
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#LANGUAGE SELECTION
print("1 - English")
print("2 - Español")
lang = input()
if(read_ints(lang)):#validating the input is an integer
    lang = int(lang)-1
    if(lang > 1 or lang < 0):#if the integer is out of the valid range the english language is set as default
        lang = 0
else:
    lang = 0
clear()

#MAIN WOPRKING CODE
#headers
print("YouTube Downloader 1.1".center(30, "*"))
print(arr_msgs[lang][0].center(30, "*"))
print()
print(arr_msgs[lang][1])
print()

#getting link and validating it
try:
    link = input(arr_msgs[lang][2])
    yt = YouTube(link)
except Exception:#if link is incorrect throws and exception and ends the program
    print(arr_msgs[lang][3])
    input(arr_msgs[lang][4])
    sys.exit()

print()

#PTINTING DOWNLOAD OPTIONS AND INFO
#Video Title
print("********",arr_msgs[lang][5],"********")
print(yt.title)
print()

#Progressive options
print("********",arr_msgs[lang][6],"********")
i =1
ls=[]
print()
print(arr_msgs[lang][7])
for sr in yt.streams:
    if(sr.is_progressive):
        print(i, " - ", sr.resolution, " - ", sr.mime_type, " - ", round(sr.filesize/1024/1024, 2), "mb")
        ls.append(sr.itag)
        i = i+1
print()

#Only audio options
print()
print(arr_msgs[lang][8])
for sr in yt.streams:
    if(sr.type == "audio"):
        print(i, " - ", sr.abr, " - ", sr.mime_type, " - ", round(sr.filesize/1024/1024, 2), "mb")
        ls.append(sr.itag)
        i = i+1
print()

#Only video options
print()
print(arr_msgs[lang][9])
for sr in yt.streams:
    if(sr.is_progressive==False and sr.type == "video" and (sr.resolution == "1080p" or sr.resolution == "1440p" or sr.resolution == "2160p")):
        print(i, " - ", sr.resolution, " - ", sr.mime_type, " - ", round(sr.filesize/1024/1024, 2), "mb")
        ls.append(sr.itag)
        i = i+1
print()

#ENTER AN INTEGER FOR SELECTION
op = input(arr_msgs[lang][10])
if(read_ints(op) and op!="0"):#validating the input is an integer and user doesnt want to abort download
    op=int(op)
    if(op < len(ls) and op > 0):#validating the integer is in valid range for given options
        ys = yt.streams.get_by_itag(ls[op-1])
        ys.download()
        print(arr_msgs[lang][11])
    input(arr_msgs[lang][4])
else:#showing messages when user aborts download
    print(arr_msgs[lang][12])
    input(arr_msgs[lang][4])