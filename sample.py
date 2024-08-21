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
    verbose=True,
    temperature=0.0,
    condition_on_previous_text=True,
    word_timestamps=True,
)
print()

# print("Transcription Text:", result["text"])
# print("Language Detected:", result["language"])
# print("Segments:", result["segments"])


# output result
print("Output result...")
output_format = "all"  # "txt", "vtt", "srt", "tsv", "json", or "all"
writer = get_writer(output_format, output_dir)
writer(result, audio_path)
print()
