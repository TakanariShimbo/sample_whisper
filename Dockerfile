FROM nvidia/cuda:12.1.1-base-ubuntu22.04

# apt get
RUN apt-get update && apt-get install --no-install-recommends -y \
    git vim build-essential python3-dev python3-venv python3-pip ffmpeg

# pip install torch
RUN pip3 install --upgrade pip setuptools && \
    pip3 install torch torchvision torchaudio

# pip install whisper
RUN pip3 install -U openai-whisper
