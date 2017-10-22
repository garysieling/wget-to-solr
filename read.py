file = open("files.txt", "r")

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin
from sklearn.datasets import load_sample_image
from sklearn.utils import shuffle
from time import time

import urllib.request, urllib.parse
import urllib3

http = urllib3.PoolManager()

import scipy.ndimage
import face_recognition
import json

i = 0

for line in file:
    data = {}
    filepath = line.strip()

    remove = len("./") 
    idremove = len("./sacredwindowrescueproject.org/")
    data['file'] = filepath
    data['id'] = filepath[idremove:]
    data['url'] = 'http://www.' + filepath[remove:]
    data['place'] = filepath.split('/')[2]
   
    shape = scipy.ndimage.imread(filepath).shape

    if (len(shape) == 2):
        height, width = shape
        data['height'] = height
        data['width'] = width
    if (len(shape) == 3):
        height, width, channels = shape
        data['height'] = height
        data['width'] = width
        data['channels'] = channels

    data['aspect'] = int(100 * height / width)
    
    image = face_recognition.load_image_file(filepath)
    face_locations = face_recognition.face_locations(image)
    data['faces'] = json.dumps(face_locations)
    data['face_count'] = len(face_locations)

    json_data = json.dumps(data)

    encoded_data = json.dumps(data).encode('utf-8')

    print(json_data)

    url = "http://40.87.64.225:8983/solr/glass/update/json/docs?commit=true"

    r = http.request(
          'POST',
          url,
          body=encoded_data,
          headers={'Content-Type': 'application/json'})

    i = i + 1

