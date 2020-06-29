#!/usr/bin/python3
# Updated In 6/13/2020
# Created By ybenel Aka pOmS
from __future__ import unicode_literals
import os,sys
from time import sleep as sl 
from random import randint,shuffle
import json
from colors import get_colors
import itertools
import threading
import banner
try:
    import validators as valid 
    import youtube_dl as dl 
    import requests as req 
except ImportError:
    print("[!] Modules ['requests','youtube_dl','validators'] Are Not Installed ! ")
    print("[+] Install Them To Get This Tool To Work ")
    sys.exit(0)



class download():
    # Define list of resolutions
    # list_of_reso = ['bestvideo[height=1080]+bestaudio/best','bestvideo[height=720]+bestaudio/best','bestvideo[height=480]+bestaudio/best','bestvideo[height=240]+bestaudio/best']
    list_of_reso = []
    # Clear The Screen 
    def clear():
        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')
    # Check if the link is alive
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
    
    # Check if my net is alive
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
    
    def animation(timing='1234',begin=True):
        done = begin
        # for c in itertools.cycle(['|', '/', '-', '\\']):
        for c in range(1,10):
                if done:
                    break
                sys.stdout.write('\rTime Is ' + str(c) + timing)
                sys.stdout.flush()
                sl(0.1)
        sys.stdout.write('\rDone!     ')
        done = True  
    def get_current_dir(filename):
        print()
        print('\n' + get_colors.green() + '[' + get_colors.magento() + '+' + get_colors.green() + ']' + get_colors.randomize2() + " Video Saved Undername "+ get_colors.randomize3() + f"['{filename}']" + get_colors.white() + '\n')
        print(get_colors.green() + '[' + get_colors.magento() + '+' + get_colors.green() + ']' + get_colors.white() + ' Folder ' + get_colors.randomize() + os.getcwd())
        print()
    # Get Downloading Status 
    def hooker(t):
        if t['status'] == 'downloading':
            sys.stdout.flush()
            sys.stdout.write('\r' + get_colors.red() +'[' + get_colors.cyan() +'+' + get_colors.red() + ']' + get_colors.randomize1() + ' Progress ' + get_colors.randomize() + str(t['_percent_str']))
            sl(0.1)
        elif t['status'] == 'finished':
            download.get_current_dir(t['filename'])
            
    # List All Available Resolutions
    def user_resolution():
        available = ['1080p','720p','480p','240p']
        return available
    
    # Use User Resolution
    # def define_resolution(reso=1080):
        # user_reso = f'bestvideo[height={reso}]+bestaudio/best'
        # download.list_of_reso.append(user_reso)

    # Resolution Configuration
    # 1080p
    def reso_1080():
        download.list_of_reso.append('1080p')
    # 720p
    def reso_720():
        download.list_of_reso.append('720p')
    # 480
    def reso_480():
        download.list_of_reso.append('480p')
    # 360
    def reso_360():
        download.list_of_reso.append('240p')
    
    # Download Config
    def get_config():
        res = download.list_of_reso
        try:
            res = res[0]
        except:
            res = 'bestvideo+bestaudio/best'
        config = {
            'Audio': {
                'format': 'bestaudio/best',
                'quiet': True,
                'noplaylist': True,
                'outtmpl': "%(title)s.%(ext)s",
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            },
            'Video': {
                'format': res,
                'quiet': True,
                'outtmpl': "%(title)s.%(ext)s",
                'noplaylist': True,
                'progress_hooks': [download.hooker],
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',
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
    
    # Download Form
    def download(link, data):
        try:
            with dl.YoutubeDL(data) as ydl:
                ydl.download([link])          
        except dl.utils.DownloadError as err:
            print("[!] " + err)      
    
    # Scrape Link Info ['metadata','thumbnail','uploader'....]
    def get_info(link):
        ydl2 = dl.YoutubeDL({'quiet':True})
        with ydl2:
            result = ydl2.extract_info(link,download=False)
            if 'entries' in result:
                video = result['entries'][0]
            else:
                video = result
            video_title = video['title']
            max_reso = video['format_id']
            if 'duration' in video:
                video_size = video['duration']
            else:
                video_size = None    
            # video_url = video['url']
        return video_title, video_size,max_reso
    
    # Let's see how lucky you are
    def buggy():
        nums = [1,2,3,4,5,6,7,8,9,10]
        shuffle(nums)
        if nums == 7:
            x = threading.Thread(target=banner.banner3)
            x.start()
            download.clear()
            banner.buggy()
            print()
        else:
            banner.banner4()  
            print()
    # The Engine
    def run():
        download.clear()
        banner.banner()
        while True:
            try:
                if download.check_url('https://pornhub.com'):
                    link = input(get_colors.randomize2() + "["+get_colors.randomize3()+"*"+get_colors.randomize1()+"]" + get_colors.randomize2() + " Enter the link: " + get_colors.randomize() + get_colors.white())
                    if not valid.url(link):
                        print("\n" + get_colors.randomize() + "["+get_colors.randomize2()+"!"+get_colors.randomize1()+"]" + get_colors.randomize3() + " Unvalid Url!!!" + get_colors.randomize2())
                        print(get_colors.randomize() + "["+get_colors.randomize1()+"!"+get_colors.randomize2()+"]" + get_colors.randomize2() + " Please Try Again" + get_colors.randomize3())
                        sys.exit(1)
                    if download.check_connection(link):
                        title, duration,reso = download.get_info(link)
                        if duration is not None:
                            duration = m,s = divmod(duration,60)
                            duration = h,m = divmod(duration[0], 60)
                            duration = (f'{h:d}:{m:02d}:{s:02d}')
                        else:
                            duration = None                            
                        download.clear()
                        banner.banner2()
                        print(get_colors.randomize() + "Title Video: " +get_colors.randomize1()+ f"{title} " + get_colors.randomize() + "Duration: " + get_colors.green() + f"{duration}" + get_colors.randomize() + " Highest Resolution: " + get_colors.cyan() + f"{reso}")
                        print()
                        print(get_colors.cyan() + "[" + get_colors.magento() + '0' + get_colors.cyan() + "] " + get_colors.randomize2() + "Download an Audio playlist")
                        print(get_colors.cyan() + "[" + get_colors.magento() + '1' + get_colors.cyan() + "] " + get_colors.randomize2() + "Download a Video playlist")
                        print(get_colors.cyan() + "[" + get_colors.magento() + '2' + get_colors.cyan() + "] " + get_colors.randomize2() + "Download a Single Audio")
                        print(get_colors.cyan() + "[" + get_colors.magento() + '3' + get_colors.cyan() + "] " + get_colors.randomize2() + "Download a single video file")
                        print()
                        check_inp = int(input(get_colors.randomize2() + "["+get_colors.randomize2()+"------------Enter your choice------------"+get_colors.randomize2()+"]: "))
                        config = download.get_config()
                        if check_inp in [0,1,2,3]:
                            if check_inp == 0:
                                config['Audio']['noplaylist'] = False 
                                download.download(link, config['Audio'])
                            elif check_inp == 1:
                                config['Video']['noplaylist'] = False
                                download.download(link, config['Video'])
                            elif check_inp == 3:
                                download.clear()
                                banner.banner2()
                                resolutions = download.user_resolution()
                                print(get_colors.randomize() + "[+] Please Select Your Prefered Resolution\n")
                                for i in range(0,4):
                                    print(get_colors.cyan() + "[" + get_colors.magento() + str(i) + get_colors.cyan() + "] " + get_colors.randomize2() +  resolutions[i])
                                print()
                                check_inp = int(input(get_colors.randomize2() + "["+get_colors.randomize2()+"------------Enter your choice------------"+get_colors.randomize2()+"]: "))
                                if check_inp in [0,1,2,3]:
                                    if check_inp == 0:
                                        download.reso_1080()
                                        config = download.get_config()
                                        download.clear()
                                        download.buggy()
                                        download.download(link, config['Video'])
                                    elif check_inp == 1:
                                        download.reso_720()
                                        config = download.get_config()
                                        download.clear()
                                        download.buggy()
                                        download.download(link, config['Video'])
                                    elif check_inp == 2:
                                        download.reso_480()
                                        config = download.get_config()
                                        download.clear()
                                        download.buggy()
                                        download.download(link, config['Video'])
                                    elif check_inp == 3:
                                        download.reso_360()
                                        config = download.get_config()
                                        download.clear()
                                        download.buggy()
                                        download.download(link, config['Video'])                                        
                                    else:
                                        print(get_colors.randomize() + "Unknown Choice :(")
                                        quit()
                                else:
                                    print(get_colors.randomize() + "Unknown Choice :(")
                            elif check_inp == 2:
                                download.download(link, config['Audio'])
                            else:
                                print(get_colors.randomize() + "Unknown Choice :(")  
                        elif check_inp not in [1,2,3,4]:
                            print(get_colors.randomize() + "Unknown Choice :(")             
                        else:
                            print(get_colors.randomize() + "Unknown Choice :(")             
                check_str = str(input(get_colors.white() + "[*] Do You Want To Continue? (Y/n): "))
                if check_str in ['Y','y']:
                        # banner()
                        download.clear()
                        banner.banner()
                        continue  
                elif check_str in ['N', 'n']:
                    print("\n[+] Cya Next Time")
                    exit(1)
                else:
                    print("Unknown Option")
                    continue
            except dl.utils.DownloadError:
                download.clear()
                print(get_colors.randomize2() + "DownloadError Occurred !!!")
                print(get_colors.randomize1() + "Re Run The Script With The Same URL And The Same Options To Continue Downloading!")
                exit(1)                             
