# Projekt-KI-Untertitel


## Ausführung
starte die main.py im Terminal mit python main.py
der momentane daten pfad ist video/DieTulpe.mp4

https://www.youtube.com/watch?v=UWOPQlxk-LM


    def combine_video_with_subtitle(video_file, subtitle_file, output_file):
        tmp = TempFileManager
        converted_subtitle_file = subtitle_file.replace('.vtt', '.srt')  # Ersetze die Dateiendung durch .srt
        converted_subtitle_file = tmp.convert_subtitle(subtitle_file, converted_subtitle_file)
    
        if converted_subtitle_file:
            try:
                (
                    ffmpeg
                    .input(video_file)
                    .input(converted_subtitle_file, vf='subtitles=' + converted_subtitle_file)  # Füge die konvertierte Untertiteldatei hinzu
                    .output(output_file, vcodec='copy', acodec='copy')
                    .run(overwrite_output=True)
                )
                print("Die Video-Datei wurde erfolgreich mit den Untertiteln kombiniert und gespeichert.")
            except ffmpeg.Error as e:
                print(f"Fehler beim Kombinieren von Video und Untertiteln: {e.stderr}")
        else:
            print("Die Untertiteldatei konnte nicht konvertiert werden. Das Video wurde nicht kombiniert.")


            import os
import ffmpeg

def combine_video_with_subtitle(video_file, subtitle_file, output_file):
    try:
        (
            ffmpeg
            .input(video_file)
            .output(output_file, vf=f'subtitles={subtitle_file}')
            .run(overwrite_output=True)
        )
        print("Die Video-Datei wurde erfolgreich mit den Untertiteln kombiniert und gespeichert.")
    except ffmpeg.Error as e:
        print(f"Fehler beim Kombinieren von Video und Untertiteln: {e.stderr}")

# Beispielaufruf
video_file = '/pfad/zum/video.mp4'
# Konstruiere den vollen Pfad zur Untertiteldatei
subtitle_file = os.path.join(os.getcwd(), 'tmp', 'subtitel.vtt')
output_file = '/pfad/zum/ausgabevideo.mp4'
combine_video_with_subtitle(video_file, subtitle_file, output_file)
