#!/usr/bin/env python3
# Created By r2dr0dn
# Hd Video Downloader For PornHub
# Don't Copy The Code Without Giving The Credits Nerd


from __future__ import unicode_literals
try:
    import os,sys,requests
    import youtube_dl as dl
    import validators as valid
    from time import sleep as sl
    from random import random,randint
except ImportError:
    print('['+'*'*20+']')
    print('Module [youtube-dl] Status: Not Found!')
    print('['+'*'*20+']')
    print('Please Install It Using [pip3 install youtube-dl]')
    print('['+'*'*20+']')
# Colors:
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
# Clear Screen
def clear():
    clear = os.system('clear')
    return clear
# banner
def banner():
    print(colors + """
           .'\   /`.
         .'.-.`-'.-.`.
    ..._:   .-. .-.   :_...
  .'    '-.(o ) (o ).-'    `.
 :  _    _ _`~(_)~`_ _    _  :
:  /:   ' .-=_   _=-. `   ;\  :
:   :|-.._  '     `  _..-|:   :
 :   `:| |`:-:-.-:-:'| |:'   :
  `.   `.| | | | | | |.'   .'
    `.   `-:_| | |_:-'   .'     - Welcome To PrNdOwN!
      `-._   ````    _.-'
          ``-------''
    """)
# Check if user is connected to internet
def net(url):
    try:
        requests.get(url)
    except requests.exceptions.ConnectionError:
        print(colors + "[!] Please check your network connection.")
        return False
    except requests.exceptions.Timeout:
        print(colors2 + "[!!!] Site is taking too long to load, TimeOut.")
        return False
    except requests.exceptions.TooManyRedirects:
        print(colors3 + "[*] Too many Redirects.")
        return False
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print(e)
        sys.exit(1)
    return True
# Check the validity of the given url
def check(link):
    try:
        requests.get(link)
        return True
    except requests.exceptions.ConnectionError:
        print(colors4 + "[!] disconnected from network.")
        return False
    except requests.exceptions.HTTPError as err:
        print(err)
        return False
# Configuration File
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
# Url Download
def download(link, data):
    try:
        with dl.YoutubeDL(data) as ydl:
            ydl.download([link])
    except dl.utils.DownloadError as err:
        print(colors + err)
# Extract URL Information
def get_info(link):
    ydl2 = dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
    with ydl2:
        result = ydl2.extract_info(link,download=False)
        if 'entries' in result:
            video = result['entries'][0]
        else:
            video = result
        video_title = video['title']
        # video_url = video['url']
    return video_title
# Main Function
def main():
    try:
        clear()
        banner()
        while True:
            try:
                if net('https://pornhub.com/'):
                    link = input(colors2 + "["+colors3+"*"+colors4+"]" + colors2 + " Enter the link: " + colors9)
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
                        check_inp = int(input(colors + "["+colors4+"------------Enter your choice------------"+colors5+"]: "))
                        if check_inp in [1,2,3,4]:
                            if check_inp == 1:
                                config['Audio']['noplaylist'] = False
                                download(link, config['Audio'])
                            elif check_inp == 2:
                                config['Video']['noplaylist'] = False
                                download(link, config['Video'])
                            elif check_inp == 4:
                                download(link, config['Video'])
                            elif check_inp == 3:
                                download(link, config['Audio'])
                        else:
                            print(colors8 + "Unknown Choice :(")
                check_str = str(input(colors7 + "[*] Do You Want To Continue? (Y/n): "))
                if check_str in ['Y','y']:
                    banner()
                    continue
                else:
                    print(colors6 + "Cya Next Time")
                    break
            except dl.utils.DownloadError:
                print(colors3 + "DownloadError Occurred !!!")
                print(colors4 + "Re Run The Script With The Same URL And The Same Options To Continue Downloading!")
                exit(1)
    except RuntimeError:
        exit(1)
if __name__ == '__main__':
    main()
