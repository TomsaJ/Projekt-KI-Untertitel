def untertitel(file_path):

    import whisper
    import datetime

    model = whisper.load_model("base")
    options = whisper.DecodingOptions(language='de', fp16 = False)
    result = model.transcribe(file_path)

    save_target = 'tmp/test.vtt'
    with open (save_target,'w') as file:
        file.write(str('WEBVTT'))
        file.write(str('\n'))
        for indx, segment in enumerate(result[ 'segments']):
            file.write(str('\n'))
            file.write(str(datetime.timedelta(seconds=segment['start'])) + ' --> ' + str(datetime.timedelta(seconds=segment[ 'end'])) +'\n')
            file.write(segment['text'].strip() + '\n')
        print(result["text"])