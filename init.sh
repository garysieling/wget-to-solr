apt-get update && apt-get upgrade
apt-get -y install libboost-all-dev setuptools python3-pip build-essential gcc cmake git

apt-get install build-dep python-imaging
apt-get install libjpeg62 libjpeg62-dev

apt-get install python-scipy

git clone https://github.com/davisking/dlib
cd dlib
cmake .. -DDLIB_USE_CUDA=0 -DUSE_AVX_INSTRUCTIONS=1
python3 setup.py install --yes USE_AVX_INSTRUCTIONS --no DLIB_USE_CUDA

python setup.py install
pip3 install face_recognition
