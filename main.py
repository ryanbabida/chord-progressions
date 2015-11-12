from frequencies import *
from note import *
from user_prompt import *

# Need to implement getScales
# ex: F4 -> F4 G4 A4 Bb4 C5 D5 E5 F5


# Common chord tones (half-steps from root)
_m3rd = 3
_3rd = 4
_5th = 7
_m7th = 10
_7th = 11


def main():
  frequencies = list()
  notes = dict()
  notes_octave = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 
  					'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#, Ab']
  choice = -1

  storing_Freq(frequencies, notes, notes_octave)

  while(choice != 0):
    choice = menu()

    if choice == 1:
  	  scales_choice = scales_prompt()

    if choice == 2:
  	  prog_choices = progressions_prompt()
   
if __name__ == '__main__':
    main()