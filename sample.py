import time

from whisper import load_model, transcribe
from whisper.utils import get_writer


# set path
model_dir = "./model"
audio_path = "./audio/test.mp3"
output_dir = "./result"


# load model
print("Load model...")
start_load_model = time.time()
model = load_model("large-v3", device="cuda", download_root=model_dir)
end_load_model = time.time()
print(f"Model loaded in {end_load_model - start_load_model:.2f} seconds.\n")


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


# output result
print("Output result...")
start_output = time.time()
output_format = "all"  # "txt", "vtt", "srt", "tsv", "json", or "all"
writer = get_writer(output_format, output_dir)
writer(result, audio_path)
end_output = time.time()
print(f"Output generated in {end_output - start_output:.2f} seconds.\n")
