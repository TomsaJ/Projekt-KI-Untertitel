def untertitel(file_path):

    import whisper
    import datetime

    model = whisper.load_model("base")
    options = whisper.DecodingOptions(language='de', fp16 = False)
    result = model.transcribe(file_path)

    save_target = 'tmp/subtitle.srt'

    with open(save_target, 'w') as file:
        for indx, segment in enumerate(result['segments'], start=1):
            start_time = datetime.timedelta(seconds=segment['start'])
            end_time = datetime.timedelta(seconds=segment['end'])
        
            file.write(str(indx) + '\n')
            file.write(str(start_time) + ' --> ' + str(end_time) + '\n')
            file.write(segment['text'].strip() + '\n\n')
        
    print("SRT file created successfully.")
