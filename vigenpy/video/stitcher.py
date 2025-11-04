__author__ = "Vinay Verma"
__copyright__ = "Copyright 2021, Vinay Verma"
__credits__ = ["Vinay Verma"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Vinay Verma"
__email__ = "vermavinay982@gmail.com"
__module_name__ = "[Video Stitcher]"


import cv2
import numpy as np
from tqdm import tqdm
from .video import Video
from nptyping import NDArray


class VideoStitcher:
    """A class to stitch multiple videos together.

    Attributes:
        videos (list[Video]): A list of video objects to be stitched.
        size (tuple[int, int]): The desired output size (width, height) of each video frame.
        axis (int): The axis along which the videos will be stacked (0 for horizontal, 1 for vertical, 2 for time-based).
    """

    def __init__(self, videos: list[Video], size: tuple[int, int] = (300, 400), axis: int = 0):
        """Constructs all the necessary attributes for the VideoStitcher object.

        Args:
            videos (list[Video]): A list of video objects to be stitched.
            size (tuple[int, int], optional): The desired output size (width, height) for each video frame. Defaults to (300, 400).
            axis (int, optional): The axis for stacking videos. 0 for horizontal, 1 for vertical, 2 for time-based. Defaults to 0.
        """
        self.videos = videos
        self.size = size
        self.axis = axis

    def _get_frame(self, video: Video) -> NDArray:
        """Reads and resizes a single frame from a video.

        If the video has ended, it will loop back to the beginning.

        Args:
            video (Video): The video object from which to read the frame.

        Returns:
            NDArray: The resized video frame.
        """
        ret, frame = video.read()
        if not ret:
            video.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = video.read()
        return cv2.resize(frame, self.size)

    def stitch(self, write_path: str, writer_fps: float, duration: int = None) -> tuple[str, float]:
        """Stitches the videos together and saves the output to a file.

        Args:
            write_path (str): The path to save the output video file.
            writer_fps (float): The frames per second for the output video.
            duration (int, optional): The desired duration of the output video in seconds.
                                     If None, it will be the maximum duration of the input videos. Defaults to None.

        Returns:
            tuple[str, float]: A tuple containing the path to the output video and its total duration in seconds.
        """
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        height, width = self._get_output_shape()
        out = cv2.VideoWriter(write_path, fourcc, int(writer_fps), (width, height))
        frame_counter = 0

        total_frames = self._get_total_frames(duration, writer_fps)

        for _ in tqdm(range(total_frames)):
            frames = [self._get_frame(video) for video in self.videos]
            if self.axis == 0:
                resized_frame = np.hstack(frames)
            elif self.axis == 1:
                resized_frame = np.vstack(frames)
            else:
                resized_frame = frames[frame_counter % len(frames)]

            out.write(resized_frame)
            frame_counter += 1

        out.release()
        total_duration = frame_counter / writer_fps
        return write_path, total_duration

    def _get_output_shape(self) -> tuple[int, int]:
        """Calculates the output shape (height, width) of the stitched video.

        Returns:
            tuple[int, int]: The height and width of the output video.
        """
        if self.axis == 0:
            height = self.size[1]
            width = self.size[0] * len(self.videos)
        elif self.axis == 1:
            height = self.size[1] * len(self.videos)
            width = self.size[0]
        else:
            height = self.size[1]
            width = self.size[0]
        return height, width

    def _get_total_frames(self, duration: int, writer_fps: float) -> int:
        """Calculates the total number of frames to be written to the output video.

        Args:
            duration (int): The desired duration of the output video in seconds.
            writer_fps (float): The frames per second for the output video.

        Returns:
            int: The total number of frames to be written.
        """
        if duration is not None:
            return int(writer_fps * duration)

        return max([video.frame_count for video in self.videos])
