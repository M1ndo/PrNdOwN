#!/usr/bin/python3
# Updated On 22/08/2021
# Created By ybenel
"""
Important Notes:
External Downloader And its args do only work in specific video formats In platforms like (youtube)
Unfortunately It doesn't work on PH And Other Sites.
"""
from __future__ import unicode_literals
import os,sys,json,itertools,threading,banner,shutil,configparser,optparse
from time import sleep as sl
from random import shuffle,randint
from colors import get_colors
from distutils import util,spawn
try:
    import validators as valid
    import youtube_dl as dl
    import requests as req
    if spawn.find_executable('ffmpeg'):
        pass
    else: print("[!] 'ffmpeg' Is Required ! ");sys.exit(0)
except ImportError:
    print("[!] Modules ['requests','youtube_dl','validators'] Are Not Installed ! ")
    print("[+] Install Them To Get This Tool To Work ")
    sys.exit(0)
# global
platform = sys.platform
user = os.environ.get('USER')
default_conf = []
directory = []
titlez = []
playlist_link = []
extension = []
cf_path = ("/home/%s/.config/PrNdOwN/"%(user))

# Config Parser
class config_reader():
    def find_config(filename='config.rc'):
        if platform in ['win64','win32'] and os.path.isfile(filename) == True:
            config_reader.read_config(filename)
        elif platform == 'linux':
            if os.path.isfile(filename) == True:
                config_reader.read_config(filename)
            elif os.path.isfile('%s%s'%(cf_path,filename)) == True:
                config_reader.read_config(('%s%s'%(cf_path,filename)))
            else:
                print("[!] Config Not Found !");exit(1)
        else: config_reader.read_config(filename)

    def read_config(filename):
            try:
                config = configparser.ConfigParser()
                config.read(filename)
                prev_loc = config['DEFAULT']['Prevered_location']
                vid_qual = config['DEFAULT']['Video_quality']
                vid_qual2 = vid_qual
                sound_qual = config['DEFAULT']['Sound_quality']
                extr = config['DEFAULT']['Extract_audio']
                qta = config['DEFAULT']['Quiet']
                Playlist = config['DEFAULT']['Playlist']
                aria2c = config['DEFAULT']['Aria2c']
                external = config['DEFAULT']['External']
                external_args = config['DEFAULT']['External_args']
                proxy = config['DEFAULT']['Proxy']
                geobypass = config['DEFAULT']['Geobypass']
                vid_Aud = config['DEFAULT']['Formats'];vid_Aud = list(vid_Aud.split(" "))
                Aud_bit = config['DEFAULT']['Audio_Bit']
                thumbnail = config['DEFAULT']['Thumbnail']
                sound_qual = bool(util.strtobool(sound_qual))
                extr = bool(util.strtobool(extr))
                qta = bool(util.strtobool(qta))
                Playlist = bool(util.strtobool(Playlist))
                aria2c = bool(util.strtobool(aria2c))
                geoby = bool(util.strtobool(geobypass))
                default_conf.extend([prev_loc,vid_qual,vid_qual2,sound_qual,extr,qta,Playlist,aria2c,external,external_args,proxy,vid_Aud,Aud_bit,geoby,thumbnail])
            except KeyError: return

# Parser All Arguments To Config Then Download
class parser_args():
    def __init__(self,*args):
        self.type = args[0]
        self.link = args[1]
        self.format = args[2]
        self.audio_format = args[3] or 'mp3'
        self.video_format = args[4] or 'mp4'
        self.video_bitrate = args[5] or '320'
        self.playlist = args[6] or False
        self.external_downloader = args[7]
        self.external_downloader_args = args[8]
        self.username = args[9] or ''
        self.password = args[10] or ''
        self.twofactor = args[11] or ''
        self.videopassword = args[12] or ''
        self.proxy = args[13] or ''
        self.geobypass = args[14] or False
        self.thumbnail = args[15] or False

    def add_values(self):
        config = download.get_config()
        incase_of_error = {'Type': self.type,'AFormat': self.audio_format,'VFormat': self.video_format,'VBitrate': self.video_bitrate,'Playlist': self.playlist,'SExternal': self.external_downloader,'SExternalD': self.external_downloader_args,'User': self.username,'Pass': self.password,'TFactor': self.twofactor, 'VPass': self.videopassword, 'Proxy': self.proxy, 'GeoBy': self.geobypass}
        config[self.type]['format'] = self.format
        if self.type == "Audio":
            for x in config[self.type]['postprocessors']:
                x['preferredcodec'] = self.audio_format;x['preferredquality'] = self.video_bitrate
                break
        config[self.type]['preferedformat'] = self.video_format
        if self.playlist == "True": config[self.type]['noplaylist'] = False
        if self.thumbnail == "False": config[self.type]['writethumbnail'] = False
        if str(self.external_downloader) != "None": config[self.type]['external_downloader'] = self.external_downloader
        if str(self.external_downloader_args) != "None": config[self.type]['external_downloader_args'] = self.external_downloader_args
        if self.username != '': config[self.type]['username'] = self.username
        if self.password != '': config[self.type]['password'] = self.password
        if self.twofactor != '': config[self.type]['twofactor'] = self.twofactor
        if self.videopassword != '': config[self.type]['videopassword'] = self.videopassword
        if self.proxy != '': config[self.type]['proxy'] = self.proxy
        if str(self.geobypass) != "None": config[self.type]['geo_bypass'] = self.geobypass
        download.download(self.link, config[self.type],incase_of_error)
        download.output_file(directory[0],titlez[0])


class download():
    # Some Global Variables And lists
    global recog
    com_reso = []
    # Clear The Screen
    def clear():
        if sys.platform in ['win64','win32']:
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
        conv = filename.endswith(".webm")
        exts = extension[0]
        if dir is None:
            if conv:
                filename = filename.split(".w")[0]+f".{exts}"
                print()
                print("\n" + get_colors.randomize() + "["+get_colors.randomize2()+"!"+get_colors.randomize1()+"]" + get_colors.randomize2() + " Converting Sample From [webm] Format")
                print()
                print(get_colors.randomize() + "["+get_colors.randomize2()+"+"+get_colors.randomize1()+"]" + get_colors.randomize2() + " This Might Take Few Seconds/Minutes")
            if os.path.isfile(filename):
                print()
                print('\n' + get_colors.green() + '[' + get_colors.magento() + '+' + get_colors.green() + ']' + get_colors.randomize2() + " Video Saved Undername "+ get_colors.randomize3() + f"['{filename}']" + get_colors.white() + '\n')
                print(get_colors.green() + '[' + get_colors.magento() + '+' + get_colors.green() + ']' + get_colors.white() + ' Folder ' + get_colors.randomize() + os.getcwd())
                print()
        else:
            if conv:
                filename = filename.split(".w")[0]+f".{exts}"
                print()
                print("\n" + get_colors.randomize() + "["+get_colors.randomize2()+"!"+get_colors.randomize1()+"]" + get_colors.randomize2() + " Converting Sample From [webm] Format")
                print()
                print(get_colors.randomize() + "["+get_colors.randomize2()+"+"+get_colors.randomize1()+"]" + get_colors.randomize2() + " This Might Take Few Seconds/Minutes")
            if os.path.isfile(filename):
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
            try: dict = directory[0]
            except: dict = None
            download.get_current_dir(t['filename'],dict)

    # List All Available Resolutions
    def user_resolution():
        available = ['4k','2k','1080p','720p','480p','360p']
        return available


    # Download Configurations
    def get_config():
        config = {
            'Audio': {
                'quiet': True,
                'outtmpl': "%(title)s.%(ext)s",
                'writethumbnail': True,
                'progress_hooks': [download.hooker],
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320'},
                    {'key': 'EmbedThumbnail'},
                    {'key': 'FFmpegMetadata'},]
            },
            'Video': {
                'quiet': True,
                'outtmpl': "%(title)s.%(ext)s",
                'noplaylist': True,
                'no_warnings': True,
                'ignoreerrors': True,
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

    def download(link, data, err):
        try:
            with dl.YoutubeDL(data) as ydl:
                ydl.download([link])
        except dl.utils.ExtractorError:
            print("[!] Exception Occurred While Extracting File ...")
            exit(1)
        except dl.utils.UnsupportedError:
            print("[!] URL Is Not Supported")
            exit(1)
        except dl.utils.GeoRestrictedError:
            print("[!] Video/Audio Is Restricted In Ur Area\n[+] Consider Using [--bypass-geo]")
            exit(1)
        except dl.utils.UnavailableVideoError:
            print("[!] Video/Audio You Requested Is Not Available")
        except dl.utils.DownloadError as e:
            if "Unable to login: Invalid username/password!" in str(e):
                print("\n" + get_colors.randomize() + "["+get_colors.randomize2()+"!"+get_colors.randomize1()+"]" + get_colors.randomize3() + " Can't Login Invalid Username/Password")
            if "requested format not available" in str(e):
                print("\n" + get_colors.randomize() + "["+get_colors.randomize2()+"!"+get_colors.randomize1()+"]" + get_colors.randomize3() + " An Error Occurred While Trying Downloading")
                print(get_colors.randomize() + "["+get_colors.randomize2()+"+"+get_colors.randomize1()+"]" + get_colors.randomize3() + " Trying Automatic Way To Fix The Error")
                err = err; s = parser_args(err['Type'],link,'bestvideo+bestaudio/best',err['AFormat'],err['VFormat'],err['VBitrate'],err['Playlist'],err['SExternal'],err['SExternalD'],err['User'],err['Pass'],err['TFactor'],err['VPass'],err['Proxy'],err['GeoBy'])
                s.add_values()

    # Scrape Link Info ['metadata','thumbnail','uploader'....]
    def get_info(link):
        ydl2 = dl.YoutubeDL({'quiet':True,'no_warnings': True,'ignoreerrors': False})
        try:
            result = ydl2.extract_info(link,download=False)
        except dl.utils.DownloadError:
            exit(1)
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
        return video_title,video_size,max_reso,result

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
    def print_metadata():
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

    # Shortcuts
    def clear_pr():
        download.clear()
        download.buggy()

    # Type Of Download
    def type_down(metadata_inp,link):
        config = download.get_config()
        if metadata_inp in [1,3]:
            download.user_print(option=2)
            reso_inp = download.user_input(option=2)
            if str(reso_inp) == '0': reso_inp = '4k'
            if str(reso_inp) == '1': reso_inp = '2k'
            if str(reso_inp) == '2': reso_inp = '1080p'
            if str(reso_inp) == '3': reso_inp = '720p'
            if str(reso_inp) == '4': reso_inp = '480p'
            if str(reso_inp) == '5': reso_inp = '360p'
            if metadata_inp == 1:
                download.get_me_my_stuff(link,None,reso_inp,0,False,False,False,False,None,None,None,None,None,None,None,None,'mp4',None,False)
            else:
                download.get_me_my_stuff(link,None,reso_inp,0,True,False,False,False,None,None,None,None,None,None,None,None,'mp4',None,False)
        if metadata_inp in [0,2]:
            if metadata_inp == 0:
                download.get_me_my_stuff(link,None,None,0,False,True,False,False,None,None,'320',None,None,None,None,None,None,'mp3',False)
            else:
                download.get_me_my_stuff(link,None,None,0,True,True,False,False,None,None,'320',None,None,None,None,None,None,'mp3',False)
        else: download.user_print(option=0)

    # all out
    def get_over(link):
        title, duration,reso,result = download.get_info(link)
        if duration is not None:
            duration = int(duration)
            duration = m,s = divmod(duration,60)
            duration = h,m = divmod(duration[0], 60)
            duration = (f'{h:d}:{m:02d}:{s:02d}')
        else:
            duration = None
        download.com_reso.append(reso);
        return title,duration,reso

    # BannerAndClear
    def bncl():
        download.clear()
        banner.banner()

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
                        download.print_metadata()
                        metadata_inp = download.user_input(option=1)
                        download.type_down(metadata_inp,link)
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
        usage = "Usage: PrNdOwN [options] url"
        parser = optparse.OptionParser(usage)
        parser.add_option('-c','--cmd', dest="cmd", action="store_true",default=False,help="Use The Traditional Look")
        parser.add_option('-u','--url', dest="url",type="string",help="Video / Audio Url")
        parser.add_option('-C','--config',dest='conf',action="store_true",default=False,help="Read And Use The Config File")
        parser.add_option('-q','--quiet',dest='verbose',action='store_true',default=False,help="Don't print status messages")
        parser.add_option('-f','--file',dest='file',type='string',help='Read a file contains a list of urls then download them all')
        parser.add_option('-o','--output',dest='output',type='string',help='Output File Location')
        parser.add_option('-s','--aria2c',dest='speed',action='store_true',default=False,help='Use External Downlaod (Aria2c)')
        parser.add_option('-t','--external',dest='external',type='string',help='Use Prevered External Downloader (wget,curl,ffmpeg ...)')
        parser.add_option('-T','--external-args',dest='external_args',type='string',help='Set Prevered External Download Args')
        parser.add_option('-r','--config-file',dest='config_file',type='string',help='Use Config file of Your Choice')
        parser.add_option('--proxy',dest='proxy',type='string',help='Proxy To Use')
        parser.add_option('--geobypass',dest='geobypass',action='store_true',default=False,help='Geo Location Bypass')
        group = optparse.OptionGroup(parser, "Video / Audio",
          "This Options Can Be Used To Select Video / Audio Like Quality / Format ...")
        group.add_option('-a','--audio-quality',dest='audio_qual',type='int',help='Specify Audio Quality Between 0 and 1 (0 is the best 1 is the worse)')
        group.add_option('-v','--video-quality',dest='video_qual',type='string',help='Specify Video Quality Between 4k To 360 (4k,2k,1080p,720p,480p,360p)')
        group.add_option('-V','--video-format',dest='videoformat',type='string',help='Video Format To Use ex (mp4,mkv..)')
        group.add_option('-A','--audio-format',dest='audioformat',type='string',help='Audio Format To Use ex (mp3,flac..)')
        group.add_option('-b','--audio-bitrate',dest='aud_bitrate',type='string',help="Audio Bitrate Default (320kbit)")
        group.add_option('-x','--extract-audio',dest='extract',action='store_true',help='Extract Audio From a video source')
        group.add_option('-l','--thumbnail',dest='thumbnail',action='store_true',help='EmbedThumbnail To Video/Audio')
        group.add_option('-p','--playlist',dest='playlist',action="store_true",default=True,help='Download A Playlist With Specified URL')
        parser.add_option_group(group)
        group2 = optparse.OptionGroup(parser, "Authentication Options",
          "This Options Can Be Used To Set Authentication Method")
        group2.add_option('-U','--username',dest='username',type='string',help='Username To Authenticate With')
        group2.add_option('-P','--password',dest='password',type='string',help='Password To Authenticate With')
        group2.add_option('--twofactor',dest='factor_two',type='string',help='2 Factor Authentication Code')
        group2.add_option('--videopassword',dest='video_password',type='string',help='Video Password To Use')
        parser.add_option_group(group2)
        (options,args) = parser.parse_args()
        return options,args

    # Check Aria2c
    def aria2c_usage(extr,extr_args,usage=False):
        if usage:
            if spawn.find_executable('aria2c'):
                external = 'aria2c'
                external_args = ['-x16','-k1M']
                return external,external_args
            else: print("[!] 'aria2c' Was Not Found ! ");sys.exit(1)
        elif extr != None:
            external = extr
            if extr_args is None:
                extr_args = ['']
            else:
                extr_args = list(extr_args.split(" "))
                external_args = extr_args
            return external,external_args
        else:
            return None,None

    # Use HLS Format
    def hls_video(quality):
        available_format = download.com_reso[0]
        if "hls" in available_format:
            if quality in ['1080p','720p','480p','360p']:
                hls_qual = f"hls-{quality}"
            else:
                hls_qual = quality
        else:
            return quality
        return hls_qual

    # For Sake of Time
    def move_file(src,loc):
        try:
            shutil.move(src,loc)
        except:
            try:
                src = src.split(".")[0] + '.mp3'
                shutil.move(src,loc)
            except Exception as e:
                print("File not found ! Thus We Cannot Move it")
                print(e)

    def playlist_checker(link):
        url = link.split("&");lene = len(url)
        if lene==3:
            print("[+] This Playlist Type Is Not Supported")
            print("[+] Going With Video ID {%s} In The Giving URL "%(url[0]).split("=")[1])
            playlist_link.append(url[0])
        elif lene==2:
            playlist_link.append(link)
        else:
            return


    # Where To Save File
    def output_file(location,title):
        if platform in ['win64','win32']:
            if location.endswith('\\'): pass
            else: location = location+"\\"
        if location.endswith('/'): pass
        else: location = location+"/"
        if extension[0] == None: extension.clear();extension.append('mp4')
        src = title+"."+extension[0]
        if os.path.isdir(location):
            download.move_file(src,location)
        else:
            print("[!] Directory Not Found")

    # Check If Resolution Matches 4k and 2k
    def check_4k_2k(reso,username,password):
        recog = download.recog
        if reso in ["4k","2k"] and str(username) == "None" and str(password) == "None" and recog == True: pass
        if reso in ["4k","2k"] and str(username) == "None" and str(password) == "None" and recog == False: print(get_colors.red() + "[" + get_colors.white() + "!" + get_colors.red() + "]" + get_colors.white() + " The Platform You're Trying To Download 4k/2k Content From Requires Username/Password \n" + get_colors.sharp_green() + "[" + get_colors.red() + "+" + get_colors.sharp_green() + "]" + get_colors.white() + " It Will Fail Trying To Grab The Content And It Will Defaults Back To The Best Quality Automatically")

    # This is a fix for PH formats changing to hls which messed up everything
    def check_ph_hls(url,reso):
        a,b,c,r = download.get_info(url)
        r = r['formats']
        if reso == "4k": s = "3840x2160"
        if reso == "2k": s = "2560x1440"
        if reso == "1080p": s = "1920x1080"
        if reso == "720p": s = "1280x720"
        if reso == "480p": s = "854x480"
        if reso == "360p": s = "426x240"
        for item in r:
          if s in item['format']:
              return item['format_id']

    # Save Few Lines Of Code
    def display_info(url):
        download.url_recognition(url)
        title,duration,resolution = download.get_over(url)
        titlez.append(title)
        download.print_metadata2(title,duration,resolution)
        sl(3)

    def get_me_my_stuff(url,output,video_qual,audio_qual,playlist,extract_audio,quiet,aria2c,external,external_args,aud_bitrate,username,password,vid_password,two_factor,proxy,vid_format,aud_format,geobypass,thumbnail):
        if not valid.url(url):
            download.user_print(option=1)
            return
        external,external_args = download.aria2c_usage(external,external_args,aria2c)
        download.playlist_checker(url)
        if playlist_link == []: pass
        else: url = playlist_link[0]
        if output != None: directory.append(output)
        else: directory.append(os.getcwd())
        if download.check_url("https://google.com") and download.check_connection(url):
            if quiet == False:
                if audio_qual == None: audio_qual = randint(2,4)
                if audio_qual >= 0 and video_qual == None and extract_audio == None:
                    video_qual = '1080p'
                if extract_audio == False or extract_audio == None:
                    download.bncl()
                    extension.append(vid_format)
                    download.display_info(url)
                    download.check_4k_2k(video_qual,username,password)
                    if video_qual in ['4k','2k','1080p','720p','480p','360p']: pass
                    else: download.user_print(option=4);exit(1)
                    video_qual = download.check_ph_hls(url,video_qual)
                    video_qual = download.hls_video(video_qual)
                    s = parser_args("Video",url,video_qual,aud_format,vid_format,aud_bitrate,str(playlist),external,external_args,username,password,two_factor,vid_password,proxy,bool(geobypass),thumbnail)
                    s.add_values()
                else:
                    download.bncl()
                    download.display_info(url)
                    extension.append(aud_format)
                    if audio_qual == 0: q = 'bestaudio/best'
                    elif audio_qual == 1: q = 'worstaudio/worst'
                    else: q = 'bestaudio/best'
                    s = parser_args("Audio",url,q,aud_format,None,aud_bitrate,str(playlist),external,external_args,username,password,two_factor,vid_password,proxy,bool(geobypass),thumbnail)
                    s.add_values()
            else:
                if audio_qual == None: audio_qual = randint(2,4)
                if audio_qual >= 0 and video_qual == None and extract_audio == None:
                    video_qual = '1080p'
                if extract_audio == False or extract_audio == None:
                    download.display_info(url)
                    download.check_4k_2k(video_qual,username,password)
                    if video_qual in ['4k','2k','1080p','720p','480p','360p']: pass
                    else: download.user_print(option=4);exit(1)
                    video_qual = download.check_ph_hls(url,video_qual)
                    video_qual = download.hls_video(video_qual)
                    s = parser_args("Video",url,video_qual,aud_format,vid_format,aud_bitrate,str(playlist),external,external_args,username,password,two_factor,vid_password,proxy,bool(geobypass),thumbnail)
                    s.add_values()
                else:
                    extension.append(aud_format)
                    download.display_info(url)
                    if audio_qual == 0: q = 'bestaudio/best'
                    elif audio_qual == 1: q = 'worstaudio/worst'
                    else: q = 'bestaudio/best'
                    s = parser_args("Audio",url,q,aud_format,None,aud_bitrate,str(playlist),external,external_args,username,password,two_factor,vid_password,proxy,bool(geobypass),thumbnail)
                    s.add_values()

    # Probably The all
    def kick_it(file,output,audio_qual,video_qual,aud_bitrate,external,external_args,username,password,video_password,two_factor,proxy,vid_format,aud_format,url=None,quiet=False,extract_audio=False,playlist=False,aria2c=False,geobypass=False,thumbnail=True):
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
                                download.get_me_my_stuff(url,output,video_qual,audio_qual,playlist,extract_audio,quiet,aria2c,external,external_args,aud_bitrate,username,password,two_factor,video_password,proxy,vid_format,aud_format,geobypass,thumbnail)
                                times += 1
                            else:
                                break
            else:
                download.get_me_my_stuff(url,output,video_qual,audio_qual,playlist,extract_audio,quiet,aria2c,external,external_args,aud_bitrate,username,password,two_factor,video_password,proxy,vid_format,aud_format,geobypass,thumbnail)


    # The Holy Engine
    def runner():
        options, args = download.command_line()
        url = options.url
        file = options.file
        if url == None:
            try:url = args[0]
            except: pass
        if options.conf or options.config_file != None:
            try: config_reader.find_config(options.config_file)
            except: config_reader.find_config('config.rc')
            output = default_conf[0]
            audio_quality = default_conf[3]
            video_quality = default_conf[1]
            vid_format,audio_format = default_conf[11]
            aud_bitrate = default_conf[12]
            quiet = default_conf[5]
            playlist = default_conf[6]
            extract_audio = default_conf[4]
            aria2c = default_conf[7]
            external = default_conf[8]
            external_args = default_conf[9]
            proxy = default_conf[10]
            geobypass = default_conf[13]
            thumbnail = default_conf[14]
            username = options.username
            password = options.password
            vid_password = options.video_password
            factor = options.factor_two
        else:
            output = options.output
            audio_quality = options.audio_qual
            video_quality = options.video_qual
            quiet = options.verbose
            playlist = options.playlist
            extract_audio = options.extract
            aria2c = options.speed
            external = options.external
            external_args = options.external_args
            aud_bitrate = options.aud_bitrate
            username = options.username
            password = options.password
            vid_password = options.video_password
            factor = options.factor_two
            proxy = options.proxy
            vid_format = options.videoformat
            audio_format = options.audioformat
            geobypass = options.geobypass
            thumbnail = options.thumbnail
        if options.cmd:
            download.run()
        download.kick_it(file,output,audio_quality,video_quality,aud_bitrate,external,external_args,username,password,vid_password,factor,proxy,vid_format,audio_format,url,quiet,extract_audio,playlist,aria2c,geobypass,thumbnail)
