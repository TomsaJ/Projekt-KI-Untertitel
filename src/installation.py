import sys
import os
src_path = "/home/jutom001/KI/src"
sys.path.append(src_path)
from file import TempFileManager

class Installation:
    @staticmethod
    def startup():
        tmp = TempFileManager()
        # Assuming jsonfile() is defined outside of TempFileManager class
        tmp.jsonfile(12)





if __name__ == "__main__":
    Installation.startup()