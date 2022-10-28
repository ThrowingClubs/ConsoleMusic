
import pyaudio as pa
import numpy as np
from itertools import cycle, compress, dropwhile, islice

# global sampling rate
fs = 44100

class SoundLib:

    def __init__(self):
        self.noteFreqMap = {}
        self.buildNoteFreqMap()
        self.pa = pa.PyAudio()
        
        self.allNotes = ["c","c#","d","d#","e","f","f#","g","g#","a","a#","b"]

        # for paFloat32 sample values must be in range [-1.0, 1.0]
        self.stream = self.pa.open(format=pa.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)
        return

    def __del__(self):
        self.stream.stop_stream()
        self.stream.close()
        self.pa.terminate()
        return

    def playNote(self, note, duration, octave = 4, volume = .5):
        freq = self.getNoteFreq(note, octave)

        # generate samples, note conversion to float32 array
        sampleRange = np.arange(fs*duration)
        samples = ((np.sin(2 * np.pi * sampleRange * freq / fs))*np.sin(np.pi*sampleRange/fs)).astype(np.float32)

        output_bytes = (volume * samples).tobytes()

        self.stream.write(output_bytes)
        return

    def buildNoteFreqMap(self):
        self.noteFreqMap["c"] = [16.35*(2**i) for i in range(9)]
        self.noteFreqMap["c#"] = [17.32*(2**i) for i in range(9)]
        self.noteFreqMap["d"] = [18.35*(2**i) for i in range(9)]
        self.noteFreqMap["d#"] = [19.45*(2**i) for i in range(9)]
        self.noteFreqMap["e"] = [20.60*(2**i) for i in range(9)]
        self.noteFreqMap["f"] = [21.83*(2**i) for i in range(9)]
        self.noteFreqMap["f#"] = [23.12*(2**i) for i in range(9)]
        self.noteFreqMap["g"] = [24.5*(2**i) for i in range(9)]
        self.noteFreqMap["g#"] = [25.96*(2**i) for i in range(9)]
        self.noteFreqMap["a"] = [27.5*(2**i) for i in range(9)]
        self.noteFreqMap["a#"] = [29.14*(2**i) for i in range(9)]
        self.noteFreqMap["b"] = [30.87*(2**i) for i in range(9)]
        return

    def getNoteFreq(self, desiredNote, octave = 4):
        return self.noteFreqMap[desiredNote.lower()][octave]

    def getNotesInKey(self, baseNote, major = True):
        majorMap = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]
        minorMap = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0]
        notes = dropwhile(lambda note: note != baseNote, cycle( self.allNotes))
        if major:
            return list(compress(islice(notes,len(majorMap)),majorMap))
        else: 
            return list(compress(islice(notes,len(minorMap)),minorMap))

if __name__ == "__main__":
    soundLib = SoundLib()
