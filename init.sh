apt-get update && apt-get upgrade
apt-get -y install libboost-all-dev python3-pip build-essential gcc cmake git python-imaging libjpeg62 libjpeg62-dev python-scipy

git clone https://github.com/davisking/dlib
cd dlib
cmake .. -DDLIB_USE_CUDA=0 -DUSE_AVX_INSTRUCTIONS=1
python3 setup.py install --yes USE_AVX_INSTRUCTIONS --no DLIB_USE_CUDA

pip3 install face_recognition matplotlib sklearn numpy

apt-get install python3-tk
pip3 install keras tensorflow h5py
