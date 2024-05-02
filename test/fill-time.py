import os
import sys
import shutil
import time
import ssl
from moviepy.editor import VideoFileClip

src_path = "/home/jutom001/kitime/src"
sys.path.append(src_path)

def main():
    tmp = TempFileManager()
    paths = ['1min.mp4','10min.mp4','15min.mp4', '20min.mp4', '30min.mp4', '45min.mp4', '90min.mp4']
    print("Folgende videos laufen durch den Test")
    for file_path in paths:
        print(file_path)
    print ("---------------\nStart")
    for file_path in paths:
        file = os.path.join(os.getcwd(), '/home/jutom001/kitime/video', file_path)
        filename = tmp.get_file_name(file)
        tmp.copy_to_tmp_directory(file_path)
        print(file_path)
        start_time = time.time()
        # Annahme: Die Funktion untertitel(file_path) erstellt Untertitel für das Video
        untertitel(file,filename)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Der Untertitel wurde in {:.5f} Sekunden erzeugt.".format(execution_time))
        
        video_file = file_path
        clip = VideoFileClip(file)
        video_duration = clip.duration
        clip.close()
        print(f'Video länge: {video_duration}')
        print(f'Pro Sekunde {execution_time/video_duration}')
        csv_file_path = os.path.join(os.getcwd(), "/home/jutom001/kitime/src", 'time.csv')
        if os.path.exists(csv_file_path) and os.path.getsize(csv_file_path) == 0:
            with open(csv_file_path, 'w') as file:
                file.write('Ausführungszeit;Dauer des Videos\n')
        with open(csv_file_path, 'a') as file:
            file.write(f'{execution_time};{video_duration};{execution_time/video_duration}\n')
        print ("---------------------\n")
    tmp.delete_tmp_folder()

if __name__ == "__main__":
    src_path = "/home/jutom001/kitime/src"
    sys.path.append(src_path)
    from installwhisper import check_and_install_package
    from whisperfile import untertitel
    from file import TempFileManager
    main()