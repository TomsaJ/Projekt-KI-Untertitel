import os
import sys
import shutil
import time
import ssl
from moviepy.editor import VideoFileClip

src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(src_path)

def main():
    tmp = TempFileManager()
    tmp.delete_tmp_folder() #für das debugging
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
    print(f"Dauert: {((video_duration *0.8) * 0.1642989597170965)/60} Minuten")
    filename = tmp.get_file_name(file_path)
    start_time = time.time()
    untertitel(file_path, filename)
    end_time = time.time()
    execution_time = (end_time - start_time)/60
    print("Der Untertitel wurde in {:.5f} Minuten erzeugt.".format(execution_time))
    output_file = os.path.join(os.getcwd(), 'tmp',  filename + '_subtitle.mp4')
    #subtitle = '/home/jutom001/KI/DieTulpe.srt'
    subtitle = os.path.join(os.getcwd(), 'tmp', filename + '_subtitel.srt')
    #tmp.convert_subtitle_me(subtitle)
    tmp.combine_video_with_subtitle(file_path, subtitle, output_file)
    # Beispielaufruf
    #output_file = '/path/to/output/combined_video.mp4'
    #tmp.delete_tmp_folder()

if __name__ == "__main__":
    #ssl._create_default_https_context = ssl._create_unverified_context
    src_path = os.path.join(os.path.dirname(__file__), 'src')
    sys.path.append(src_path)
    from installwhisper import check_and_install_package
    #check_and_install_package('openai-whisper')
    #check_and_install_package('ffmpeg-python')
    #check_and_install_package('moviepy')

    from whisperfile import untertitel
    from file import TempFileManager
    main()