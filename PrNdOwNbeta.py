from __future__ import unicode_literals
import youtube_dl
import sys
import requests
from random import randint
##########################################
Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
yellow="\033[1;36m"
Red="\033[1;31m"
purple="\033[35m"
Light="\033[95m"
cyan="\033[96m"
stong="\033[39m"
unknown="\033[38;5;82m"
unknown2="\033[38;5;198m"
unknown3="\033[38;5;208m"
unknown4="\033[38;5;167m"
unknown5="\033[38;5;91m"
unknown6="\033[38;5;210m"
unknown7="\033[38;5;165m"
unknown8="\033[38;5;49m"
unknown9="\033[38;5;160m"
unknown10="\033[38;5;51m"
unknown11="\033[38;5;13m"
unknown12="\033[38;5;162m"
unknown13="\033[38;5;203m"
unknown14="\033[38;5;113m"
unknown15="\033[38;5;14m"
##########################################
## Random Colors Generator:
cor = ["\033[1;33m","\033[1;34m","\033[1;30m","\033[1;36m","\033[1;31m","\033[35m","\033[95m","\033[96m","\033[39m","\033[38;5;82m","\033[38;5;198m","\033[38;5;208m","\033[38;5;167m","\033[38;5;91m","\033[38;5;210m","\033[38;5;165m","\033[38;5;49m","\033[38;5;160m","\033[38;5;51m","\033[38;5;13m","\033[38;5;162m","\033[38;5;203m","\033[38;5;113m","\033[38;5;14m"]
colors = cor[randint(0,15)]
colors2 = cor[randint(0,15)]
colors3 = cor[randint(0,15)]
colors4 = cor[randint(0,15)]
colors5 = cor[randint(0,15)]
colors6 = cor[randint(0,15)]
colors7 = cor[randint(0,15)]
colors8 = cor[randint(0,15)]
###########################

print("              "+unknown+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("              "+unknown2+"MMMMMMMMMMNKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("              "+unknown3+"MMMMMMMMMNc.dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("              "+unknown4+"MMMMMMMMWd. .kWMMMMMMMMMMMMMMMMMMMMMMW0KMMMMMMMMMM")
print("              "+unknown15+"MMMMMMMMk:;. 'OMMMMMMMMMMMMMMMMMMMMMWx.,0MMMMMMMMM")
print("              "+unknown14+"MMMMMMMK:ok.  ,0MMMMMMMMMMMMMMMMMMMWO. .cXMMMMMMMM")
print("              "+unknown13+"MMMMMMNl:KO.   ;KWNXK00O0000KXNWMMWO' .c;dWMMMMMMM")
print("              "+unknown12+"MMMMMMx,xNk.    .;'...    ....';:l:.  ,0l,0MMMMMMM")
print("              "+unknown11+"MMMMMK;,l;. .,:cc:;.                  .dx,lWMMMMMM")
print("              "+unknown10+"MMMMWo    ,dKWMMMMWXk:.      .cdkOOxo,. ...OMMMMMM")
print("              "+unknown5+"MMMM0'   cXMMWKxood0WWk.   .lkONMMNOOXO,   lWMMMMM")
print("              "+unknown2+"MMMWl   ;XMMNo.    .lXWd. .dWk;;dd;;kWM0'  '0MMMMM")
print("              "+unknown9+"kxko.   lWMMO.      .kMO. .OMMK;  .kMMMNc   oWMMMM")
print("              "+unknown8+"X0k:.   ;KMMXc      :XWo  .dW0c,lo;;xNMK,   'xkkk0")
print("              "+unknown10+"kko'     :KMMNkl::lkNNd.   .dkdKWMNOkXO,    .lOKNW")
print("              "+unknown15+"0Kk:.     .lOXWMMWN0d,       'lxO0Oko;.     .ckkOO")
print("              "+unknown4+"kkkdodo;.    .,;;;'.  .:ooc.     .        ...ck0XN")
print("              "+unknown8+"0XWMMMMWKxc'.          ;dxc.          .,cxKK0OkkOO")
print("              "+unknown+"MMMMMMMMMMMN0d:'.  .'        .l'  .;lxKWMMMMMMMMMN")
print("              "+unknown2+"MMMMMMMMMMMMMMMN0xo0O:,;;;;;;xN0xOXWMMMMMMMMMMMMMM")
print("              "+unknown14+"MMMMMMMMMMMMMMMMMMMMMMWWWWWMMMMMMMMMMMMMMMMMMMMMMM")
print("              "+unknown6+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("              "+unknown7+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("              "+unknown8+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("              "+unknown9+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("              "+Blue+"                   "+unknown2+"["+unknown14+"PrNdOwN"+unknown5+"]"+unknown+"         ")
print("     "+purple+"                       "+unknown13+"["+unknown10+"Created By Do0pH2ck"+unknown2+"]"+unknown10+"    "+Reset+"\n")
master = {
    'Audio': {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    },
    'Video': {
        'format': 'bestvideo+bestaudio/best',
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
            #'preferredquality': '137',
        }]
    },
    'list': {
        'listsubtitles': True
    },
    'listformat': {
        'lisformats': True
    }
}


def net(url):
    """
    check if the user has connected to the internet.
    """
    try:
        requests.get(url)
    except requests.exceptions.ConnectionError:
        print(colors + "[!] Please check your network connection.")
        return False
    except requests.exceptions.Timeout:
        print(colors + "[!!!] Site is taking too long to load, TimeOut.")
        return False
    except requests.exceptions.TooManyRedirects:
        print(colors + "[*] Too many Redirects.")
        return False
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print(e)
        sys.exit(1)
    return True


def check(link):
    """
    checking the validity of the link.
    """
    try:
        requests.get(link)
        return True
    except requests.exceptions.ConnectionError:
        print(colors + "[!] disconnected from network.")
        return False
    except requests.exceptions.HTTPError as err:
        print(err)
        return False


def download(link, data):
    try:
        with youtube_dl.YoutubeDL(data) as ydl:
            ydl.download([link])
    except youtube_dl.utils.DownloadError as err:
        print(err)


def main():
    ch = 'Y'
    if net("https://www.pornhub.com/"):
        if ch == 'Y':
            link = input(colors + "["+colors3+"*"+colors4+"]" + colors2 + " Enter the link: ")
            if check(link):
                print(colors5 + "[*] 1.Download an Audio playlist")
                print(colors6 + "[*] 2.Download a Video playlist")
                print(colors7 + "[*] 3.Download a Single Audio")
                print(colors8 + "[*] 4.Download a single video file")
                ch = int(input(colors + "["+Green+"------------Enter your choice------------"+colors5+"]: "))
                if ch in [1, 2, 3, 4]:
                    if ch == 1:
                        master['Audio']['noplaylist'] = False
                        download(link, master['Audio'])
                    elif ch == 2:
                        master['Video']['noplaylist'] = False
                        download(link, master['Video'])
                    elif ch == 4:
                        download(link, master['Video'])
                    else:
                        download(link, master['Audio'])
                else:
                    print("[!] Bad choice")
                ch = str(input(unknown15 + "[*] do you want to continue?(Y/n)"))


if __name__ == "__main__":
    main()

################

#Made For Fun
#################
