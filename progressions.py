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

  if hasOctaveNum(prog_choices[0]) == False:
  	prog_choices[0] += '4'

  roman_num = [["I": 1, "Major"], ["i": 1, "Minor"], 
               ["II": 2, "Major"], ["ii": 1, "Minor"],
               ["III": 3, "Major"], ["iii": 3, "Minor"],
               ["IV": 4, "Major"], ["iv": 4, "Minor"],
               ["V": 5, "Major"], ["v": 5, "Minor"], 
               ["VI": 6, "Major"], ["vi": 6, "Minor"],
               ["VII": 7, "Major"], ["vii": 7, "Minor"]]

  progression = prog_choices[1].split()
  '''
  for x in range (0, len(progression)):
     parsed_prog.append(roman_num[progression[x]])
    '''
  print roman_num

  return progression

def get_Prog(notes, frequencies, key, progression):
  print ""