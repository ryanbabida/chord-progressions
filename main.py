from frequencies import *

def main():
  notes = dict()
  notes_octave = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 
  					'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#, Ab']
  storing_Freq(notes, notes_octave)

  print notes['A4']

if __name__ == '__main__':
    main()