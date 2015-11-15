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

  if hasOctaveNum(prog_choices[0]) == False:
  	prog_choices[0] += '4'

  progression = prog_choices[1].split()

  return progression

def get_Prog(notes, frequencies, key, progression):
  print ""