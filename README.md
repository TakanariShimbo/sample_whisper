## About

Run Whisper on Docker

## Usage

### download mp3

download from here  
https://pro-video.jp/voice/announce/

copy mp3 to audio dir

### run commands

```sh
# build image
docker build . -t whisper-image

# wakeup server
docker compose up -d

# into terminal of whisper-container
docker exec -it whisper-container /bin/bash

# run test
whisper ./audio/test.mp3 --language Japanese --model large-v3 --model_dir ./model --output_dir ./result --device cuda
```

### result tree

```txt
├── Dockerfile
├── README.md
├── audio
│   └── test.mp3
├── docker-compose.yaml
├── model
│   └── large-v3.pt
└── result
    ├── test.json
    ├── test.srt
    ├── test.tsv
    ├── test.txt
    └── test.vtt
```
