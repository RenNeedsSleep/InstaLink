import cv2

class Frame:
    def __init__(self,video_path, transcript, output_path):
        self.frames = []
        self.video_path = video_path
        self.segments = transcript if transcript else []
        self.output_path = output_path

    def extractor(self):
        cam = cv2.VideoCapture(self.video_path)

        timestamp = self.calculate_timestamps()

        if not timestamp:
            # cv2.CAP_PROP_DURATION doesn't exist; calculate from frame count and FPS
            frame_count = cam.get(cv2.CAP_PROP_FRAME_COUNT)
            fps = cam.get(cv2.CAP_PROP_FPS)
            duration = int(frame_count / fps) if fps > 0 else 0
            for ts in range(0, duration, 5):
                timestamp.append(ts * 1000)  # expects timestamps in milliseconds
            
            


        success, count = True, 0
        for ts in timestamp:
            cam.set(cv2.CAP_PROP_POS_MSEC, ts)
            success, image = cam.read()
            if success: 
                frame_path = f"{self.output_path}\\frame_{count}.jpg"
                cv2.imwrite(frame_path, image) # Save frame
                self.frames.append(frame_path)
                count += 1


        cam.release()

    def calculate_timestamps(self):

        timestamp = []

        keywords = ['check this','check bio','this website']

        for sentence in self.segments:
            if any(keyword in sentence["text"] for keyword in keywords):
                timestamp.append(sentence['start']*1000)

        return timestamp
        