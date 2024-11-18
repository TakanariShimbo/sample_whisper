## About

Run Whisper(https://github.com/openai/whisper) on Docker

## Usage

### download mp3

You can download sample audio from here (https://pro-video.jp/voice/announce/)  
After that, please rename input.mp3 and copy to audio dir

### run commands

```sh
# build image
docker build . -t whisper-image

# wakeup server
docker compose up -d

# into terminal of whisper-container
docker exec -it whisper-container python3 sample.py
```

### result console

used audio: https://pro-video.jp/voice/announce/mp3/g_08.mp3 (total length: 43s)  
used gpu: RTX2060

```bash
$ docker exec -it whisper-container python3 sample.py
Load model...
Model loaded in 27.78 seconds.

Transcribe...
100%|███████████████████████████████████████████████████████████| 4318/4318 [00:08<00:00, 535.88frames/s]
[0002.780 --> 0007.160] それでは当社の概要と業務についてご紹介いたします
[0009.020 --> 0015.620] 今世界的規模で地球環境の保護CO2削減などが叫ばれていますが
[0015.620 --> 0019.200] いずれもまだまだ進んでいないのが現状です
[0020.600 --> 0027.160] 当社ではFA機器の開発製造を自社独自の合理化技術により
[0027.160 --> 0032.240] 省力化、見える化するファインプログラムシステムを開発
[0032.780 --> 0036.540] 見える化することにより材料の無駄をなくし
[0036.540 --> 0039.540] 環境保全に優れた効果を発揮します

Transcription completed in 8.25 seconds.

Output transcription...
Output generated in 0.00 seconds.
```

### result tree

```txt
├── Dockerfile
├── README.md
├── audio
│   └── input.mp3
├── docker-compose.yaml
├── model
│   └── large-v3.pt
├── transcription
│   ├── output.txt
└── sample.py
```
