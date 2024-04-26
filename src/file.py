import os
import shutil
import ffmpeg

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
    def convert_subtitle_me(subtitle_file, converted_subtitle_file):
        try:
            (
            ffmpeg
                .input(subtitle_file)
                .output(converted_subtitle_file, format='srt')  # Konvertiere in das SRT-Format
                .run(overwrite_output=True)
            )
            print("Die Untertiteldatei wurde erfolgreich konvertiert.")
            return converted_subtitle_file
        except ffmpeg.Error as e:
            print(f"Fehler beim Konvertieren der Untertiteldatei: {e.stderr}")
            return None

    @staticmethod
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

