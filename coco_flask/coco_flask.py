#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)
img =cv2.VideoCapture(0, cv2.CAP_V4L2)
#window_title = "CSI Camera"
#if img.isOpened():
#    try:
#        window_handle = cv2.namedWindow(window_title, cv2.WINDOW_AUTOSIZE)
#        while True:
#            ret_val, frame = img.read()
#            if cv2.getWindowProperty(window_title, cv2.WND_PROP_AUTOSIZE) >= 0:
#                cv2.imshow(window_title, frame)
#            else:
#                break 
#            keyCode = cv2.waitKey(10) & 0xFF
#            # Stop the program on the ESC key or 'q'
#            if keyCode == 27 or keyCode == ord('q'):
#                break
#    finally:
#        img.release()
#        cv2.destroyAllWindows()
#else:
#    print("Error: Unable to open camera")

def gen_frames():
    while True:
        success, frame = img.read()  
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False, threaded=True)
