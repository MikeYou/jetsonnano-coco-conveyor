#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, Response
import cv2
import os
import time
app = Flask(__name__)



def new_report(test_report):
    lists=os.listdir(test_report)
    lists.sort(key=lambda fn:os.path.getmtime(test_report+"//"+fn))
    return lists[-1]
#a = new_report("./static/")
#print("./static/"+ str(a))


def gen_frames():
    while True:
        a = new_report("./static/")
        #print(a)        
        frame = cv2.imread("./static/"+ str(a))  
        
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        time.sleep(0.5)
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False, threaded=True)
