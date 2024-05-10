# Projekt-KI-Untertitel

## Beschreibung
Diese Anwendung erstellt einen Untertitel mit dem KI-Model [Whisper](https://github.com/openai/whisper), das von OpenAI entwickelt worden ist. Es wird zum einen eine Untertitel-Datei erstellt (SRT-Datei),
die anschließend mit einem Video (mp4) zusammen kombiniert wird. Außerdem wird eine Text-Datei erstellt, in der der gesamte gesprochenen Text gespeichert wird.

## Voraussetzung
whisper-openai wird beim Programmstart automatisch installiert sowie movipy und ffmepg-python. Wichtig ist auch das ffmpeg installiert ist.

## Autor
Entwickelt wurde dieses Projekt von [LauriTrite](https://www.github.com/LauriTrite) und [TomsaJ](https://www.github.com/TomsaJ)

## Version
Aktuelle Version v1.3

## Ausführung
Nach dem Start des Programms wird nach dem Video gefragt in FOrm eines Pfads. Es ist möglich den Pfad einzutippen, einfach ist es aber das Video in das Terminalfenster zu ziehen. Es wird ein Ordner erstellt mit dem Video, das nun einen Untertitel hat, der SRT-Datei und einer Text-Datei.
Dieser Ordner befindet sich im gleichen Pfad, wie das Video. DIes wird aber auch nochmal im Terminal angezeigt.

# Installation
In diesem Repo liegt eine Standard-Config bei. Diese Config beinhaltet einen Durchschnittswert, der die dauer 1er-Sekunde eines videos braucht um einen unter titel zu generieren und hinzuzufügen.
In diesem Fall wurde der Standardwert mit einer NVIDIA GPU ermittel, diese liegt bei 0.14346300072019624 pro Sekunde.
Um Umkehrschluss bedeutet das, dass die richtige Dauer abweichen kann. 
Um eine genauere geschätzte Zeit zuhaben kann die Software mit dem folgenden Link heruntergeladen werden (Link). Bei der Installation werden 4 Videos durchlaufen, um einen genaueren Schätzwert für 
deine CPU/GPU zu ermitteln.
