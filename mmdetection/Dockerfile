FROM killonexx/mmdetection:latest

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    TZ=Asia/Shanghai

ENV CUDA_HOME=/usr/local/cuda-10.0
ENV LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64:$LD_LIBRARY_PATH
ENV FORCE_CUDA="1"

#ENV PYTHON_EXECUTABLE=/opt/conda/bin/python3
#ENV PYTHON_EXECUTABLE=/opt/conda/bin/python2


# FROM pytorch/pytorch:1.1.0-cuda10.0-cudnn7.5-devel

# Set the Working Directory
WORKDIR /workspace/mmdetection

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC

# Copy the FastAPI inference server script to the container (e.g., api.py)
COPY api.py /mmdetection/api.py

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn asyncio "mmcv==0.3.1"
#RUN pip install fastapi==0.103.2
#RUN pip install uvicorn==0.22.0
#RUN pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu101/torch1.4/index.html
#RUN pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu101/torch1.3/index.html
#RUN pip install mmcv-full==0.3.1 -f https://download.openmmlab.com/mmcv/dist/cu100/torch1.1/index.html
#RUN pip install mmcv==0.3.1

#RUN pip install fastapi uvicorn "mmcv==0.3.1"



# Expose the FastAPI server port (adjust the port number if needed)
EXPOSE 8000

# Run the FastAPI server when the container starts
#CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
#CMD ["python", "-c", "import asyncio; asyncio.run(uvicorn.run(app='api:app', host='0.0.0.0', port=8000))"]

