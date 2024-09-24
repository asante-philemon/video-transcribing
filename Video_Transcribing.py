import whisper


model = whisper.load_model('base')
result = model.transcribe('/Introduction.mp4')

with open("transcription.txt", "w") as f:
        f.write(result["text"])