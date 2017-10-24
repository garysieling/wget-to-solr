file = open("files.txt", "r")
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


from PIL import Image
import numpy as np

import urllib.request, urllib.parse
import urllib3

http = urllib3.PoolManager()

import json

i = 0

client = vision.ImageAnnotatorClient()
for line in file:
    data = {}
    filepath = line.strip()

    remove = len("./") 
    idremove = len("./sacredwindowrescueproject.org/")
    data['id'] = filepath[idremove:]


    with io.open(filepath, 'rb') as image_file:
        content = image_file.read()

        image = types.Image(content=content)

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        print(response)
        labels = response.label_annotations

        data['gv_labels'] = {}
        data['gv_labels']['set'] = {}
        data['gv_labels']['set'] = [label.description for label in labels]

        response = client.text_detection(image=image)
        #print(response)
        gv_inscription = response.full_text_annotation.text

        data['gv_inscription'] = {}
        data['gv_inscription']['set'] = {}
        data['gv_inscription']['set'] = gv_inscription

        print(client)
        response = client.web_detection(image=image)
        notes = response.web_detection
        print(response)

        if notes.pages_with_matching_images:
            urls = [x.url for x in notes.pages_with_matching_images]

            data['gv_pages_matching_images'] = {}
            data['gv_pages_matching_images']['set'] = {}
            data['gv_pages_matching_images']['set'] = urls

        if notes.full_matching_images:
            urls = [x.url for x in notes.full_matching_images]
            data['gv_full_matching_images'] = {}
            data['gv_full_matching_images']['set'] = {}
            data['gv_full_matching_images']['set'] = urls

        if notes.partial_matching_images:
            urls = [x.url for x in notes.partial_matching_images]
            data['gv_partial_matching_images'] = {}
            data['gv_partial_matching_images']['set'] = {}
            data['gv_partial_matching_images']['set'] = urls

        if notes.web_entities:
            for entity in notes.web_entities:
                print('Score      : {}'.format(entity.score))
                print('Description: {}'.format(entity.description))

    encoded_data = ("[" + json.dumps(data) + "]").encode('utf-8')
    print(encoded_data)

    url = "http://40.87.64.225:8983/solr/glass/update?commit=true"

    r = http.request(
        'POST',
        url,
        body=encoded_data,
        headers={'Content-Type': 'application/json'})
