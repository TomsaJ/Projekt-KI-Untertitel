def untertitel(file_path):

    import whisper
    import datetime
    import os

    model = whisper.load_model("base")
    options = whisper.DecodingOptions(language='de', fp16 = False)
    result = model.transcribe(file_path)

    save_target = os.path.join(os.getcwd(), 'tmp', 'subtitel.vtt')

    with open(save_target, 'w') as file:
        file.write(str('WEBVTT'))
        file.write(str('\n' + '\n'))
        for indx, segment in enumerate(result['segments'], start=1):
            start_time = datetime.timedelta(seconds=segment['start'])
            end_time = datetime.timedelta(seconds=segment['end'])
        
            file.write(str(indx) + '\n')
            file.write(str(start_time) + ' --> ' + str(end_time) + '\n')
            file.write(segment['text'].strip() + '\n\n')
        
    print("VTT file created successfully.")
