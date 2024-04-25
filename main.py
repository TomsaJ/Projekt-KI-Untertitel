import os
import sys
import shutil
import time

src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(src_path)

# Importiere die Funktion Untertitel aus der Datei whisper.py
from whisperfile import untertitel
from installwhisper import check_and_install_package
from transferfile import TempFileManager


if __name__ == "__main__":
    tmp = TempFileManager()
    a = False
    check_and_install_package()
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
    tmp.delete_tmp_folder()
    
