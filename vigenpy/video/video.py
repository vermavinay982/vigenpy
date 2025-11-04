__author__ = "Vinay Verma"
__copyright__ = "Copyright 2021, Vinay Verma"
__credits__ = ["Vinay Verma"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Vinay Verma"
__email__ = "vermavinay982@gmail.com"
__module_name__ = "[Video]"


import cv2
from nptyping import NDArray


class Video:
    """A class to represent a video file.

    Attributes:
        video_path (str): The path to the video file.
        cap (cv2.VideoCapture): The OpenCV video capture object.
        width (int): The width of the video frames.
        height (int): The height of the video frames.
        fps (float): The frames per second of the video.
        frame_count (int): The total number of frames in the video.
    """

    def __init__(self, video_path: str):
        """Constructs all the necessary attributes for the video object.

        Args:
            video_path (str): The path to the video file.
        """
        self.video_path = video_path
        self.cap = cv2.VideoCapture(self.video_path)
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

    def is_opened(self) -> bool:
        """Check if the video capture object is opened.

        Returns:
            bool: True if the video capture object is opened, False otherwise.
        """
        return self.cap.isOpened()

    def read(self) -> tuple[bool, NDArray]:
        """Read a frame from the video.

        Returns:
            tuple[bool, NDArray]: A tuple containing a boolean value indicating
            whether the frame was read successfully, and the frame itself.
        """
        return self.cap.read()

    def release(self) -> None:
        """Release the video capture object."""
        self.cap.release()
