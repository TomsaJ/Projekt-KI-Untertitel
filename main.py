import os
import sys
import shutil
import time
import ssl
import asyncio

src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(src_path)

async def subtitel(file_path, filename):
        sub = Subtitle_gen()
        start_time = time.time()
        # Hier wird untertitel(file_path) aufgerufen oder implementiert
        await sub.untertitel(file_path,filename)
        #await asyncio.sleep(10)
        end_time = time.time()
        execution_time = end_time - start_time
        return execution_time


async def main():
    tmp = TempFileManager()
    tmp.delete_tmp_folder() #für das debugging
    timer = Tim()
    a = False
    while a == False: 
        # Fordere den Benutzer auf, den Dateipfad einzugeben
        file_path = input("Geben Sie den Pfad zur Datei ein: ")
        # Überprüfe, ob der angegebene Pfad gültig ist
        if os.path.isfile(file_path):
            file_path = tmp.copy_to_tmp_directory(file_path)
            a = True
        else:
            print("Ungültiger Dateipfad.")
    print(f"Der Untertitel wird nun erzeugt.")
    video_file = file_path

    # VideoClip-Objekt erstellen
    clip = VideoFileClip(video_file)

    # Dauer des Videos in Sekunden
    video_duration = clip.duration

    # Schließen des Clips
    clip.close()
    print(f"Dauert: {(video_duration * 0.041648740525032146)/60} Minuten")
    filename = tmp.get_file_name(file_path)
    # Starte die asynchrone Methode subtitel() in einem Task
    task = asyncio.create_task(subtitel(file_path, filename))

# Erstelle einen Task für die Methode timer() der Klasse Time
    '''timer_task = asyncio.create_task(Tim.timer())'''

# Warte auf das Ende der asynchronen Methode subtitel()
    execution_time = await task
    #print("Execution Time:", execution_time)

# Beende den Timer
    '''timer_task.cancel()
    try:
        await timer_task
    except asyncio.CancelledError:
        pass'''
    print("Der Untertitel wurde in {:.5f} Sekunden erzeugt.".format(execution_time/60))
    output_file = tmp.get_file_name(file_path)
    output_file = os.path.join(os.getcwd(), 'tmp',  output_file + '_subtitle.mp4')
    #subtitle = '/home/jutom001/KI/DieTulpe.srt'
    subtitle = os.path.join(os.getcwd(), 'tmp', 'subtitel.srt')
    #tmp.convert_subtitle_me(subtitle)
    tmp.combine_video_with_subtitle(file_path, subtitle, output_file)
    # Beispielaufruf
    #output_file = '/path/to/output/combined_video.mp4'
    #tmp.delete_tmp_folder()
    video_file = file_path

    # VideoClip-Objekt erstellen
    clip = VideoFileClip(video_file)

    # Dauer des Videos in Sekunden
    video_duration = clip.duration

# Schließen des Clips
    clip.close()
    '''file_path = os.path.join(os.getcwd(), 'src', 'time.csv')
    if os.path.exists(file_path) and os.path.getsize(file_path) == 0:
        with open(file_path, 'w') as file:
            file.write('Ausführungszeit;Dauer des Videos\n')

# Öffnen der Datei im Anhänge-Modus ('a')
    with open(file_path, 'a') as file:
    # Schreiben der Ausführungszeit und der Videodauer in die Datei
        file.write(f'{execution_time};')
        file.write(f'{video_duration/60}')'''

if __name__ == "__main__":
    #ssl._create_default_https_context = ssl._create_unverified_context
    src_path = os.path.join(os.path.dirname(__file__), 'src')
    sys.path.append(src_path)
    from installwhisper import check_and_install_package
    check_and_install_package('openai-whisper')
    check_and_install_package('ffmpeg-python')
    check_and_install_package('moviepy')
    from moviepy.editor import VideoFileClip
    from whisperfile import Subtitle_gen
    from file import TempFileManager
    from timer import Tim
    asyncio.run(main())