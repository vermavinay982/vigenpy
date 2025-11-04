__author__ = "Vinay Verma"
__copyright__ = "Copyright 2021, Vinay Verma"
__credits__ = ["Vinay Verma"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Vinay Verma"
__email__ = "vermavinay982@gmail.com"
__module_name__ = "[Stack Video]"

import os
from .video import Video
from .stitcher import VideoStitcher


def stack_video(
    videos: list[str],
    axis: int = 0,
    size: tuple[int, int] = (300, 400),
    write_path: str = None,
    writer_fps: float = None,
    duration: int = None
) -> str:
    """Stitches multiple videos together and saves the output.

    This function takes a list of video paths, creates video objects for each,
    and then uses a VideoStitcher to combine them. The output video is saved
    to the specified path.

    Args:
        videos (list[str]): A list of paths to the video files.
        axis (int, optional): The axis for stacking videos. 0 for horizontal,
                              1 for vertical, 2 for time-based. Defaults to 0.
        size (tuple[int, int], optional): The desired output size (width, height)
                                          for each video frame. Defaults to (300, 400).
        write_path (str, optional): The path to save the output video file.
                                    If None, the video will not be saved. Defaults to None.
        writer_fps (float, optional): The frames per second for the output video.
                                      If None, the minimum FPS of the input videos will be used.
                                      Defaults to None.
        duration (int, optional): The desired duration of the output video in seconds.
                                  If None, it will be the maximum duration of the input videos.
                                  Defaults to None.

    Returns:
        str: The path to the output video file, or None if an error occurred.
    """
    for video_path in videos:
        if not os.path.exists(video_path):
            print(f'Video {video_path} not found.')
            return None
        else:
            print(f'Video {video_path} found.')

    video_objects = [Video(video) for video in videos]
    fps = min([video.fps for video in video_objects])
    print(f"Minimum FPS of all videos: {fps:.2f}")

    if writer_fps is None:
        writer_fps = fps

    stitcher = VideoStitcher(video_objects, size, axis)
    
    if write_path:
        video_name, vid_duration = stitcher.stitch(write_path, writer_fps, duration)
        print(f"Video written successfully at: {video_name} || Duration: {vid_duration:.2f} seconds")
    else:
        video_name = None
        print("No write path specified. Video will not be saved.")

    for video in video_objects:
        video.release()

    return video_name


if __name__ == '__main__':
    # This is an example of how to use the stack_video function.
    # The paths to the videos are relative to the root of the repository.
    # You will need to provide your own video files to run this example.
    path1 = 'path/to/your/first/video.mp4'
    path2 = 'path/to/your/second/video.mp4'

    if os.path.exists(path1) and os.path.exists(path2):
        videos = [path1, path2]
        video_size = (300, 300)  # width, height
        video_path = 'test.mp4'
        video_duration = 4  # in seconds, None for full duration

        output_video = stack_video(
            videos=videos,
            axis=0,
            size=video_size,
            write_path=video_path,
            writer_fps=None,
            duration=video_duration
        )
        if output_video:
            print(f"Output video saved at: {output_video}")
    else:
        print("Please provide valid paths to your video files in the `if __name__ == '__main__':` block.")
