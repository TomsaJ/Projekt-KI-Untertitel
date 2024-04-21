def untertitel(file_path):

    import whisper

    model = whisper.load_model("base")
    options = whisper.DecodingOptions(language='de', fp16 = False)
    result = model.transcribe(file_path)
    
    print(result["text"])
    '''
    import whisper
    model = whisper.load_model("base")
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(file_path)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)

    # print the recognized text
    print(result.text)
    import subprocess
    model = "medium"
    language = "German"
    try:
        # Baue den Befehl zusammen
        command = f"whisper {file_path} --model {model} --language {language} --output_dir tmp"
        # Führe den Befehl aus und erhalte die Ausgabe
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        # Gib die Ausgabe zurück
        return result.stdout
    except subprocess.CalledProcessError as e:
        # Handle den Fehler, wenn der Befehl fehlschlägt
        print(f"Fehler beim Ausführen des Befehls: {e}")
        return None
    '''