#!/usr/bin/python3
# Updated In 00/04/2020
# Created By Ybenel
from __future__ import unicode_literals
import os,sys
from time import sleep as sl 
from random import randint
import json
from colors import get_colors
try:
    import validators as valid 
    import youtube_dl as dl 
    import requests as req 
except ImportError:
    print("[!] Modules ['requests','youtube_dl','validators'] Are Not Installed ! ")
    print("[+] Install Them To Get This Tool To Work ")
    sys.exit(0)

class download():
    def clear():
        clear = os.system('clear')
        return clear
    def banner():
        print(get_colors.white() + get_colors.randomize() + """
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
    def check_url(url):
        try:
            req.get(url)
        except req.exceptions.ConnectionError:
            print("[!] Please check your network connection.")    
            return False
        except req.exceptions.Timeout:
            print("[!] Site is taking too long to load, TimeOut.")
            return False
        except req.exceptions.TooManyRedirects:
            print("[!] Too Many Redirects")
            return False
        except req.exceptions.RequestException as ex:
            print("[!] " + ex)
            sys.exit(0)
        return True
    def check_connection(link):
        try:
            req.get(link)
            return True
        except req.exceptions.ConnectionError:
            print("[!] Please check your network connection.")  
            return False
        except req.exceptions.HTTPError as error:
            print("[!] " + error)
            sys.exit(0)
    def get_config():
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
        return config
    def download(link, data):
        try:
            with dl.YoutubeDL(data) as ydl:
                ydl.download([link])          
        except dl.utils.DownloadError as err:
            print("[!] " + err)      
    def get_info(link):
        ydl2 = dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
        with ydl2:
            result = ydl2.extract_info(link,download=False)
            if 'entries' in result:
                video = result['entries'][0]
            else:
                video = result
            video_title = video['title']
            if 'duration' in video:
                video_size = video['duration']
            else:
                video_size = None    
            # video_url = video['url']
        return video_title, video_size
    def run():
        download.clear()
        download.banner()
        while True:
            try:
                if download.check_url('https://pornhub.com'):
                    link = input(get_colors.randomize2() + "["+get_colors.randomize3()+"*"+get_colors.randomize1()+"]" + get_colors.randomize2() + " Enter the link: " + get_colors.randomize() + get_colors.white())
                    if not valid.url(link):
                        print("\n" + get_colors.randomize() + "["+get_colors.randomize2()+"!"+get_colors.randomize1()+"]" + get_colors.randomize3() + " Unvalid Url!!!" + get_colors.randomize2())
                        print(get_colors.randomize() + "["+get_colors.randomize1()+"!"+get_colors.randomize2()+"]" + get_colors.randomize2() + " Please Try Again" + get_colors.randomize3())
                        sys.exit(1)
                    if download.check_connection(link):
                        title, duration = download.get_info(link)
                        if duration is not None:
                            duration = m,s = divmod(duration,60)
                            duration = h,m = divmod(duration[0], 60)
                            duration = (f'{h:d}:{m:02d}:{s:02d}')
                        else:
                            duration = None                            
                        download.clear()
                        download.banner()
                        print(get_colors.randomize() + "Title Video: " +get_colors.randomize1()+ f"{title} " + get_colors.randomize() + "Duration: " + get_colors.green() + f"{duration}")
                        print(get_colors.randomize2()+ "[*] 1.Download an Audio playlist")
                        print(get_colors.randomize3() + "[*] 2.Download a Video playlist")
                        print(get_colors.randomize() + "[*] 3.Download a Single Audio")
                        print(get_colors.randomize1() + "[*] 4.Download a single video file")
                        check_inp = int(input(get_colors.randomize2() + "["+get_colors.randomize2()+"------------Enter your choice------------"+get_colors.randomize2()+"]: "))
                        config = download.get_config()
                        if check_inp in [1,2,3,4]:
                            if check_inp == 1:
                                config['Audio']['noplaylist'] = False
                                download.download(link, config['Audio'])
                            elif check_inp == 2:
                                config = download.get_config()
                                config['Video']['noplaylist'] = False
                                download.download(link, config['Video'])
                            elif check_inp == 4:
                                download.download(link, config['Video'])
                            elif check_inp == 3:
                                download.download(link, config['Audio'])
                            else:
                                print(get_colors.randomize() + "Unknown Choice :(")  
                        elif check_inp not in [1,2,3,4]:
                            print(get_colors.randomize() + "Unknown Choice :(")             
                        else:
                            print(get_colors.randomize() + "Unknown Choice :(")             
                check_str = str(input(get_colors.randomize1() + "[*] Do You Want To Continue? (Y/n): "))
                if check_str in ['Y','y']:
                        # banner()
                        download.clear()
                        download.banner()
                        continue  
                elif check_str in ['N', 'n']:
                    print("[+] Cya Next Time")
                    exit(1)
                else:
                    print("Unknown Option")
                    continue
            except dl.utils.DownloadError:
                download.clear()
                print(get_colors.randomize2() + "DownloadError Occurred !!!")
                print(get_colors.randomize1() + "Re Run The Script With The Same URL And The Same Options To Continue Downloading!")
                exit(1)                             
