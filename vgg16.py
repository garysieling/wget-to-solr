file = open("files.txt", "r")

import numpy as np

from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input, decode_predictions

import urllib.request, urllib.parse
import urllib3

http = urllib3.PoolManager()

import json

i = 0

model = VGG16(weights='imagenet', include_top=False)

for line in file:
    data = {}
    filepath = line.strip()

    remove = len("./") 
    idremove = len("./sacredwindowrescueproject.org/")
    data['id'] = filepath[idremove:]

    img = image.load_img(filepath, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    features = model.predict(x)
    # decode the results into a list of tuples (class, description, probability)
    # (one such list for each sample in the batch)
    predictions = decode_predictions(features, top=20)

    print(features)
    flattened = [val for sublist in predictions for val in sublist]
    print(flattened)

    tags = [tag for (id, tag, am) in flattened if am >= 0.25]
    print('Predicted:', tags)

    data['resnet50_tags'] = {}
    data['resnet50_tags']['set'] = tags
    encoded_data = ("[" + json.dumps(data) + "]").encode('utf-8')
    print(encoded_data)

    url = "http://40.87.64.225:8983/solr/glass/update?commit=true"

    r = http.request(
          'POST',
          url,
          body=encoded_data,
          headers={'Content-Type': 'application/json'})

    i = i + 1

