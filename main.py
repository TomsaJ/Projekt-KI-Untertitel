import os
import sys
import shutil
import time

src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(src_path)


from whisperfile import untertitel
from installwhisper import check_and_install_package
from file import TempFileManager

def main():
    tmp = TempFileManager()
    a = False
    check_and_install_package('openai-whisper')
    check_and_install_package('ffmpeg-python')
    check_and_install_package('vtt-to-srt3')
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
    start_time = time.time()
    untertitel(file_path)
    end_time = time.time()
    execution_time = (end_time - start_time)/60
    print("Die Testfunktion wurde in {:.5f} Minuten ausgeführt.".format(execution_time))
    output_file = tmp.get_file_name(file_path)
    output_file = os.path.join(os.getcwd(), 'tmp',  output_file + '_subtitle.mp4')
    #subtitle = '/home/jutom001/KI/tmp/subtitel.vtt' 
    subtitle = os.path.join(os.getcwd(), 'tmp', 'subtitel.vtt')
    tmp.convert_subtitle_me(subtitle)
    tmp.combine_video_with_subtitle(file_path, subtitle, output_file)
    # Beispielaufruf
    #output_file = '/path/to/output/combined_video.mp4'
    #tmp.delete_tmp_folder()


if __name__ == "__main__":
    main()