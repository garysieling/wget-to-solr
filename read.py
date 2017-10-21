file = open("files.txt", "r")

import scipy.ndimage
import face_recognition

for line in file:
      filepath = line.strip()
      print(filepath)
      height, width, channels = scipy.ndimage.imread(filepath).shape
      print(height)
      print(width)
      print(channels)
      print(1.0 * height / width)

