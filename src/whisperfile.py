def untertitel(file_path):
    import whisper
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    print(result["text"])