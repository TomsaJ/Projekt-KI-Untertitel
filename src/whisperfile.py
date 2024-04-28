def untertitel(file_path):

    import whisper
    import datetime
    import os

    model = whisper.load_model("base")
    options = whisper.DecodingOptions(language='de', fp16 = False)
    result = model.transcribe(file_path)

    save_target = os.path.join(os.getcwd(), 'tmp', 'subtitel.srt')

    with open(save_target, 'w') as file:
        for indx, segment in enumerate(result['segments'], start=1):
            start_time = datetime.timedelta(seconds=segment['start'])
            end_time = datetime.timedelta(seconds=segment['end'])

            # Konvertiere Zeitstempel in einen String im gewünschten Format mit Komma für Dezimalstellen
            start_time_str = '0' + str(start_time).replace('.', ',')
            end_time_str = '0' + str(end_time).replace('.', ',')
            if indx == 1:
                start_time_str += ',000'
            file.write(str(indx) + '\n')
            file.write(start_time_str + ' --> ' + end_time_str + '\n')
            file.write(segment['text'].strip() + '\n\n')

    print("VTT-Datei erfolgreich erstellt.")
