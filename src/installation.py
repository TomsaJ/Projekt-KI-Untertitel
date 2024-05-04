import sys
import os
src_path = "/home/jutom001/KI/src"
sys.path.append(src_path)
from file import TempFileManager as tmp
from timer import Tim

class Installation:
    @staticmethod
    def startup():
        # Assuming jsonfile() is defined outside of TempFileManager class
        paths = ['10min.mp4','15min.mp4', '20min.mp4', '30min.mp4', '45min.mp4']
        Tim.fillfile(paths)
        installtatio_neede_time = Tim.calculate_average()
        tmp.jsonfile(installtatio_neede_time)
        tmp.delete_tmp_file()





if __name__ == "__main__":
    Installation.startup()
        #0.1220757381170537