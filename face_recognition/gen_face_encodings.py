import face_recognition
import cv2
import camera
import os
import numpy as np
import pandas as pd

dirname_raw = 'raw_data'
dirname_res = 'knowns'
files_raw = os.listdir(dirname_raw)
files_res = os.listdir(dirname_res)
for filename in files:
    name, ext = os.path.splitext(filename)
    if ext == '.mp4':
        pathname = os.path.join(dirname_raw, filename)
        mov = face_recognition.load_image_file(pathname)
        