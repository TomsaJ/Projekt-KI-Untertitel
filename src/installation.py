import sys
import os
src_path = "/src"
sys.path.append(src_path)
from file import TempFileManager as tmp
from timer import Tim
from design import ProgramInfo

class Installation:
    @staticmethod
    def startup():
        ProgramInfo.lines()
        print("Die Installation wird gestartet bitte warten ...")
        # Assuming jsonfile() is defined outside of TempFileManager class
        paths = ['1min.mp4','10min.mp4','15min.mp4', '20min.mp4', '30min.mp4']
        Tim.fillfile(paths)
        installtatio_neede_time = Tim.calculate_average()
        tmp.jsonfile(installtatio_neede_time)
        print("Iinstallation beendet")
        ProgramInfo.lines()
        tmp.delete_tmp_folder()
        tmp.delete_tmp_file("src/time.csv")





if __name__ == "__main__":
    Installation.startup()
        #0.1220757381170537