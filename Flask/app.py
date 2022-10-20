# libraries
import cv2
from utils import *
import numpy as np
from rembg import remove
import os

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

detector = Measuring_Volume()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def select():
    return render_template('select.html')

@app.route('/RECTANGLE',methods=['GET'])
def RECTANGLE():
    return render_template('upload.html')

@app.route('/file_upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        img_dir = '/Users/krc/Downloads/Fit_in_Volume/Flask/uploads/'
        files = request.files.getlist("files")
        for f in files:
            f.save(os.path.join(img_dir, secure_filename(f.filename)))
        return render_template('rectangle.html')

@app.route('/calculate1', methods=['GET', 'POST'])
def calculate1(): 
    if request.method == 'POST':
        img_dir = '/Users/krc/Downloads/Fit_in_Volume/Flask/uploads/'
    
        files = os.listdir(img_dir)
        if os.path.exists(img_dir+'.DS_Store'):
            os.remove(img_dir+'.DS_Store')
            
        for i in range(len(files)):
            if (img_dir+files[i]).__contains__(".jpg" or '.jpeg' or ".png"):
                globals()[f'img{i+1}_width'], globals()[f'img{i+1}_height'] = get_sizes(img_dir + files[i], files[i])

        result1 = compare_width(img1_width, img1_height, img2_width, img2_height)
        if os.path.exists(img_dir):
            for f in os.scandir(img_dir):
                os.remove(f.path)
        return result1
    return "Error"

@app.route('/CYLINDER',methods=['GET'])
def CYLINDER():
    return render_template('cylinder.html')

@app.route('/calculate2', methods=['GET', 'POST'])
def calculate2():
    if request.method == 'POST':
        img_dir = '/Users/krc/Downloads/Fit_in_Volume/Flask/uploads/'
        
        f = request.files['file']
        file_path = os.path.join(img_dir, secure_filename(f.filename))
        f.save(file_path)

        files = os.listdir(img_dir)
        if os.path.exists(img_dir+'.DS_Store'):
            os.remove(img_dir+'.DS_Store')

        for i in range(len(files)):
            if (img_dir+files[i]).__contains__(".jpg" or '.jpeg' or ".png"):
                globals()[f'img{i+1}_width'], globals()[f'img{i+1}_height'] = get_sizes(img_dir + files[i], files[i])

        result2 = get_circumference(img1_width, img1_height)
        if os.path.exists(img_dir):
            for f in os.scandir(img_dir):
                os.remove(f.path)
        return result2
    return "Error"
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)