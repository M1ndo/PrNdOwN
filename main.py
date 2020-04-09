#!/usr/bin/python3
# Updated In 00/04/2020
# Created By Ybenel
import sys
sys.path.insert(1, 'src')
from src.downloader import download
from src.colors import get_colors
# def main():
#     try:
#         download.run()
#     except KeyboardInterrupt:
#         print(get_colors.white()+"CTRL+C Detected \nCYA NEXT TIME")
# if __name__ == "__main__":
#     main()


def main():
    try:
        download.run()
    except KeyboardInterrupt as ky:
        print(get_colors.yellow()+get_colors.red() + "\n[!] CTRL+C Detected \n"+get_colors.cyan()+"Thanks For Usage :)")
if __name__ == "__main__":
    main()   
