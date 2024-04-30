import os
import shutil
import ffmpeg
import subprocess



class TempFileManager:
    @staticmethod
    def copy_to_tmp_directory(file_path):
        # Erstelle einen temporären Ordner im aktuellen Verzeichnis
        tmp_folder = os.path.join(os.getcwd(), 'tmp')
        os.makedirs(tmp_folder, exist_ok=True)

        # Extrahiere den Dateinamen aus dem angegebenen Pfad
        file_name = os.path.basename(file_path)

        # Konstruiere den Ziel-Pfad im temporären Ordner
        destination_path = os.path.join(tmp_folder, file_name)

        try:
            # Kopiere die Datei in den temporären Ordner
            shutil.copy(file_path, destination_path)
            print(f"Die Datei wurde erfolgreich nach {destination_path} kopiert.")
        except FileNotFoundError:
            print("Die angegebene Datei existiert nicht.")
        except PermissionError:
            print("Zugriff verweigert. Überprüfen Sie die Berechtigungen.")
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
        return destination_path

    @staticmethod
    def delete_tmp_folder():
        folder_path = "tmp"  # Pfad zum zu löschenden Ordner
        try:
            shutil.rmtree(folder_path)
            print("Der Ordner 'tmp' wurde erfolgreich gelöscht.")
        except FileNotFoundError:
            print("Der Ordner 'tmp' wurde nicht gefunden.")
        except PermissionError:
            print("Keine Berechtigung zum Löschen des Ordners 'tmp'.")
        except Exception as e:
            print("Ein Fehler ist beim Löschen des Ordners 'tmp' aufgetreten:", e)

    @staticmethod
    def get_file_name(file_path):
        # Extrahiere den Dateinamen aus dem Dateipfad
        file_name_with_extension = os.path.basename(file_path)
        # Trenne den Dateinamen und die Erweiterung
        file_name, file_extension = os.path.splitext(file_name_with_extension)
        # Gib den Dateinamen zurück
        return file_name

    @staticmethod
    def convert_subtitle_me(subtitle_file):
        from vtt_to_srt.vtt_to_srt import ConvertFile

        convert_file = ConvertFile(subtitle_file, "utf-8")
        convert_file.convert()

    @staticmethod
    def combine_video_with_subtitle(video_file, subtitle_file, output_file):
    # Überprüfen, ob die Dateien existieren
        if not os.path.exists(video_file):
            print("Video file not found.")
            return
        if not os.path.exists(subtitle_file):
            print("Subtitle file not found.")
            return
        print(f"Video: {video_file} Subtitle: {subtitle_file} Output: {output_file}")

        #(ffmpeg
        #.input(video_file)
        #.output(output_file, vcodec='copy', acodec='copy', scodec='mov_text', **{'metadata:s:s:0': 'language=ger'})
        #.output(subtitle_file, **{'metadata:s:s:0': 'language=ger'})
        #.run())

        #video = ffmpeg.input(video_file)
        #audio = video.audio
        #subtitles = ffmpeg.input(subtitle_file)
        #(ffmpeg.output(video, audio, subtitles, output_file, vcodec='copy', acodec='copy').run())

        #ffmpeg.input(video_file).output(output_file, vcodec='copy', acodec='copy').output(subtitle_file, c:s='mov_text').run()
        # FFmpeg-Befehl zum Kombinieren von Video und Untertiteln
        cmd = [
        "ffmpeg",
    "-i", video_file,
    "-i", subtitle_file,
    "-c:v", "copy",
    "-c:a", "copy",
    "-c:s", "mov_text",
    "-map", "0:v:0",
    "-map", "0:a:0",
    "-map", "1:s:0",
    "-metadata:s:s:0", "language=ger",
    output_file
    ]    
            
    # FFmpeg-Befehl ausführen
        with open(os.devnull, 'w') as devnull:
            subprocess.run(cmd, stdout=devnull, stderr=subprocess.STDOUT)
        print("Video hat jetzt einen untertitel")
        #subprocess.run(cmd)
        #try:
            #ffmpeg_cmd = f'ffmpeg -i {video_file} -i {subtitle_file} -c:s mov_text -c:v copy -c:a copy {output_file}'

    # Führe den FFmpeg-Befehl aus
            #subprocess.run(ffmpeg_cmd, check=True, shell=True)
            #print("Die Video-Datei wurde erfolgreich mit den Untertiteln kombiniert und gespeichert.")
        #except ffmpeg.Error as e:
            #print(f"Fehler beim Kombinieren von Video und Untertiteln: {e.stderr}")

        
        #command = ['ffmpeg', '-i', video_file, '-i', subtitle_file, '-c', 'copy', '-c:s', 'mov_text', output_file]
        #subprocess.run(command)

