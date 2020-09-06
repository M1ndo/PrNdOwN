#!/usr/bin/python3
# Updated In 00/04/2020
# Created By Ybenel(r2dr0dn)
import sys
sys.path.insert(1, 'src')
from src.downloader import download
from src.colors import get_colors

def main():
    try:
        download.runner()
    except KeyboardInterrupt as ky:
        print(get_colors.yellow()+get_colors.red() + "\n[!] CTRL+C Detected \n"+get_colors.cyan()+"Thanks For Usage :)"+get_colors.white())
if __name__ == "__main__":
    main()
