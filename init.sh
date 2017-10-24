apt-get update && apt-get upgrade
apt-get -y install libboost-all-dev python3-pip build-essential gcc cmake git python-imaging libjpeg62 libjpeg62-dev python-scipy

git clone https://github.com/davisking/dlib
cd dlib
cmake .. -DDLIB_USE_CUDA=0 -DUSE_AVX_INSTRUCTIONS=1
python3 setup.py install --yes USE_AVX_INSTRUCTIONS --no DLIB_USE_CUDA

pip3 install face_recognition matplotlib sklearn numpy

apt-get install python3-tk
pip3 install keras tensorflow h5py

apt-get install tesseract-ocr-all
pip3 install opencv-python

pip3 install -U scikit-image 
pip3 install --upgrade imutils

sudo apt-get install build-essential cmake pkg-config
sudo apt-get install libjpeg8-dev libtiff5-dev 
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev

sudo apt-get install libatlas-base-dev gfortran
sudo apt-get install python2.7-dev python3.6-dev

apt install unzip
cd ~
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip
unzip opencv.zip

wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.1.0.zip
unzip opencv_contrib.zip

wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py

sudo pip install virtualenv virtualenvwrapper
sudo rm -rf ~/get-pip.py ~/.cache/pip

export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh

echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.bashrc
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
source ~/.bashrc
mkvirtualenv cv -p python3

pip3 install numpy

workon cv
cd ~/opencv-3.1.0/
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
	    -D CMAKE_INSTALL_PREFIX=/usr/local \
	        -D INSTALL_PYTHON_EXAMPLES=ON \
		    -D ENABLE_PRECOMPILED_HEADERS=OFF -D INSTALL_C_EXAMPLES=OFF \
		        -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.1.0/modules \
			    -D PYTHON_EXECUTABLE=~/.virtualenvs/cv/bin/python \
			        -D BUILD_EXAMPLES=ON ..

make

sudo make install
sudo ldconfig

cd /usr/local/lib/python3.6/site-packages/
mv cv2.cpython-36m-x86_64-linux-gnu.so cv2.so

cd ~/.virtualenvs/cv/lib/python3.5/site-packages/
ln -s /usr/local/lib/python3.5/site-packages/cv2.so cv2.so

apt-install tesseract

sudo add-apt-repository ppa:alex-p/tesseract-ocr
sudo apt-get update
apt-get install tesseract-ocr

wget https://github.com/tesseract-ocr/tessdata/raw/master/eng.traineddata
mkdir -p /usr/local/share/tessdata/
mv eng.traineddata /usr/share/tesseract-ocr/4.00/

pip3 install --upgrade google-cloud-vision
