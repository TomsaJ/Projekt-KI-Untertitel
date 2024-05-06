# main.py

class ProgramInfo:
    def __init__(self, author, version, description):
        self.author = "Laureen Roccotelli und Julian Maximilian Tomsa"
        self.version = "1.2"
        self.description = "Erstellt mit whisper einen Untertitel\nfür das ausgewählte Video und verbindet beides miteinander"
        ProgramInfo.print_info(self)

    def print_info(self):
        print("=" * 60)
        print("          Videos mit Untertitel")
        print("=" * 60)
        print(f"Autor: {self.author}")
        print(f"Version: {self.version}")
        print(f"Beschreibung: {self.description}")
        print("=" * 60)
    
    def duration(video_duration, d):
        print(f"Dauert: {(video_duration * d)/60:.2f} Minuten")

    def neededtime(execution_time):
        print("Der Untertitel wurde in {:.2f} Sekunden erzeugt.".format((execution_time/60)%60))

    def lines():
        print("=" * 60)

if __name__ == "__main__":
    info = ProgramInfo(
        author="Max Mustermann",
        version="1.0",
        description="Eine coole Anwendung, die alles kann!"
    )
