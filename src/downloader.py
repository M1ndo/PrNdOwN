#!/usr/bin/python3
# Updated On 7/26/2020 (Latest Update 09/06/2020)
# Created By ybenel Aka m1ndo
from __future__ import unicode_literals
import os,sys,json,itertools,threading,banner,shutil,configparser,optparse
from time import sleep as sl
from random import shuffle,randint
from colors import get_colors
from distutils import util
try:
    import validators as valid
    import youtube_dl as dl
    import requests as req
except ImportError:
    print("[!] Modules ['requests','youtube_dl','validators'] Are Not Installed ! ")
    print("[+] Install Them To Get This Tool To Work ")
    sys.exit(0)
# global
platform = sys.platform
user = os.environ.get('USER')
default_conf = []
directory = []
class formats_ph():
    # Pornhub / xnxx / etc
    def reso_1080(): download.list_of_reso.append('1080p')
    def reso_720(): download.list_of_reso.append('720p')
    def reso_480(): download.list_of_reso.append('480p')
    def reso_360(): download.list_of_reso.append('360p')

class formats_yt():
    # Youtube
    def reso_4k_yt(): download.list_of_reso.append('313+140')
    def reso_2k_yt(): download.list_of_reso.append('271+140')
    def reso_1080_yt(): download.list_of_reso.append('137+140')
    def reso_720_yt(): download.list_of_reso.append('136+140')
    def reso_480_yt(): download.list_of_reso.append('135+140')
    def reso_360_yt(): download.list_of_reso.append('134+140')

class compare():
    def compare_formats(reso,link):
        if link.split('.')[1] in ['pornhub','xnxx','yourporn','xvideos','sex.com']:
            if reso not in ['1080p','720p','480p','360p','240p']: reso = "bestvideo+bestaudio/best"; download.list_of_reso *= 0; download.list_of_reso.append(reso)
            else: return
        else: return
class download():
    # Define list of resolutions
    # list_of_reso = ['bestvideo[height=1080]+bestaudio/best','bestvideo[height=720]+bestaudio/best','bestvideo[height=480]+bestaudio/best','bestvideo[height=240]+bestaudio/best']
    list_of_reso = []
    global recog
    com_reso = []
    audio_quality_list = []
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

    # Animation
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
    # get the current directory
    def get_current_dir(filename,dir):
        if dir is None:
            print()
            print('\n' + get_colors.green() + '[' + get_colors.magento() + '+' + get_colors.green() + ']' + get_colors.randomize2() + " Video Saved Undername "+ get_colors.randomize3() + f"['{filename}']" + get_colors.white() + '\n')
            print(get_colors.green() + '[' + get_colors.magento() + '+' + get_colors.green() + ']' + get_colors.white() + ' Folder ' + get_colors.randomize() + os.getcwd())
            print()
        else:
            print()
            print('\n' + get_colors.green() + '[' + get_colors.magento() + '+' + get_colors.green() + ']' + get_colors.randomize2() + " Video Saved Undername "+ get_colors.randomize3() + f"['{filename}']" + get_colors.white() + '\n')
            print(get_colors.green() + '[' + get_colors.magento() + '+' + get_colors.green() + ']' + get_colors.white() + ' Folder ' + get_colors.randomize() + dir)
            print()
    # Get Downloading Status
    def hooker(t):
        if t['status'] == 'downloading':
            sys.stdout.flush()
            sys.stdout.write('\r' + get_colors.red() +'[' + get_colors.cyan() +'+' + get_colors.red() + ']' + get_colors.randomize1() + ' Progress ' + get_colors.randomize() + str(t['_percent_str']))
            sl(0.1)
        elif t['status'] == 'finished':
            download.get_current_dir(t['filename'],directory[0])

    # List All Available Resolutions
    def user_resolution():
        available = ['4k','2k','1080p','720p','480p','360p']
        return available


    # Download Configurations
    def get_config():
        res = download.list_of_reso
        aud = download.audio_quality_list
        try:
            res = res[0]
        except:
            res = 'bestvideo+bestaudio/best'
        try:
            aud1 = aud[0]
            aud2 = aud[1]
        except:
            aud1 = 'bestaudio/best'
            aud2 = '320'
        config = {
            'Audio': {
                'format': aud1,
                'quiet': True,
                'noplaylist': True,
                'outtmpl': "%(title)s.%(ext)s",
                'writethumbnail': True,
                'progress_hooks': [download.hooker],
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': aud2},
                    {'key': 'EmbedThumbnail'},             # https://github.com/ytdl-org/youtube-dl/pull/25717/
                    {'key': 'FFmpegMetadata'},]
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

    def download(link, data):
        try:
            with dl.YoutubeDL(data) as ydl:
                ydl.download([link])
        except dl.utils.DownloadError:
            print("\n" + get_colors.randomize() + "["+get_colors.randomize2()+"!"+get_colors.randomize1()+"]" + get_colors.randomize2() + " Selected Quality Was Not Found!")
            print(get_colors.randomize() + "["+get_colors.randomize2()+"+"+get_colors.randomize1()+"]" + get_colors.randomize3() + " Auto Selecting The Best Quality Available")
            compare.compare_formats(download.com_reso[0],link)
            sl(2);download.reforce_check(link)

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
            if 'duration' in result:
                video_size = result['duration']
            else:
                video_size=None
            # video_url = video['url']
        return video_title,video_size,max_reso

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

    # URL recognition (Youtube,PH etc)
    def url_recognition(link):
        if "youtube" in link: download.recog = True
        else: download.recog = False

    # Video metadata
    def print_metadata(title,duration,resolution):
        print(get_colors.randomize() + "Title Video: " +get_colors.randomize1()+ f"{title} " + get_colors.randomize() + "Duration: " + get_colors.green() + f"{duration}" + get_colors.randomize() + " Highest Resolution: " + get_colors.cyan() + f"{resolution}")
        print()
        print(get_colors.cyan() + "[" + get_colors.magento() + '0' + get_colors.cyan() + "] " + get_colors.randomize2() + "Download an Audio playlist")
        print(get_colors.cyan() + "[" + get_colors.magento() + '1' + get_colors.cyan() + "] " + get_colors.randomize2() + "Download a Video playlist")
        print(get_colors.cyan() + "[" + get_colors.magento() + '2' + get_colors.cyan() + "] " + get_colors.randomize2() + "Download a Single Audio")
        print(get_colors.cyan() + "[" + get_colors.magento() + '3' + get_colors.cyan() + "] " + get_colors.randomize2() + "Download a single video file")
        print()
    # Video Metadata 2
    def print_metadata2(title,duration,resolution):
        print(get_colors.randomize() + "Title Video: " +get_colors.randomize1()+ f"{title} " + get_colors.randomize() + "Duration: " + get_colors.green() + f"{duration}" + get_colors.randomize() + " Highest Resolution: " + get_colors.cyan() + f"{resolution}")
        print()

    # User Input
    def user_input(option=0):
        if option==0:
            link = input(get_colors.randomize2() + "["+get_colors.randomize3()+"*"+get_colors.randomize1()+"]" + get_colors.randomize2() + " Enter the link: " + get_colors.randomize() + get_colors.white())
            return link
        elif option==1:
            try:
                metadata_inp = int(input(get_colors.randomize2() + "["+get_colors.randomize2()+"------------Enter your choice------------"+get_colors.randomize2()+"]: "))
                return metadata_inp
            except ValueError:
                user_input(option=1)
        elif option==2:
            try:
                reso_inp = int(input(get_colors.randomize2() + "["+get_colors.randomize2()+"------------Enter your choice------------"+get_colors.randomize2()+"]: "))
                return reso_inp
            except ValueError:
                user_input(option=2)
        elif option==3:
            con_inp = str(input(get_colors.white() + "[*] Do You Want To Continue? (Y/n): "))
            return con_inp
        else: return

    # Print More Stuff
    def user_print(option=0):
        if option==0:
            print(get_colors.randomize() + "Unknown Choice :(")
        elif option==1:
            print("\n" + get_colors.randomize() + "["+get_colors.randomize2()+"!"+get_colors.randomize1()+"]" + get_colors.randomize3() + " Unvalid Url!!!" + get_colors.randomize2())
            print(get_colors.randomize() + "["+get_colors.randomize1()+"!"+get_colors.randomize2()+"]" + get_colors.randomize2() + " Please Try Again" + get_colors.randomize3())
        elif option==2:
            resolutions = download.user_resolution()
            print(get_colors.randomize() + "[+] Please Select Your Prefered Resolution\n")
            for i in range(0,6):
                print(get_colors.cyan() + "[" + get_colors.magento() + str(i) + get_colors.cyan() + "] " + get_colors.randomize2() +  resolutions[i])
            print()
        elif option==3:
            print(get_colors.randomize2() + "DownloadError Occurred !!!")
            print(get_colors.randomize1() + "Re Run The Script With The Same URL And The Same Options To Continue Downloading!")
        elif option==4:
            print(get_colors.randomize1() + "Your Choice Is Out Of Range !")
        else: return

    # Shortcut
    def reforce_check(link):
        config = download.get_config()
        download.clear()
        download.buggy()
        download.download(link, config['Video'])

    # Download Options
    def down_options(reso_inp,link):
        recog = download.recog
        if reso_inp in [0,1,2,3]:
            if recog == False:
                if reso_inp == 2:
                    formats_ph.reso_1080()
                    download.reforce_check(link)
                elif reso_inp == 3:
                    formats_ph.reso_720()
                    download.reforce_check(link)
                elif reso_inp == 4:
                    formats_ph.reso_480()
                    download.reforce_check(link)
                elif reso_inp == 5:
                    formats_ph.reso_360()
                    download.reforce_check(link)
                elif reso_inp in [0,1]:
                    print("[+] 2k and 4k Only Supports Youtube And Pornhub Premium")
                    exit(1)
                else: download.user_print(option=4)
            else:
                if reso_inp == 2:
                    formats_yt.reso_1080_yt()
                    download.reforce_check(link)
                elif reso_inp == 3:
                    formats_yt.reso_720_yt()
                    download.reforce_check(link)
                elif reso_inp == 4:
                    formats_yt.reso_480_yt()
                    download.reforce_check(link)
                elif reso_inp == 5:
                    formats_yt.reso_360_yt()
                    download.reforce_check(link)
                elif reso_inp == 0:
                    formats_yt.reso_4k_yt()
                    download.reforce_check(link)
                elif reso_inp == 1:
                    formats_yt.reso_2k_yt()
                    download.reforce_check(link)
                else: download.user_print(option=4)

        else: download.user_reso(option=4)

    # Type Of Download
    def type_down(metadata_inp,link,resolution):
        config = download.get_config()
        if metadata_inp in [0,1,2,3]:
            if metadata_inp == 0:
                config['Audio']['noplaylist'] = False
                download.download(link, config['Audio'])
            elif metadata_inp == 1:
                config['Video']['noplaylist'] = False
                download.download(link, config['Video'])
            elif metadata_inp == 2:
                 download.download(link, config['Audio'])
            elif metadata_inp == 3:
                download.bncl()
                download.user_print(option=2)
                reso_inp = download.user_input(option=2)
                download.com_reso.append(resolution)
                download.down_options(reso_inp,link)
            else: download.user_print(option=0)

    # all out
    def get_over(link):
        title, duration,reso = download.get_info(link)
        if duration is not None:
            duration = int(duration)
            duration = m,s = divmod(duration,60)
            duration = h,m = divmod(duration[0], 60)
            duration = (f'{h:d}:{m:02d}:{s:02d}')
        else:
            duration = None
        return title,duration,reso

    # BannerAndClear
    def bncl():
        download.clear()
        banner.banner()

    # Use A config
    # Later

    # The Holy Engine Of Look
    def run():
        download.bncl()
        while True:
            try:
                if download.check_url("https://google.com"):
                    link = download.user_input(option=0)
                    if not valid.url(link):
                        download.user_print(option=1)
                        exit(1)
                    if download.check_connection(link):
                        download.bncl()
                        download.url_recognition(link)
                        title,duration,resolution = download.get_over(link)
                        download.print_metadata(title,duration,resolution)
                        metadata_inp = download.user_input(option=1)
                        download.type_down(metadata_inp,link,resolution)
                con_inp = download.user_input(option=3)
                if con_inp in ['Y','y']:
                        download.bncl()
                        continue
                elif con_inp in ['N', 'n']:
                    print("\n[+] Cya Next Time")
                    exit(1)
                else:
                    download.user_print(option=0)
                    continue

            except dl.utils.DownloadError:
                download.bncl()
                print(get_colors.randomize2() + "DownloadError Occurred !!!")
                print(get_colors.randomize1() + "Re Run The Script With The Same URL And The Same Options To Continue Downloading!")
                exit(1)

    # Command Arguments
    def command_line():
        parser = optparse.OptionParser()
        parser.add_option('-c','--cmd', dest="cmd", action="store_true",default=False,help="Use The Traditional Look")
        parser.add_option('-u','--url', dest="url",type="string",help="Video / Audio Url")
        parser.add_option('-r','--config',dest='conf',action="store_true",default=False,help="Read And Use The Config File")
        parser.add_option('-q','--quiet',dest='verbose',action='store_true',default=False,help="Don't print status messages")
        parser.add_option('-a','--audio-quality',dest='audio_qual',type='int',help='Specify Audio Quality Between 0 and 1 (0 is the best 1 is the worse)')
        parser.add_option('-v','--video-quality',dest='video_qual',type='string',help='Specify Video Quality Between 4k To 360 (4k,2k,1080,720,480,360)')
        parser.add_option('-x','--extract-audio',dest='extract',action='store_true',help='Extract Audio From a video source')
        parser.add_option('-p','--playlist',dest='playlist',action="store_true",help='Download A Playlist With Specified URL')
        parser.add_option('-f','--file',dest='file',type='string',help='Read a file contains a list of urls then download them all')
        parser.add_option('-o','--output',dest='output',type='string',help='Output File Location')
        (options,args) = parser.parse_args()
        return options,parser


    # More And More And More If Statements FUCK

    # Download Options
    def com_options(reso,link):
        recog = download.recog
        if recog == False:
            if reso == '1080':
                formats_ph.reso_1080()
                download.reforce_check(link)
            elif reso == '720':
                formats_ph.reso_720()
                download.reforce_check(link)
            elif reso == '480':
                formats_ph.reso_480()
                download.reforce_check(link)
            elif reso == '360':
                formats_ph.reso_360()
                download.reforce_check(link)
            elif reso in ["4k","2k"]:
                print("[+] 2k and 4k Only Supports Youtube And Pornhub Premium")
                exit(1)
            else: download.user_print(option=4)
        else:
            if reso == '1080':
                formats_yt.reso_1080_yt()
                download.reforce_check(link)
            elif reso == '720':
                formats_yt.reso_720_yt()
                download.reforce_check(link)
            elif reso == '480':
                formats_yt.reso_480_yt()
                download.reforce_check(link)
            elif reso == '360':
                formats_yt.reso_360_yt()
                download.reforce_check(link)
            elif reso == "4k":
                formats_yt.reso_4k_yt()
                download.reforce_check(link)
            elif reso == "2k":
                formats_yt.reso_2k_yt()
                download.reforce_check(link)
            else: download.user_print(option=4)

    # Audio Managing
    def audio_man(link,choice=1):
        config = download.get_config()
        if choice==1:
            download.download(link, config['Audio'])
        else:
            config['Audio']['noplaylist'] = False
            download.download(link, config['Audio'])

    # For Sake of Time
    def move_file(src,loc):
        try:
            shutil.move(src,loc)
        except:
            try:
                src = src.split(".")[0] + '.mp3'
                shutil.move(src,loc)
            except:
                print("File not found ! Thus We Cannot Move it")

    # Where To Save File
    def output_file(location,title):
        src = title+'.mp4'
        if os.path.isdir(location):
            if platform == 'win32':
                if location.endswith('\\'):
                    download.move_file(src,location)
                else:
                    location = location+"\\"
                    download.move_file(src,location)
            else:
                if location.endswith('/'):
                    download.move_file(src,location)
                else:
                    location = location + "/"
                    download.move_file(src,location)

        else:
            print("[!] Directory Not Found")


    def get_me_my_stuff(url,output,video_qual,audio_qual,playlist,extract_audio,quiet):
        if not valid.url(url):
            download.user_print(option=1)
            return
        if download.check_url("https://google.com") and download.check_connection(url):
            if quiet == False:
                if extract_audio == False or extract_audio == None:
                    download.bncl()
                    download.url_recognition(url)
                    directory.append(output)
                    title,duration,resolution = download.get_over(url)
                    download.com_reso.append(resolution)
                    download.print_metadata2(title,duration,resolution)
                    sl(5)
                    if video_qual == None:
                        video_qual = '1080'
                    if video_qual in ['4k','2k','1080','720','480','360']:
                        if playlist == True:
                            config['Video']['noplaylist'] = False
                        download.com_options(video_qual,url)
                        if output != None: download.output_file(output,title)
                    else: download.user_print(option=4)
                else:
                    title,duration,resolution = download.get_over(url)
                    download.print_metadata2(title,duration,resolution)
                    directory.append(output)
                    if audio_qual != None:
                        if playlist == False:
                            if audio_qual == 0:
                                download.audio_quality_list.extend(['bestaudio/best','320'])
                                download.audio_man(url,choice=1)
                                if output != None: download.output_file(output,title)
                            elif audio_qual == 1:
                                download.audio_quality_list.extend(['worstaudio/worst','124'])
                                download.audio_man(url,choice=1)
                                if output != None: download.output_file(output,title)
                            else:
                                download.audio_quality_list.extend(['bestaudio/best','320'])
                                download.audio_man(url,choice=1)
                                if output != None: download.output_file(output,title)
                        else:
                            if audio_qual == 0:
                                download.audio_quality_list.extend(['bestaudio/best','320'])
                                download.audio_man(url,choice=2)
                                if output != None: download.output_file(output,title)
                            elif audio_qual == 1:
                                download.audio_quality_list.extend(['worstaudio/worst','124'])
                                download.audio_man(url,choice=2)
                                if output != None: download.output_file(output,title)
                            else:
                                download.audio_quality_list.extend(['bestaudio/best','320'])
                                download.audio_man(url,choice=2)
                                if output != None: download.output_file(output,title)

                    else:
                        print("[!] Audio Quality Was Not Specified\n[+] Using The Best Quality Available")
                        download.audio_quality_list.extend(['bestaudio/best','320'])
                        download.audio_man(url,choice=1)
            else:
                if extract_audio == False or extract_audio == None:
                    download.url_recognition(url)
                    directory.append(output)
                    title,duration,resolution = download.get_over(url)
                    download.com_reso.append(resolution)
                    sl(5)
                    if video_qual == None:
                        video_qual = '1080'
                    if video_qual in ['4k','2k','1080','720','480','360']:
                        if playlist == True:
                            config['Video']['noplaylist'] = False
                        download.com_options(video_qual,url)
                        if output != None: download.output_file(output,title)
                    else: download.user_print(option=4)
                else:
                    title,duration,resolution = download.get_over(url)
                    directory.append(output)
                    if audio_qual != None:
                        if playlist == False:
                            if audio_qual == 0:
                                download.audio_quality_list.extend(['bestaudio/best','320'])
                                download.audio_man(url,choice=1)
                                if output != None: download.output_file(output,title)
                            elif audio_qual == 1:
                                download.audio_quality_list.extend(['worstaudio/worst','124'])
                                download.audio_man(url,choice=1)
                                if output != None: download.output_file(output,title)
                            else:
                                download.audio_quality_list.extend(['bestaudio/best','320'])
                                download.audio_man(url,choice=1)
                                if output != None: download.output_file(output,title)
                        else:
                            if audio_qual == 0:
                                download.audio_quality_list.extend(['bestaudio/best','320'])
                                download.audio_man(url,choice=2)
                                if output != None: download.output_file(output,title)
                            elif audio_qual == 1:
                                download.audio_quality_list.extend(['worstaudio/worst','124'])
                                download.audio_man(url,choice=2)
                                if output != None: download.output_file(output,title)
                            else:
                                download.audio_quality_list.extend(['bestaudio/best','320'])
                                download.audio_man(url,choice=2)
                                if output != None: download.output_file(output,title)

                    else:
                        print("[!] Audio Quality Was Not Specified\n[+] Using The Best Quality Available")
                        download.audio_quality_list.extend(['bestaudio/best','320'])
                        download.audio_man(url,choice=1)

    # Probably The all
    def kick_it(file,output,audio_qual,video_qual,url=None,quiet=False,extract_audio=False,playlist=False):
        if url==None and file==None:
            print("[!] Cannot Procced if there's no URL Or File list")
            exit(1)
        else:
            if file != None:
                if os.path.isfile(file):
                    times = 0
                    while True:
                        with open(file, 'r') as list:
                            url = list.readlines()
                            leng = len(url)
                            if leng > times:
                                url = url[times].strip()
                                times += 1
                                download.get_me_my_stuff(url,output,video_qual,audio_qual,playlist,extract_audio,quiet)
                            else:
                                break
            else:
                download.get_me_my_stuff(url,output,video_qual,audio_qual,playlist,extract_audio,quiet)


    # The Holy Engine
    def runner():
        options, parser = download.command_line()
        if options.conf:
            config_reader.find_config()
            url = options.url
            file = options.file
            output = default_conf[0]
            audio_quality = default_conf[3]
            video_quality = default_conf[1]
            quiet = default_conf[5]
            playlist = default_conf[6]
            extract_audio = default_conf[4]
        else:
            url = options.url
            file = options.file
            output = options.output
            audio_quality = options.audio_qual
            video_quality = options.video_qual
            quiet = options.verbose
            playlist = options.playlist
            extract_audio = options.extract
        if options.cmd:
            download.run()
        download.kick_it(file,output,audio_quality,video_quality,url,quiet,extract_audio,playlist)



class config_reader():
    def find_config():
        if platform in ['win64','win32'] and os.path.isfile('config.rc') == True:
            config_reader.read_config(1)
        elif platform == 'linux':
            if os.path.isfile('config.rc') == True:
                config_reader.read_config(1)
            elif os.path.isfile('/home/%s/.config/PrNdOwN/config.rc'%(user)) == True:
                config_reader.read_config(2)
        else:  return

    def read_config(option=1):
        if option==1:
            try:
                config = configparser.ConfigParser()
                config.read('config.rc')
                prev_loc = config['DEFAULT']['Prevered_location']
                vid_qual = config['DEFAULT']['Video_quality']
                # vid_qual2 = config['DEFAULT']['Second_video_quality']
                vid_qual2 = vid_qual
                sound_qual = config['DEFAULT']['Sound_quality']
                extr = config['DEFAULT']['Extract_audio']
                qta = config['DEFAULT']['Quiet']
                Playlist = config['DEFAULT']['Playlist']
                extr = bool(util.strtobool(extr))
                qta = bool(util.strtobool(qta))
                Playlist = bool(util.strtobool(Playlist))
                default_conf.extend([prev_loc,vid_qual,vid_qual2,sound_qual,extr,qta,Playlist])
            except KeyError: return
        else:
            try:
                config = configparser.ConfigParser()
                config.read('/home/%s/.config/PrNdOwN/config.rc'%(user))
                prev_loc = config['DEFAULT']['Prevered_location']
                vid_qual = config['DEFAULT']['Video_quality']
                vid_qual2 = vid_qual
                sound_qual = config['DEFAULT']['Sound_quality']
                extr = config['DEFAULT']['Extract_audio']
                qta = config['DEFAULT']['Quiet']
                Playlist = config['DEFAULT']['Playlist']
                extr = bool(util.strtobool(extr))
                qta = bool(util.strtobool(qta))
                Playlist = bool(util.strtobool(Playlist))
                default_conf.extend([prev_loc,vid_qual,vid_qual2,sound_qual,extr,qta,Playlist])
            except KeyError: return
