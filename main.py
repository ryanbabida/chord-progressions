from frequencies import *
from collections import OrderedDict

def main():
  frequencies = list()
  notes = list()
  notes_octave = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 
  					'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#, Ab']
  storing_Freq(frequencies, notes, notes_octave)
 
if __name__ == '__main__':
    main()