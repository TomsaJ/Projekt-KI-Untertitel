import os
import sys
import shutil

src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(src_path)

# Importiere die Funktion Untertitel aus der Datei whisper.py
from whisperfile import untertitel


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

if __name__ == "__main__":
    # Fordere den Benutzer auf, den Dateipfad einzugeben
    file_path = input("Geben Sie den Pfad zur Datei ein: ")

    # Überprüfe, ob der angegebene Pfad gültig ist
    if os.path.isfile(file_path):
        copy_to_tmp_directory(file_path)
    else:
        print("Ungültiger Dateipfad.")
    untertitel(file_path)
