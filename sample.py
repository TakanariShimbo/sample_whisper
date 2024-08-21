from whisper import load_model, transcribe
from whisper.utils import get_writer


# set path
model_dir = "./model"
audio_path = "./audio/test.mp3"
output_dir = "./result"


# load model
print("Load model...")
model = load_model("large-v3", device="cuda", download_root=model_dir)
print()


# run transcribe
print("Transcribe...")
result = transcribe(
    model,
    audio_path,
    language="Japanese",
    verbose=False,
    temperature=0.0,
    condition_on_previous_text=True,
    word_timestamps=True,
)
print()

result_text = ""
for segment in result["segments"]:
    segment_start = segment["start"]
    segment_end = segment["end"]
    segment_text = segment["text"]

    # Format as [hh:mm:ss.sss --> hh:mm:ss.sss] Text
    result_text += f"[{segment_start:0>7.3f} --> {segment_end:0>7.3f}] {segment_text}\n"

if len(result_text) > 0:
    result_text = result_text[:-1]

print(result_text)
print()

# output result
print("Output result...")
output_format = "all"  # "txt", "vtt", "srt", "tsv", "json", or "all"
writer = get_writer(output_format, output_dir)
writer(result, audio_path)
print()
