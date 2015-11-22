from scales import *

def hasOctaveNum(inputString):
  return any(char.isdigit() for char in inputString)

def getChord(notes, frequencies, chord_choices):

  chord = list()
  chord_choices = chord_choices.split()

  if hasOctaveNum(chord_choices[0]) == False:
  	chord_choices[0] += '4'

  root = notes[chord_choices[0]]

  if chord_choices[1] == "Major":
    chord = [frequencies[root], frequencies[root + 4], frequencies[root + 7]]
  elif chord_choices[1] == "Minor":
    chord = [frequencies[root], frequencies[root + 3], frequencies[root + 7]]

  if int(chord_choices[2]) == 7 and chord_choices[1] == "Major": 
    chord.append(frequencies[root + 11])
  elif int(chord_choices[2]) == 7 and chord_choices[1] == "Minor":
    chord.append(frequencies[root + 10])

  if int(chord_choices[2]) == 9:
    chord.append(frequencies[root + 14])

  if int(chord_choices[2]) == 11:
    chord.append(frequencies[root + 17])

  if int(chord_choices[2]) == 13:
    chord.append(frequencies[root + 21])

  return chord

# If octave number is not specified,
# defaults to octave 4 (eg. C -> C4)
def parseProg(prog_choices):
  progression = list()
  parsed_prog = list()


  roman_num = {"I": 1, "i": 1, 
               "II": 2, "ii": 2,
               "III": 3, "iii": 3,
               "IV": 4, "iv": 4,
               "V": 5, "v": 5, 
               "VI": 6, "vi": 6,
               "VII": 7, "vii": 7}

  progression = prog_choices[1].split()

  for x in progression:
    if x.islower() == True:
      parsed_prog.append((roman_num[x] - 1, "Minor"))
    if x.isupper() == True:
      parsed_prog.append((roman_num[x] - 1, "Major"))

  return parsed_prog

def get_Prog(notes, frequencies, key, progression):

  final_prog = list()

  if hasOctaveNum(key) == False:
    key += '4'
 
  scales_choices = [key, 1]
  scale = getScale(notes, frequencies, scales_choices)

  for x in progression:
    chord_choices = scale[x[0]].note_name + ' ' + x[1] + ' 0'

    chord = getChord(notes, frequencies, chord_choices)
    final_prog.append(chord)

  return final_prog






