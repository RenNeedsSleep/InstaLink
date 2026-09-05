# 📹 Instagram Reel Analyzer

A Python tool that scrapes Instagram Reels, transcribes their audio with word-level timestamps, and extracts key video frames based on transcript content.

## ✨ Features

- **Reel Scraping** — Downloads video and extracts metadata (caption, hashtags, likes, views, post date) via [Instaloader](https://instaloader.github.io/).
- **Audio Transcription** — Converts video to WAV and transcribes using [Whisper](https://github.com/openai/whisper) with word-level timestamps.
- **Smart Frame Extraction** — Pulls key frames from the video at moments that match configurable keywords (e.g. *"check this"*, *"check bio"*).
- **Structured Output** — Returns all data (metadata + transcript + segments) as a clean Python dictionary.

## 🗂️ Project Structure

```
.
├── main.py               # Entry point — prompts for a reel link and runs the pipeline
├── scraper.py            # Scraper class — fetches metadata, downloads video, orchestrates transcription
├── transcriber.py        # Transcribe class — audio extraction, Whisper transcription, frame extraction
├── frame_extractor.py    # Frame class — extracts frames at keyword-matched timestamps
├── Storage-Unit/         # Runtime directory for downloaded videos, audio, and extracted frames
├── requirements.txt      # Python dependencies
└── .gitignore
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+**
- **FFmpeg** — must be installed and available on your system `PATH`.  
  Download: <https://ffmpeg.org/download.html>

### Installation

```bash
# Clone the repo
git clone https://github.com/<your-username>/instagram-reel-analyzer.git
cd instagram-reel-analyzer

# Create a virtual environment
python -m venv venv

# Activate it
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Usage

```bash
python main.py
```

You will be prompted to paste an Instagram Reel link. The tool will then:

1. Extract the shortcode from the URL
2. Fetch reel metadata (caption, likes, views, etc.)
3. Download the video
4. Extract audio → transcribe with Whisper (medium model)
5. Extract key frames based on keyword matching
6. Print all structured data to the console

## ⚙️ Configuration

| Setting | Location | Default |
|---|---|---|
| Whisper model size | `transcriber.py` → `transcribe()` | `"medium"` |
| Whisper model cache | `transcriber.py` → `transcribe()` | `C:\whisper_models` |
| Frame keywords | `frame_extractor.py` → `calculate_timestamps()` | `['check this', 'check bio', 'this website']` |
| Fallback frame interval | `frame_extractor.py` → `extractor()` | Every 5 seconds |

## 🛠️ Tech Stack

| Library | Purpose |
|---|---|
| [Instaloader](https://instaloader.github.io/) | Instagram data access |
| [Requests](https://docs.python-requests.org/) | HTTP video download |
| [OpenCV](https://opencv.org/) | Video frame extraction |
| [ffmpeg-python](https://github.com/kkroening/ffmpeg-python) | Audio extraction from video |
| [whisper-timestamped](https://github.com/linto-ai/whisper-timestamped) | Speech-to-text with word timestamps  |

## 📝 License

This project is for educational and personal usage.

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.
