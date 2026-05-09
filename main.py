import re
import subprocess
from scraper import Scraper
from frame_extractor import Frame

#https://www.instagram.com/reel/DVlwrPeCB9i/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==

def main():
    scraper = Scraper()
    link = input("paste thy link here: ")
    data = scraper.scrape_reel(link)
    print(data)



    


if __name__ == '__main__':
    main()