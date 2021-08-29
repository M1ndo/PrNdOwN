# PrNdOwN

[PrNdOwN](https://github.com/m1ndo/PrNdOwN) Is a Tool To Download Ultra HD Videos From Multi Video Sharing Websites  (Made Just For Fun)

## Installation Requirements :heavy_check_mark: ##
```
           Linux  

       Arch Linux (AUR)
yay -S phantomjs
pip install -r requirements.txt

       Debian/Ubuntu
sudo apt install phantomjs
pip3 install -r requirements.txt
```
```
           MacOs
sudo brew install phantomjs
pip3 install -r requirements.txt
```
```
           Windows
requires python 3.3.5+ and ffmpeg installed and accessible from CMD
pip install -r requirements.txt
```
# Optional Requirements
- For Fast Download Speeds Please Install (Aria2 Or Curl Or Wget ...)

## Commands :pencil:  ##

```    Display Help
python main.py --help

       Download A Single Video in (1080p)
python main.py -u <URL> or python main.py <URL>

       Download A Single Audio (High Quality)
python main.py -a 0 -x -u <URL>

      Download A Single Video In Prevered quality
python main.py -v 4k -u <URL>

      Download A Single Audio File And Specify A Custom Output location
python main.py -a 0 -x -o /home/ybenel/Music/ -u <URL>

      Download A Video Playlist And Do Not Output Any Information About Video
python main.py -p -u <URL>

      Download A Video / Audio With Custom Config file
python main.py -r -u <URL>

      Download A Video / Audio List From a file
python main.py -v 1080 -f links.txt
      
      Download A Video / Audio With Aria2c For Fast Download Speeds
python main.py -v 1080 -s <URL>

      Download A Video / Audio With A Different Utility
python main.py -v 1080 -t wget --external-args "-S --user-agent='PrNdOwN/9.1.1'" <URL>
```

## Important Notes ##
- Use The Help Menu To See All Available Command Line option 
- Read The Config File To Customize All Your Options
- In Linux You Can Set Your Config File Either In '~/.config/PrNdOwN' Or Inside Of PrNdOwN itself
- In Windows Config File Can Only Be Available In PrNdOwN Itself

**If You Have Ideas To Improve PrNdOwN, Then Fork This Repository And Push A Pull Request**

## Features ##
- Multi Video Platform Downloader
- Download From Youtube - Soundcloud - Twitter - PH - Erotic Sites etc.
- HD Quality (depends on video(s) resolution)
- Multiple Qualities (4k - 2k - 1080p - 720p - 480p - 360)
- Fast Downloading Speed (Again Depends On Your Bandwidth Speed)
- Supports Proxy Through SOCKS/Http (You Might Get Slow Speed While Downloading)
- Download Multiple Choices (Playlist audio / video, single audio / video)
- Having Fun :star:

## Author: ybenel
## LICENSE :page_with_curl: ##
[MIT License]
