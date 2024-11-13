# Specify the base image, 'Ubuntu 18.04.3' 
FROM pytorch/pytorch:1.4-cuda10.1-cudnn7-devel

ARG DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV TZ=Asia/Shanghai

# ENV CUDA_HOME=/usr/local/cuda
# ENV LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
# ENV PATH=$CUDA_HOME/bin:$PATH

# ENV PATH="/usr/local/cuda/bin:${PATH}"
# ENV LD_LIBRARY_PATH="/usr/local/cuda/lib64:${LD_LIBRARY_PATH}"
# ENV CUDA_HOME="/usr/local/cuda"

ENV CUDA_HOME=/usr/local/cuda-10.1
ENV LD_LIBRARY_PATH=/usr/local/cuda-10.1/lib64:$LD_LIBRARY_PATH
ENV FORCE_CUDA="1"


# FROM pytorch/pytorch:1.1.0-cuda10.0-cudnn7.5-devel

# Set the Working Directory
WORKDIR /workspace/CascadeTabNet

# Install system dependencies; libgl1-mesa-glx is mainly for OpenCV's GUI dependencies in image processing
# RUN apt-get update && apt-get install -y \
#     libgl1-mesa-glx \
#     && rm -rf /var/lib/apt/lists/*

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC

# ARG DEBIAN_FRONTEND=noninteractive
# ENV LANG=C.UTF-8
# ENV LC_ALL=C.UTF-8
# ENV TZ=Asia/Shanghai
#ENV DEBIAN_FRONTEND=noninteractive

#RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
#RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC

RUN apt-get update && \
    apt-get install -y --no-install-recommends --fix-missing \  
    libgl1-mesa-glx \
    cmake \
    gcc \
    g++ \
    git \
    gfortran \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    && rm -rf /var/lib/apt/lists/*

# RUN apt-get update && apt-get install -y \
#     liblapack-dev libblas-dev libatlas-base-dev \
#     libjpeg-dev libpng-dev libtiff-dev libdc1394-22-dev \
#     libavcodec-dev libavformat-dev libswscale-dev \
#     libv4l-dev libxvidcore-dev libx264-dev \
#     libgtk-3-dev libcanberra-gtk3-module \
#     libatlas-base-dev gfortran

# RUN apt-get update && apt-get install -y python3.7 python3.7-dev python3.7-venv
# RUN ln -s /usr/bin/python3.7 /usr/bin/python

# Set OpenCV version
ARG OPENCV_VERSION="4.10.0"

# Update and install required packages, including comprehensive OpenCV dependencies
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends --fix-missing \
#         build-essential binutils cmake\
#         ca-certificates\
#         cmake-qt-gui \
#         curl

# RUN apt-get update && \
#     apt-get install -y --no-install-recommends --fix-missing \
#         #dbus-x11 \
#         #ffmpeg \
#         #gdb \
#         gcc g++ gfortran git \
#         tar \
#         libjpeg-dev \
#         libpng-dev \
#         libtiff-dev 

RUN apt-get update && \
    apt-get install -y --no-install-recommends --fix-missing \        
        lsb-release \
        procps \
        manpages-dev \
        unzip \
        zip \
        wget \
        xauth \
        swig 

# RUN apt-get update && \
#     apt-get install -y --no-install-recommends --fix-missing \
#         python3-pip python3-dev python3-numpy python3-distutils \
#         python3-setuptools python3-pyqt5 python3-opencv 

# RUN apt-get update && \
#     apt-get install -y --no-install-recommends --fix-missing \
#         libboost-python-dev libboost-thread-dev libatlas-base-dev libavcodec-dev \
#         libavformat-dev libavutil-dev libcanberra-gtk3-module libeigen3-dev \
#         libglew-dev libgl1-mesa-dev libgl1-mesa-glx libglib2.0-0 libgtk2.0-dev \
#         libgtk-3-dev libjpeg-dev libjpeg8-dev libjpeg-turbo8-dev liblapack-dev 

# RUN apt-get update && \
#     apt-get install -y --no-install-recommends --fix-missing \
#         liblapacke-dev libopenblas-dev libopencv-dev libpng-dev libpostproc-dev \
#         libpq-dev libsm6 libswscale-dev libtbb-dev libtbb2 libtesseract-dev \
#         libtiff-dev libtiff5-dev libv4l-dev libx11-dev libxext6 libxine2-dev 

# RUN apt-get update && \
#     apt-get install -y --no-install-recommends --fix-missing \       
#         libxrender-dev libxvidcore-dev libx264-dev libgtkglext1 libgtkglext1-dev 
#         #libvtk9-dev

# RUN apt-get update && \
#     apt-get install -y --no-install-recommends --fix-missing \
#         #libdc1394-dev\
#         libgstreamer-plugins-base1.0-dev 

# RUN apt-get update && \
#     apt-get install -y --no-install-recommends --fix-missing \
#         libgstreamer1.0-dev libopenexr-dev 

# RUN apt-get update && \
#     apt-get install -y --no-install-recommends --fix-missing \
#         openexr \
#         pkg-config \
#         qv4l2 \
#         v4l-utils \
#         zlib1g-dev \
#         locales \
#     && locale-gen en_US.UTF-8 \
#     && apt-get clean && rm -rf /var/lib/apt/lists/*

# Various Python and C/build deps
RUN apt-get update && \
    apt-get install -y --no-install-recommends --fix-missing \
    wget \
    build-essential \ 
    pkg-config 
    #python3-dev \ 
    #python3-opencv \ 

RUN apt-get update && \
    apt-get install -y --no-install-recommends --fix-missing \
    libopencv-dev \ 
    #libav-tools  \ 
    # libjpeg-dev \ 
    # libpng-dev \ 
    # libtiff-dev \ 
    #libjasper-dev \ 
    libgtk-3-dev 

RUN apt-get update && \
    apt-get install -y --no-install-recommends --fix-missing \
    #libgtk2.0-dev \ 
    python3-numpy \ 
    python3-pycurl \ 
    libatlas-base-dev \
    #gfortran \
    webp \ 
    python3-opencv 

# Install Open CV - Warning, this takes absolutely forever
# RUN cd ~ && git clone https://github.com/Itseez/opencv.git && \ 
#     cd opencv && \
#     git checkout && \
#     cd ~ && git clone https://github.com/Itseez/opencv_contrib.git && \
#     cd opencv_contrib && \
#     git checkout && \
#     cd ~/opencv && mkdir -p build && cd build && \
#     cmake -D CMAKE_BUILD_TYPE=RELEASE \
#     -D CMAKE_INSTALL_PREFIX=/usr/local \ 
#     -D INSTALL_C_EXAMPLES=ON \ 
#     -D INSTALL_PYTHON_EXAMPLES=ON \ 
#     -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \ 
#     -D BUILD_EXAMPLES=OFF .. && \
#     make -j4 && \
#     make install && \ 
#     ldconfig


# Copy the CascadeTabNet model folder into the Docker container, ensuring all files are in the specified path
COPY CascadeTabNet/ /workspace/CascadeTabNet/CascadeTabNet/

#RUN pip install torch==1.4.0+cu101 torchvision==0.4.1+cu101 -f https://download.pytorch.org/whl/torch_stable.html

# RUN pip install https://download.pytorch.org/whl/cu101/torch-1.4.0-cp37-cp37m-linux_x86_64.whl \
#     https://download.pytorch.org/whl/cu101/torchvision-0.4.0-cp37-cp37m-linux_x86_64.whl

RUN pip install gdown

WORKDIR /workspace/CascadeTabNet

#COPY torch-1.4.0-cp37-cp37m-linux_x86_64.whl .
#COPY torchvision-0.4.0-cp37-cp37m-manylinux1_x86_64.whl .
#COPY torchvision-0.5.0+cu100-cp37-cp37m-linux_x86_64.whl .

RUN gdown --id 16JPIuzo3lJNY6bVmSdqyf2ppBnaxvehS -O /workspace/CascadeTabNet/torch-1.4.0-cp37-cp37m-linux_x86_64.whl
RUN gdown --id 1rlxAMdW3-ZImTdnEsO_V__JYJXzZJXeW -O /workspace/CascadeTabNet/torchvision-0.5.0+cu100-cp37-cp37m-linux_x86_64.whl


RUN pip install torch-1.4.0-cp37-cp37m-linux_x86_64.whl torchvision-0.5.0+cu100-cp37-cp37m-linux_x86_64.whl
# Copy requirements.txt into the Docker container; requirements.txt lists the Python dependencies
COPY requirements.txt .

# Install Python dependencies, including FastAPI, mmdetection, mmcv, and others
RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install -r requirements.txt > install.log 2>&1

# # Clone the mmdetection repository and install its dependencies
# RUN git clone --branch v1.2.0 https://github.com/open-mmlab/mmdetection.git /mmdetection

# # Set working directory to mmdetection
# WORKDIR /mmdetection

# # Install mmdetection dependencies and setup
# RUN export CUDA_HOME=/usr/local/cuda && \
#     export LD_LIBRARY_PATH=${CUDA_HOME}/lib64:${LD_LIBRARY_PATH} && \
#     pip install -r requirements/optional.txt \
#     && python setup.py install \
#     && python setup.py develop \
#     && pip install -r requirements.txt 
#     #&& pip install pillow==6.2.1

# Return to working directory for CascadeTabNet
WORKDIR /workspace/CascadeTabNet

# Copy the FastAPI service code into the Docker container
#RUN wget -O /workspace/CascadeTabNet/epoch_36.pth "https://drive.google.com/uc?export=download&id=1-QjeHkR1Q7CXuBu4fp3rYrvDG9j26eFT"
#RUN gdown https://drive.google.com/uc?id=1-QjeHkR1Q7CXuBu4fp3rYrvDG9j26eFT -O /workspace/CascadeTabNet/epoch_36.pth

RUN pip install gdown
#RUN gdown https://drive.google.com/uc?id=1-QjeHkR1Q7CXuBu4fp3rYrvDG9j26eFT -O /workspace/CascadeTabNet/epoch_36.pth
#RUN gdown https://drive.google.com/file/d/1yyNAuNVJ0TNzAY6HnuLLDimBUMdJfgU2/view?usp=sharing -O /workspace/CascadeTabNet/epoch_36.pth
RUN gdown --id 1yyNAuNVJ0TNzAY6HnuLLDimBUMdJfgU2 -O /workspace/CascadeTabNet/epoch_36.pth


# Copy pretrained model (if needed)
#COPY epoch_36.pth .

# Copy the FastAPI service code into the Docker container
COPY api.py .

EXPOSE 6006

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "6006"]