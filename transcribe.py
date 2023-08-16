import whisper

model = whisper.load_model("base", device="cpu")
result = model.transcribe("EarningsCall.wav")
print(result["text"])
