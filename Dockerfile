FROM nvidia/cuda:12.1.1-base-ubuntu22.04

# apt get
RUN apt-get update && apt-get install --no-install-recommends -y \
    git vim build-essential python3-dev python3-venv python3-pip ffmpeg

# pip install
RUN pip3 install --upgrade pip setuptools
RUN pip3 install -U openai-whisper
