__author__      = "Vinay Verma"
__copyright__   = "Copyright 2021, Vinay Verma"
__credits__     = ["Vinay Verma"]
__license__     = "MIT"
__version__     = "0.3.0"
__maintainer__  = "Vinay Verma"
__email__       = "vermavinay982@gmail.com"
__module_name__ = "[Stack Video]"

import os
import cv2
import time
import numpy as np
from tqdm import tqdm

def write_video(frame_list, video_name, output_shape, writer_fps, duration):
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    height, width = output_shape

    if duration is not None:
        stop_frame = writer_fps * duration
    
    out = cv2.VideoWriter(video_name, fourcc, int(writer_fps), (width, height))
    frame_counter = 0
    for encoded_frame in tqdm(frame_list):
        frame_encoded = np.frombuffer(encoded_frame, np.uint8)
        frame = cv2.imdecode(frame_encoded, cv2.IMREAD_COLOR)
        out.write(frame)

        frame_counter+=1
        
        if duration is not None:
            if frame_counter>stop_frame:
                break # Video Duration Achieved

    out.release()

    total_duration = frame_counter/writer_fps
    return video_name, total_duration

def axis_stack(caps, videos, size, axis, display):
    frame_list = list() # storing video frames to write
    past_frame=[]
    start = True
    video_over = False

    while True:
        frames = []
        for i,cap in enumerate(caps):
            ret, frame = cap.read()
            if not ret:
                # Video Still Not Over, Loop Again
                caps[i] = cv2.VideoCapture(videos[i])
                print('Video Ended, RESTARTING',videos[i])
                frame = past_frame[i]

                # Limiting Video Ended, Stop Now
                if i==limit_video:
                    print(f'{videos[i]} Video Ended, Stopping Now',)
                    video_over = True
                # break # stop for both cams later will buffer

            if start:
                # only initialize at start
                # Save Past in case of frame drop
                start = False
                past_frame = [frame for i in videos] 

            past_frame[i]=frame
            frame = cv2.resize(frame, size)
            frames.append(frame) # combined frames in array
        
        if video_over: break
        
        if axis==0:
            resized_frame = np.hstack(frames)
        
        if axis==1:
            resized_frame = np.vstack(frames)

        output_shape = resized_frame.shape[:2]
        flag, encoded_frame = cv2.imencode('.jpg', resized_frame)
        frame_list.append(encoded_frame)

        if display:
            cv2.imshow('test',resized_frame)
            wait_key = cv2.waitKey(1)

            if ord('q')==wait_key or ord('Q')==wait_key:
                break
    return frame_list, output_shape

def time_stack(caps, videos, size, display):
    frame_list = list() # storing video frames to write
    for i,cap in enumerate(caps):
        while True:
            ret, frame = cap.read()
            if not ret:
                print('Video Ended, Closed',videos[i])
                break # frame is NONE

            resized_frame = cv2.resize(frame, size)
            output_shape = resized_frame.shape[:2]
            flag, encoded_frame = cv2.imencode('.jpg', resized_frame)
            frame_list.append(encoded_frame)

            if display:
                cv2.imshow('test',resized_frame)
                wait_key = cv2.waitKey(1)

                if ord('q')==wait_key or ord('Q')==wait_key:
                    break
    return frame_list, output_shape

def stack_video(
    videos:list=[],
    axis:int=0,
    size=(300,400), 
    limit_video=None, 
    write_path=None,
    writer_fps=None,
    display=False,
    duration=None
    )->str:
    """
    stack_video

    Write or display the video after stacking it
    """
    if limit_video is None and write_path is not None:
        print("Cant write an infinite video, Keep a limit video")
        return None

    for video in videos:
        if not os.path.exists(video):
            print(f'Video {video} Not There')
            return None
        else:
            print(f'Video {video} Found')

    caps = [cv2.VideoCapture(cam) for cam in videos]
    fps  = min([cap.get(cv2.CAP_PROP_FPS) for cap in caps])
    print(f"Min FPS of All Videos is :{fps:.2f}")

    if axis==2:
        frame_list, output_shape = time_stack(caps, videos, size, display=display)

    if axis==1:
        frame_list, output_shape = axis_stack(caps, videos, size, axis=axis, display=display)

    if axis==0:
        frame_list, output_shape = axis_stack(caps, videos, size, axis=axis, display=display)

    if writer_fps is None:
        writer_fps = fps

    if write_path:
        video_name, vid_duration = write_video(frame_list, write_path, output_shape, writer_fps=writer_fps, duration=duration)        
        print(f"Video written sucessfully at :{video_name} || With Duration {vid_duration:.2f} seconds")
        return video_name
    
    if display:
        cv2.destroyAllWindows()
    return None

if __name__ == '__main__':
    
    path1 = '../../../archery.mp4'
    path2 = '../../../cars.mp4'

    videos = [path1, path2]
    video_size = (300,300) # w/h
    limit_video = 0 # video index, that will decide to close streaming
    video_path = 'test.mp4'
    video_duration = 4 # in seconds default None

    output_video = stack_video(
                            videos,
                            axis=2,
                            size=video_size,
                            limit_video=limit_video, 
                            write_path=video_path,
                            writer_fps=None, 
                            display=True,
                            duration=video_duration)
    print(output_video)