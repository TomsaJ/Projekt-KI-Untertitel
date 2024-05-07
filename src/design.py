# main.py

class ProgramInfo:
    def __init__(self):
        self.author = "Laureen Roccotelli und Julian Maximilian Tomsa"
        self.github = "Github: LauriTrite und TomsaJ"
        sef.repo = "Repo: https://github.com/TomsaJ/Projekt-KI-Untertitel.git"
        self.version = "1.2.2"
        self.description = "Erstellt mit whisper einen Untertitel für das\nausgewählte Video und verbindet beides miteinander"
        ProgramInfo.print_info(self)

    def print_info(self):
        ProgramInfo.lines()
        print("                     Videos mit Untertitel")
        ProgramInfo.lines()
        print(f"Autor: {self.author}")
        print(f"Version: {self.version}")
        print(f"Beschreibung: {self.description}")
        ProgramInfo.lines()
    
    def duration(video_duration, d):
        print(f"Dauert: {(video_duration * d)/60:.2f} Minuten")

    def neededtime(execution_time):
        print("Der Untertitel wurde in {:.2f} Sekunden erzeugt.".format((execution_time/60)%60))

    def lines():
        print("=" * 65)

if __name__ == "__main__":
    info = ProgramInfo(
        author="Max Mustermann",
        version="1.0",
        description="Eine coole Anwendung, die alles kann!"
    )
