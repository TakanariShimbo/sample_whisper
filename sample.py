import io
import time
import os
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

from whisper import load_model, transcribe


# set path
model_dir = "./model"
audio_dir = "./audio"
output_dir = "./transcription"


# find audio file
audio_files = [
    f for f in os.listdir(audio_dir)
    if os.path.isfile(os.path.join(audio_dir, f)) and f.startswith("input.")
]
if not audio_files:
    raise FileNotFoundError("Audio file not found.")
audio_path = os.path.join(audio_dir, audio_files[0])


# load model
print("Load model...")
start_load_model = time.time()
model = load_model("large-v3", device="cuda", download_root=model_dir)
end_load_model = time.time()
print(f"Model loaded in {end_load_model - start_load_model:.2f} seconds.\n")


# load audio
print("Load audio...")
start_load_audio = time.time()
with open(audio_path, 'rb') as audio_file:
    audio_buffer = io.BytesIO(audio_file.read())
end_load_audio = time.time()
print(f"Audio loaded in {end_load_audio - start_load_audio:.2f} seconds.\n")


# run transcribe
print("Transcribe...")
start_transcribe = time.time()
result = transcribe(
    model,
    audio_path,
    language="Japanese",
    verbose=False,
    temperature=0.0,
    condition_on_previous_text=False,
    word_timestamps=True,
)

result_text = ""
for segment in result["segments"]:
    segment_start = segment["start"]
    segment_end = segment["end"]
    segment_text = segment["text"]

    # Format as [hh:mm:ss.sss --> hh:mm:ss.sss] Text
    result_text += f"[{segment_start:0>8.3f} --> {segment_end:0>8.3f}] {segment_text}\n"

if len(result_text) > 0:
    result_text = result_text[:-1]

print(f"{result_text}\n")

end_transcribe = time.time()
print(f"Transcription completed in {end_transcribe - start_transcribe:.2f} seconds.\n")


# output transcription
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("Output transcription...")
start_output = time.time()

with open(f"{output_dir}/output.txt", "w", encoding="utf-8") as f:
    f.write(result_text)
end_output = time.time()
print(f"Output generated in {end_output - start_output:.2f} seconds.\n")
