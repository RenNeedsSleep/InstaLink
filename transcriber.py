import os
# pyrefly: ignore [missing-import]
import ffmpeg
# pyrefly: ignore [missing-import]
import whisper_timestamped as whisper

from frame_extractor import Frame


class Transcribe:
    def __init__(self,video_path):
        self.video_path = video_path
        self.audio_path = video_path.replace(".mp4",".wav")
        self.transcript = None
        self.segments = None


    def extract_audio(self):
            (
                    ffmpeg.input(f'{self.video_path}')
                    .output(f'{self.audio_path}')
                    .run(overwrite_output = True)
            )

    def transcribe(self):

        if not os.path.exists(self.audio_path):
            print("No audio file detected")
            return None
        
        else:
            model = whisper.load_model("medium", download_root="C:\\whisper_models")
            result = whisper.transcribe(model,self.audio_path)

            self.transcript = result["text"]
            self.segments = result["segments"]

            return self.transcript
        
    def format_segments(self):
         """We need the id, start, end, text the words list, and confidence"""
         formatted_segments = []
         for segment in self.segments:
                formatted_words = []
                for word in segment['words']:
                    word_dict = {
                        "word": word['text'],
                        "start": word['start'],
                        "end": word['end'],
                        "confidence": word['confidence']
                    }
                    formatted_words.append(word_dict)
                
                seg_dict = {
                    "id": segment['id'],
                    "text": segment['text'],
                    "start": segment['start'],
                    "end":segment['end'],
                    "confidence":segment['confidence'],
                    "words": formatted_words
                }
                formatted_segments.append(seg_dict)
         return formatted_segments    
                
        
    def run(self):
         self.extract_audio()
         self.transcribe()
         segments = self.format_segments() if self.segments else []

         extractor = Frame(video_path=self.video_path,transcript=segments,output_path="C:\\Users\\MOHAMMED SOHAIL ALI\\OneDrive\\Desktop\\employment\\Personal Project\\Storage-Unit")
        
         extractor.extractor()
         return self.transcript, segments