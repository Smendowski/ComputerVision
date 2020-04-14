import cv2
import os

class VideoConfig(object):
    VIDEO_DIMENSIONS =  {
        "360p": (480, 360),
        "480p": (640, 480),
        "720p": (1280, 720),
        "1080p": (1920, 1080),
        "4k": (3840, 2160),
    }

    ENCODING_TYPES = {
        'avi': cv2.VideoWriter_fourcc(*'XVID'),
        'mp4': cv2.VideoWriter_fourcc(*'XVID'),
    }

    # DEFAULT
    width           = 640
    height          = 480
    dims            = (640, 480)
    capture         = None
    video_type      = None

    def __init__(self, capture, filepath, res="480p", *args, **kwargs):
        self.capture = capture
        self.filepath = filepath
        self.width, self.height = self.get_dimensions(res=res)
        self.video_type = self.get_video_type()

    def custom_resolution(self, width, height):
        self.capture.set(3, width)
        self.capture.set(4, height)

    def get_dimensions(self, res='480p'):
        width, height = self.VIDEO_DIMENSIONS['480p']
        if res in self.VIDEO_DIMENSIONS:
            width, height = self.VIDEO_DIMENSIONS[res]
        self.custom_resolution(width, height)
        self.dims = (width, height)
        return width, height

    def get_video_type(self):
        filename, ext = os.path.splitext(self.filepath)
        if ext in self.ENCODING_TYPES:
          return  self.ENCODING_TYPES[ext]
        return self.ENCODING_TYPES['avi']


def image_resize(original_image, width = None, height = None, inter = cv2.INTER_AREA):
    dimensions = None
    (h, w) = original_image.shape[:2]
    if width is None and height is None:
        return original_image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(original_image, dim, interpolation = inter)
    return resized


