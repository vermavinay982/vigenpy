# vigenpy
## Video Generation Package

- Project URL: https://pypi.org/project/vigenpy/
- Github URL: https://github.com/vermavinay982/vigenpy
- Intro & Demo Video: https://youtu.be/shr7d-4P5IA

Having 2 videos and you want to merge them? Tell what side by side, top and bottom, or just wrt time - you can do that too just by choosing the axis where you want to attach the video at.

## Installing Library
```bash
pip install vigenpy
```
![image](https://github.com/vermavinay982/vigenpy/blob/main/documents/demo.gif?raw=true)

Suppose you have trained a model, and want to run comparison on 2 different videos at same time. This tool will help you to choose any axis of placing the frame - you can directly stack 2 videos like lego bricks and it will work for you as single video. You can even process 2 videos individually with different ML model and can put them side by side for comparison - cool just give their path - rest the algo will deal with it. you can even process indiviually and process it later - its very easy.

`Future update` will have shuffle too - meaning one frame of 1st then one from 2nd then again from 1st.
Its upto you what amazing you can do with this tool. Feel free to contribute and add more features in this package. 

`vigenpy` is a video generation library. It enables the developer to generate a new video by merging 2 or more videos in one video.
It is a flexible library that provides you total flexibility.

# Axis Stacking
It has 3 axis 
- axis 0 - horizontal x axis - side by side videos
- axis 1 - vertical y axis - top and bottom merge of videos
- axis 2 - that is back to back - video will be generated combining the 2 videos in time axis
- axis 3 - shuffle in the middle - one frame this another that - again first 1,2,1,2,1,2.....(Future Update)

The video path or the stream path is given as list 
and based on the list - the precedence is decided for stacking the video together

## There are multiple modes in the code
1. Show Video as Output:
	just show the combined video to the user 
	you can just pass the frames and it will merge it to create video output
	or if you want to show you can do

2. Video Output Generation: 
	provide the path of output and the program will generate a video merged for you 
	you can set the time or #frames to get the generated video for.
	initially the longer video - and shorter video will run on loop until longer one is over
	or the shorter video will be used to break the loop irrespective of longer video time
	use_time_of = 0,1 whatever - that will be used to generate the video

3. If you want to fetch frames that are merged so you can do other things
	that you can process the frames and use it at your end.


## Sample Code to Start Using
```python
from vigenpy.video import stack_video

videos = ['archery.mp4','cycling.mp4']
stack_video(videos, axis=0, write_path='mixed.mp4') 
```

## Advanced Way to Use
```python
from vigenpy.video import stack_video

path1 = '../../../archery.mp4'
path2 = '../../../cars.mp4'

videos = [path1, path2, path1, path2]
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
```


- License: MIT
- Author: [Vinay Kumar Verma](mailto:vermavinay982@gmail.com) 
- Maintainer: [Vinay Kumar Verma](mailto:vermavinay982@gmail.com) 
