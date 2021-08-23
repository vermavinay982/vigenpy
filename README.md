# vigenpy
Video Generation Package

## Installing Library
```bash
pip install vigenpy
```

## Sample Code to Start Using
```python
from vigenpy.video import stack_video
videos = ['archery.mp4','cycling.mp4']
stack_video(videos, axis=0) 
```