# CascadeTabNet with MMDetection - Docker Setup

This repository provides a Dockerized environment for running CascadeTabNet with MMDetection, including a FastAPI interface to process inference requests.

## Contents

- **CascadeTabNet/**: Contains configuration files and additional resources for CascadeTabNet (Python 3.7 + Pytorch 1.4 + cuda10.1 + cudnn7)
- **mmdetection/**: Contains the MMDetection framework and necessary dependencies (Python 3.6 + Pytorch 1.1 + cuda10.0 + cudnn7.5) 
- **docker-compose.yml**: Configuration file to build and manage Docker containers for the CascadeTabNet and MMDetection setup.



## Steps to Set Up and Run

### 1. Pull the MMDetection Docker Image

To start, pull the pytorch image for `CascadeTabNet` and base image for `mmdetection` from Docker Hub:

```bash
docker pull pytorch/pytorch:1.4-cuda10.1-cudnn7-devel
docker pull killonexx/mmdetection:latest
```

### 2. Clone the CascadeTabNet Repository (If needed)

```bash
!git clone https://github.com/DevashishPrasad/CascadeTabNet.git /CTN/CascadeTabNet
```

### 3. Building and Running with Docker Compose

To build and run the Docker Compose setup:

```bash
docker-compose build
docker-compose up
```

This command builds the containers based on the docker-compose.yml configuration and starts the services.


## Ports

- **CascadeTabNet**: 6006 
- **mmdetection**: 8000 