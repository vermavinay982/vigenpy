import os
import pytest
import wget
from vigenpy.video.video import Video
from vigenpy.video.stitcher import VideoStitcher

@pytest.fixture
def video_path():
    path = "tests/Big_Buck_Bunny_360_10s_1MB.mp4"
    if not os.path.exists(path):
        wget.download("https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4", out=path)
    return path

@pytest.fixture
def video_path_2():
    path = "tests/Jellyfish_360_10s_1MB.mp4"
    if not os.path.exists(path):
        wget.download("https://test-videos.co.uk/vids/jellyfish/mp4/h264/360/Jellyfish_360_10s_1MB.mp4", out=path)
    return path

def test_video_creation(video_path):
    video = Video(video_path)
    assert video.is_opened()
    assert video.width == 640
    assert video.height == 360
    assert video.fps == 30.0
    assert video.frame_count == 300
    video.release()

def test_video_read(video_path):
    video = Video(video_path)
    ret, frame = video.read()
    assert ret
    assert frame.shape == (360, 640, 3)
    video.release()

def test_video_stitcher(video_path, video_path_2):
    videos = [Video(video_path), Video(video_path_2)]
    stitcher = VideoStitcher(videos, size=(300, 300), axis=0)
    output_path = "tests/output.mp4"
    path, duration = stitcher.stitch(output_path, writer_fps=24.0, duration=2)
    assert os.path.exists(path)
    assert duration == 2.0
    os.remove(path)
