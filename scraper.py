import re
import requests
import instaloader
from transcriber import Transcribe

class Scraper:
    def __init__(self):
        self.loader = instaloader.Instaloader()
        self.shortcode_value = None
        self.username = None
        self.caption = None
        self.duration = None
        self.like_count = None
        self.view_count = None
        self.video_url = None
        self.video_path = None
        self.posted_at = None
        self.caption_hash = None
        self.transcript = None
        self.segments = None

    '''Each instagram reel has a code attached to it, it has a partciular
    format to it, and that is how the library gets to know what video to 
    download and scrape'''
    def extract_shortcode(self, link):
        match = re.search(r'/reel/([^/?]+)', link)
        if match:
            self.shortcode_value = match.group(1)
            return self.shortcode_value
        else:
            print("Invalid link! Could not extract shortcode.")
            return None

    def fetch_metadata(self):
        """This way all the data is stored in each attribute like we want, The response 
        block of code is complex as it sends a HTTP GET request to the instagram post and then
        loads the video in chunks as the videos can lowkey be a lil big"""
        post = instaloader.Post.from_shortcode(self.loader.context, self.shortcode_value)
        self.username = post.owner_username
        self.caption = post.caption
        self.caption_hash = post.caption_hashtags
        self.duration = post.video_duration
        self.like_count = post.likes
        self.view_count = post.video_view_count
        self.posted_at = post.date


        video_url = post.video_url
        response = requests.get(video_url, stream=True)
        self.video_path = r"C:\Users\MOHAMMED SOHAIL ALI\OneDrive\Desktop\employment\Personal Project\Storage-Unit" + "\\" + self.shortcode_value + ".mp4"

        with open(self.video_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)


        t = Transcribe(self.video_path)
        self.transcript, self.segments = t.run()
    
    def display_segments(self):
        """Display segments first, then the words in each segment."""
        print("=== SEGMENTS ===")
        for segment in self.segments:
            print(f"ID: {segment['id']}")
            print(f"Text: {segment['text']}")
            print(f"Start: {segment['start']}")
            print(f"End: {segment['end']}")
            print(f"Confidence: {segment['confidence']}")
            print("Words:")
            for word in segment['words']:
                print(f"  - Word: {word['word']}, Start: {word['start']}, End: {word['end']}, Confidence: {word['confidence']}")
            print("-" * 50)
    
    def make_dict(self):
        return {
            "shortcode": self.shortcode_value,
            "username": self.username,
            "caption": self.caption,
            "caption_hashtags":self.caption_hash,
            "duration": f"{self.duration}s",
            "like_count": self.like_count,
            "view_count": self.view_count,
            "video_path": self.video_path,
            "posted_at": str(self.posted_at),
            "transcript": self.transcript,
            "segments": self.segments
        }
         
    
    def display_metadata(self):
        data = self.make_dict()
        for key,value in data.items():
            if key != "segments":
                print(f"|{key}| :|{value}|")
        self.display_segments()

    def scrape_reel(self,link):
        if self.extract_shortcode(link):
            self.fetch_metadata()
            self.display_metadata()
            return self.make_dict()
        else:
            print("Failed to scrape reel: invalid link.")
            return None
