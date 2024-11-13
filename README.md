This repository provides a Dockerized environment for running CascadeTabNet with MMDetection, including a FastAPI interface to process inference requests.

Contents
-CascadeTabNet/: Contains configuration files and additional resources for CascadeTabNet.
-mmdetection/: Contains the MMDetection framework and necessary dependencies.
-docker-compose.yml: Configuration file to build and manage Docker containers for the CascadeTabNet and MMDetection setup.

Prerequisites
Docker and Docker Compose installed on your system.
Access to a pretrained model file and configuration files required for CascadeTabNet.

Steps to Set Up and Run

1. Pull the MMDetection Docker Image
To start, pull the base image for mmdetection from Docker Hub:
docker pull killonexx/mmdetection:latest

This image contains MMDetection with the necessary dependencies for running object detection models.
