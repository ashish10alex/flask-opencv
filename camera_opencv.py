import cv2
from base_camera import BaseCamera
import time
import argparse 

ap = argparse.ArgumentParser()
ap.add_argument('--video', help='path to video')
args = vars(ap.parse_args())
video_source = args['video']

if video_source == 'web-cam':
    video_source = 0

class Camera(BaseCamera):

    video_source = video_source

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()

            #if we reach the end of video file
            if (img is None):
                break

            time.sleep(0.03)

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
