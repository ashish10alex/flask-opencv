#!/usr/bin/env python3
from importlib import import_module
import os
from flask import Flask, render_template, Response, request, redirect, url_for, flash
import io
from flask import Markup, make_response
from camera_opencv import Camera  # import camera driver
import os

app = Flask(__name__)


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def test_feed():
    return render_template('video.html')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True)
