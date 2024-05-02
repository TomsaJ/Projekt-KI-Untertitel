import asyncio
import time
import os
import sys
src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(src_path)
from whisperfile import Subtitle_gen
class Tim:

    @staticmethod
    async def timer():
        start_time = time.time()
        while True:
            elapsed_time = time.time() - start_time
            print("Elapsed Time: {:.2f} seconds".format(elapsed_time))
            await asyncio.sleep(1)  # Warte 1 Sekunde
    async def async_method():
    # Hier kommt der Code deiner asynchronen Methode
        await asyncio.sleep(20)  # Beispiel: Warten für 5 Sekunden

    
    
    async def calculate_average(filename):
        total = 0
        count = 0

        with open(filename, 'r') as file:
            # Ignoriere die erste Zeile
            next(file)
            
            for line in file:
                # Trenne die Zeile anhand des Semikolons
                values = line.strip().split(';')
                
                # Extrahiere den ersten und zweiten Wert als Gleitkommazahlen
                first_value, second_value = map(float, values)
                
                # Füge das Ergebnis zur Gesamtsumme hinzu
                total += first_value / second_value
                print(first_value / second_value)
                count += 1

        # Berechne den Durchschnitt
        average = total / count if count > 0 else 0

        return average

async def main():
    time = Tim
    # Starte die asynchrone Methode in einem Task
    task = asyncio.create_task(time.async_method())

    # Starte den Timer in einem separaten Task
    timer_task = asyncio.create_task(time.timer())

    # Warte auf das Ende der asynchronen Methode
    await task

    # Beende den Timer
    timer_task.cancel()
    try:
        await timer_task
    except asyncio.CancelledError:
        pass

if __name__ == "__main__":
    asyncio.run(main())

# Beispielaufruf des Skripts
#filename = 'time.csv'  # Passe den Dateinamen entsprechend an
#result = Time.calculate_average(filename)
#print("Durchschnitt:", result)
