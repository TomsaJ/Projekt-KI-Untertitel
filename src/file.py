import os
import shutil
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
        print (f"Der Untertitel wird nun erzeugt.")
    except FileNotFoundError:
        print("Die angegebene Datei existiert nicht.")
    except PermissionError:
        print("Zugriff verweigert. Überprüfen Sie die Berechtigungen.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
    return destination_path

def get_file_name(file_path):
    # Extrahiere den Dateinamen aus dem Dateipfad
    file_name_with_extension = os.path.basename(file_path)
    # Trenne den Dateinamen und die Erweiterung
    file_name, file_extension = os.path.splitext(file_name_with_extension)
    # Gib den Dateinamen zurück
    return file_name