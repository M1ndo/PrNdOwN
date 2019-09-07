#!/usr/bin/env python3
# Created By ybenel
## Hd Video Downloader For PornHub Videos
## Don't Copy The Code Without Giving The Credits Nerd

from __future__ import unicode_literals
try:
    from time import sleep as sl
    import os,sys,requests
    import youtube_dl as dl
    from random import random,randint
    import validators as valid
except ImportError:
    print('['+'*'*20+']')
    print('Module [youtube-dl] Status: Not Found!')
    print('['+'*'*20+']')
    print('Please Install It Using [pip3 install youtube-dl]')
    print('['+'*'*20+']')
## Colors ##
Reset="\033[0m"
cor = ["\033[1;33m","\033[1;34m","\033[1;30m","\033[1;36m","\033[1;31m","\033[35m","\033[95m","\033[96m","\033[39m","\033[38;5;82m","\033[38;5;198m","\033[38;5;208m","\033[38;5;167m","\033[38;5;91m","\033[38;5;210m","\033[38;5;165m","\033[38;5;49m","\033[38;5;160m","\033[38;5;51m","\033[38;5;13m","\033[38;5;162m","\033[38;5;203m","\033[38;5;113m","\033[38;5;14m"]
colors = cor[randint(0,15)]
colors2 = cor[randint(0,15)]
colors4 = cor[randint(0,15)]
colors3 = cor[randint(0,15)]
colors4 = cor[randint(0,15)]
colors5 = cor[randint(0,15)]
colors6 = cor[randint(0,15)]
colors7 = cor[randint(0,15)]
colors8 = cor[randint(0,15)]
colors9 = cor[randint(0,15)]
##        ##
## Clear Function ####
def clear():
    clear = os.system('clear')
    return clear

def banner():
    print("              "+colors+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("              "+colors2+"MMMMMMMMMMNKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("              "+colors3+"MMMMMMMMMNc.dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("              "+colors4+"MMMMMMMMWd. .kWMMMMMMMMMMMMMMMMMMMMMMW0KMMMMMMMMMM")
    print("              "+colors5+"MMMMMMMMk:;. 'OMMMMMMMMMMMMMMMMMMMMMWx.,0MMMMMMMMM")
    print("              "+colors6+"MMMMMMMK:ok.  ,0MMMMMMMMMMMMMMMMMMMWO. .cXMMMMMMMM")
    print("              "+colors7+"MMMMMMNl:KO.   ;KWNXK00O0000KXNWMMWO' .c;dWMMMMMMM")
    print("              "+colors8+"MMMMMMx,xNk.    .;'...    ....';:l:.  ,0l,0MMMMMMM")
    print("              "+colors+"MMMMMK;,l;. .,:cc:;.                  .dx,lWMMMMMM")
    print("              "+colors2+"MMMMWo    ,dKWMMMMWXk:.      .cdkOOxo,. ...OMMMMMM")
    print("              "+colors3+"MMMM0'   cXMMWKxood0WWk.   .lkONMMNOOXO,   lWMMMMM")
    print("              "+colors4+"MMMWl   ;XMMNo.    .lXWd. .dWk;;dd;;kWM0'  '0MMMMM")
    print("              "+colors5+"kxko.   lWMMO.      .kMO. .OMMK;  .kMMMNc   oWMMMM")
    print("              "+colors6+"X0k:.   ;KMMXc      :XWo  .dW0c,lo;;xNMK,   'xkkk0")
    print("              "+colors7+"kko'     :KMMNkl::lkNNd.   .dkdKWMNOkXO,    .lOKNW")
    print("              "+colors8+"0Kk:.     .lOXWMMWN0d,       'lxO0Oko;.     .ckkOO")
    print("              "+colors+"kkkdodo;.    .,;;;'.  .:ooc.     .        ...ck0XN")
    print("              "+colors2+"0XWMMMMWKxc'.          ;dxc.          .,cxKK0OkkOO")
    print("              "+colors3+"MMMMMMMMMMMN0d:'.  .'        .l'  .;lxKWMMMMMMMMMN")
    print("              "+colors4+"MMMMMMMMMMMMMMMN0xo0O:,;;;;;;xN0xOXWMMMMMMMMMMMMMM")
    print("              "+colors5+"MMMMMMMMMMMMMMMMMMMMMMWWWWWMMMMMMMMMMMMMMMMMMMMMMM")
    print("              "+colors6+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("              "+colors7+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("              "+colors8+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("              "+colors+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("              "+colors+"                   "+colors2+"["+colors4+"Cryptz"+colors6+"]"+colors7+"         ")
    print("     "+colors3+"                      "+colors8+"["+colors3+"Created By ybenel"+colors5+"]"+colors4+"    "+Reset+"\n")

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
config = {
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

def download(link, data):
    try:
        with dl.YoutubeDL(data) as ydl:
            ydl.download([link])
    except dl.utils.DownloadError as err:
        print(err)

def get_info(link):
    ydl2 = dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
    with ydl2:
        result = ydl2.extract_info(link,download=False)
        if 'entries' in result:
            video = result['entries'][0]
        else:
            video = result
        video_title = video['title']
        video_url = video['url']
    return video_title


def main():
    clear()
    banner()
    check2='Y'
    if net('https://pornhub.com/'):
        if check2 == 'Y':
            link = input(colors + "["+colors3+"*"+colors4+"]" + colors2 + " Enter the link: " + colors9)
            if not valid.url(link):
                print("\n" + colors8 + "["+colors2+"!"+colors5+"]" + colors7 + " Unvalid Url!!!" + colors6)
                print(colors8 + "["+colors2+"!"+colors5+"]" + colors7 + " Please Try Again" + colors6)
                exit(1)
            if check(link):
                print(colors6 + "Title Video: " +colors+ "{}".format(get_info(link)))
                print(colors5 + "[*] 1.Download an Audio playlist")
                print(colors3 + "[*] 2.Download a Video playlist")
                print(colors7 + "[*] 3.Download a Single Audio")
                print(colors8 + "[*] 4.Download a single video file")
                check2 = int(input(colors + "["+colors4+"------------Enter your choice------------"+colors5+"]: "))
                if check2 in [1, 2, 3, 4]:
                    if check2 == 1:
                        config['Audio']['noplaylist'] = False
                        download(link, config['Audio'])
                    elif check2 == 2:
                        config['Video']['noplaylist'] = False
                        download(link, config['Video'])
                    elif check2 == 4:
                        download(link, config['Video'])
                    else:
                        download(link, config['Audio'])
                else:
                    print(colors8 + "Unknown Choice :(")
                check2 = str(input(colors7 + "[*] do you want to continue?(Y/n): "))
                if check2 == 'n':
                    print(colors9 + "Enjoy Watching Your Video, BYE/BYE :-D")
if __name__ == '__main__':
    main()
