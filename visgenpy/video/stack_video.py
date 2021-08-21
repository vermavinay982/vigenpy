__author__      = "Vinay Verma"
__copyright__   = "Copyright 2021, Vinay Verma"
__credits__     = ["Vinay Verma"]
__license__     = "MIT"
__version__     = "0.1.0"
__maintainer__  = "Vinay Verma"
__email__       = "vermavinay982@gmail.com"
__module_name__ = "[Stack Video]"

import numpy as np
import cv2

def write_video(frame_list, video_name, resized_frame, writer_fps):
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    height, width = resized_frame.shape[:2]

    out = cv2.VideoWriter(video_name, fourcc, int(writer_fps), (width, height))
    for encoded_frame in tqdm(window_frame_list):
        frame_encoded = np.frombuffer(encoded_frame, np.uint8)
        frame = cv2.imdecode(frame_encoded, cv2.IMREAD_COLOR)
        out.write(frame)
    out.release()
    return video_name

def stack_video(videos:list=[], axis:int=0)->str:
    frame_list = list()
    caps = [cv2.VideoCapture(cam) for cam in videos]
    size = (300,400)
    past_frame=[]
    start = True
    while True:
        frames = []
        for i,cap in enumerate(caps):
            ret, frame = cap.read()
            if not ret:
                caps[i] = cv2.VideoCapture(videos[i])
                print('Video Ended, RESTARTING',videos[i])
                frame = past_frame[i]
                # continue
                # break # stop for both cams later will buffer
            if start:
                start = False
                past_frame = [frame, frame]
                    
            past_frame[i]=frame
            frame = cv2.resize(frame, size)
            frames.append(frame)

        if axis==0:
            resized_frame = np.hstack(frames)
        
        if axis==1:
            resized_frame = np.vstack(frames)

        cv2.imshow('test',resized_frame)
        if ord('q')==cv2.waitKey(1):
            break  
            
    # _, encoded_frame = cv2.imencode('.jpg', resized_frame)
    # frame_list.append(encoded_frame)


if __name__ == '__main__':
    
    path1 = '../../archery.mp4'
    path2 = '../../cars.mp4'
    videos = [path1, path2]
    stack_video(videos, axis=1)