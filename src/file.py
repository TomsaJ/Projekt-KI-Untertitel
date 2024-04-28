import os
import shutil
import ffmpeg
import subprocess
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from pysubs2 import SSAFile
import moviepy.config as cf

# Setze den Pfad zur ImageMagick-Binärdatei
cf.change_settings({"IMAGEMAGICK_BINARY": "/pfad/zur/convert"})


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
        "-metadata:s:s:0", "language=eng",
        output_file
    ]

    # FFmpeg-Befehl ausführen
        subprocess.run(cmd)
