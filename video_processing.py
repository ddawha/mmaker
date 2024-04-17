import cv2
import os

def process_video(video_path):
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite("TrainingVideos/GenImages/frame%d.jpg" % count, image)     # save frame as JPEG file   
        #img_path = f"TrainingVideos/GenImages/frame{count}.jpg"
        #print(f"Image location: {os.path.abspath(img_path)}")   
        success, image = vidcap.read()
        count += 1
