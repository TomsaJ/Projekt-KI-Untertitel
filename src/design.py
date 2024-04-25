# main.py

class ProgramInfo:
    def __init__(self, author, version, description):
        self.author = author
        self.version = version
        self.description = description
        print_info(self)

    def print_info(self):
        print("=" * 50)
        print("          COOLE ANWENDUNG")
        print("=" * 50)
        print(f"Autor: {self.author}")
        print(f"Version: {self.version}")
        print(f"Beschreibung: {self.description}")
        print("=" * 50)

if __name__ == "__main__":
    info = ProgramInfo(
        author="Max Mustermann",
        version="1.0",
        description="Eine coole Anwendung, die alles kann!"
    )
