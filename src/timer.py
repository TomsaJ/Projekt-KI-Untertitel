import asyncio
import time
import os
import sys
src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(src_path)
from whisperfile import Subtitle_gen
from file import TempFileManager
from moviepy.editor import VideoFileClip
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
        filename = 'time.csv'
        await Tim.calculate_average(filename)

    
    
    def calculate_average():
        filename = os.path.join(os.getcwd(), 'src', 'time.csv')
        total = 0
        count = 0

        with open(filename, 'r') as file:
            for line in file:
                # Trenne die Zeile anhand des Semikolons
                values = line.strip().split(';')
                
                # Extrahiere den ersten und zweiten Wert als Gleitkommazahlen
                first_value, second_value = map(float, values)
                
                # Füge das Ergebnis zur Gesamtsumme hinzu
                total += first_value / second_value
                #print(first_value / second_value)
                count += 1

        # Berechne den Durchschnitt
        average = total / count 
        #print(average)

        return average

    def fillfile(paths):
        #print("Folgende videos laufen durch den Test")
        summe_time = 0
        ini_time = time.time()
        i = 0
        #for file_path in paths:
        #    print(file_path)
        #print ("---------------\nStart")
        for file_path in paths:
            file = os.path.join(os.getcwd(), 'video', file_path)
            #filename = TempFileManager.get_file_name(file)
            filename = 'tmp'
            file = TempFileManager.copy_to_tmp_directory(file,filename)
            
            #print(file, filename)
            start_time = time.time()
        # Annahme: Die Funktion untertitel(file_path) erstellt Untertitel für das Video
            asyncio.run(Subtitle_gen.untertitel(file,filename))
            output_file = os.path.join(os.getcwd(), filename,  file_path + '_subtitle.mp4')
            subtitle = os.path.join(os.getcwd(), filename, filename +'_subtitel.srt')
            TempFileManager.combine_video_with_subtitle(file, subtitle, output_file)
            end_time = time.time()
            execution_time = end_time - start_time
            #print("Der Untertitel wurde in {:.5f} Sekunden erzeugt.".format(execution_time))
        
            video_file = file_path
            clip = VideoFileClip(file)
            video_duration = clip.duration
            clip.close()
            #print(f'Video länge: {video_duration}')
            #print(f'Pro Sekunde {execution_time/video_duration}')
            csv_file_path = os.path.join(os.getcwd(), "src", 'time.csv')
            if i == 0:
                with open(csv_file_path, 'w') as file:
                    file.write(f'{execution_time};{video_duration}\n')
            else:
                with open(csv_file_path, 'a') as file:
                    file.write(f'{execution_time};{video_duration}\n')
            while i == 0:
                print(f'Die Installation wird {(((execution_time/video_duration)*(60*60))/60)%60: .2f} Minuten dauern' )
                time_init = ((execution_time/video_duration)*(60*60))/60
                i =1
            #print ("---------------------\n")
            init_time_end = time.time()
            init_time_end = init_time_end - ini_time
            summe_time = summe_time + (init_time_end/60)
            if ((summe_time)/time_init) * 100 <= 100:
                print (f'Es sind schon {((summe_time)/time_init) * 100: .2f} % ')
        print('Es sind schon 100 % ')

async def main():
    #time = Tim
    # Starte die asynchrone Methode in einem Task
    task = asyncio.create_task(Tim.async_method())

    # Starte den Timer in einem separaten Task
    #timer_task = asyncio.create_task(time.timer())

    # Warte auf das Ende der asynchronen Methode
    await task

    # Beende den Timer
    #timer_task.cancel()
    #try:
    #    await timer_task
    #except asyncio.CancelledError:
    #    pass

if __name__ == "__main__":
    asyncio.run(Tim.async_method())

# Beispielaufruf des Skripts
#filename = 'time.csv'  # Passe den Dateinamen entsprechend an
#result = Time.calculate_average(filename)
#print("Durchschnitt:", result)
