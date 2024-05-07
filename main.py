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

def input_path():
    a = False
    while a == False: 
        # Fordere den Benutzer auf, den Dateipfad einzugeben
        old_path = input("Geben Sie den Pfad zur Datei ein: ")
        # Überprüfe, ob der angegebene Pfad gültig ist
        if os.path.isfile(old_path):
            filename = TempFileManager.get_file_name(old_path)
            file_path = TempFileManager.copy_to_tmp_directory(old_path,filename)
            a = True
        else:
            print("Ungültiger Dateipfad.")
    print(f"Der Untertitel wird nun erzeugt.")
    return file_path,old_path, filename


async def main():
    tmp = TempFileManager()
    #tmp.delete_tmp_folder() #für das debugging
    timer = Tim()
    info = ProgramInfo(
        author="Max Mustermann",
        version="1.0",
        description="Eine coole Anwendung, die alles kann!"
    )
    file_path, old_path, filename = input_path()
    video_duration = tmp.duration_video(file_path)
    d = tmp.readjson()
    ProgramInfo.duration(video_duration, d)
    task = asyncio.create_task(subtitel(file_path, filename))
    '''timer_task = asyncio.create_task(Tim.timer())'''
    execution_time = await task
    #print("Execution Time:", execution_time)
    '''timer_task.cancel()
    try:
        await timer_task
    except asyncio.CancelledError:
        pass'''
    ProgramInfo.neededtime(execution_time)
    output_file = tmp.get_file_name(file_path)
    output_file = os.path.join(os.getcwd(), filename,  output_file + '_subtitle.mp4')
    subtitle = os.path.join(os.getcwd(), filename, filename +'_subtitel.srt')
    tmp.combine_video_with_subtitle(file_path, subtitle, output_file)
    #print(filename +'/' +filename + '.mp4')
    tmp.delete_tmp_file(file_path)
    #print (file_path)
    t = TempFileManager.move_tmp_directory_back(old_path,filename)
    ProgramInfo.lines()
    print(f"Das Video hat jetzt einen untertitel und liegt im Verzeichnis {old_path}")
    ProgramInfo.lines()

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
    from installation import Installation
    from design import ProgramInfo
    json_file_path = "src/data.json"
    # Überprüfen, ob die Datei bereits vorhanden ist
    if not os.path.exists(json_file_path):
        Installation.startup()
    asyncio.run(main())