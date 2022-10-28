import sys
import time
from SoundLib import SoundLib
import random

key = "e"
soundlib = SoundLib()
startTime = time.time()+1

def makeMusic(line):
    global key
    notes = soundlib.getNotesInKey(key)
    note = notes[int(hash(line))%len(notes)]
    octive = 4
    volume = 0.5
    if lineIsDebug(line):
        octive = 3
    elif lineIsError(line):
        octive = 5
        allnotes = soundlib.allNotes
        key = allnotes[random.randint(0,len(allnotes)-1)]
        volume = 1
        print(key)
        soundlib.playNote("f", 0.8, 7, 0.25)
    soundlib.playNote(note, 0.1,octave=octive, volume=volume)
    return

def lineIsError(line):
    return line[0:4].lower()=="fail" or line[0:5].lower=="error"
def lineIsDebug(line):
    return line[0:4].lower()=="info" or line[0:4].lower()=="dbug" or line[0:5].lower()=="debug" 
def lineIsWarning(line):
    return line[0:4].lower()=="warn" or line[0:7].lower() == "warning"

def main():
    file = ""
    # gets the file from the command line args, and uses output.txt if no args were supplied
    try: 
        file = sys.argv[1]
    except:
        file = "output.txt"
        
    with open(file, 'r') as f:
        while True:
            for line in iter(f.readline, ''):
                # spend the first second(ish) of runtime just chugging to get to the end of the file
                if time.time() <= startTime:
                    continue
                makeMusic(line)
                print(line, end = "")

if __name__ == "__main__":
    main()
