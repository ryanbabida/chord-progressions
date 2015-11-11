from frequencies import *
from note import *

# Need to implement getScales
# ex: F4 -> F4 G4 A4 Bb4 C5 D5 E5 F5

def main():
  frequencies = list()
  notes = dict()
  notes_octave = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 
  					'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#, Ab']
  storing_Freq(frequencies, notes, notes_octave)

  # print frequencies[notes['C4']]

  for x in range(0, 88):
    print frequencies[x].note_name
 
if __name__ == '__main__':
    main()