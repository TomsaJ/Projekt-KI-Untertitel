import os
import sys
import shutil

src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(src_path)

# Importiere die Funktion Untertitel aus der Datei whisper.py
from whisperfile import untertitel
from installwhisper import check_and_install_package
from transferfile import copy_to_tmp_directory

if __name__ == "__main__":
    a = False
    check_and_install_package()
    while a == False: 
        # Fordere den Benutzer auf, den Dateipfad einzugeben
        file_path = input("Geben Sie den Pfad zur Datei ein: ")
        # Überprüfe, ob der angegebene Pfad gültig ist
        if os.path.isfile(file_path):
            copy_to_tmp_directory(file_path)
            a = True
        else:
            print("Ungültiger Dateipfad.")
    untertitel(file_path)
