def hasOctaveNum(inputString):
  return any(char.isdigit() for char in inputString)

def getChord(notes, frequencies, note, type, extensions):

  chord = new list()
  root = notes[note]

  if type == "Major":
    chord = [frequencies[root], frequencies[root + 4], frequencies[root + 7]]
  else type == "Minor":
    chord = [frequencies[root], frequencies[root + 3], frequencies[root + 7]]

  for ext = extensions:
  	if ext = 7:
      chord.append(frequencies[root + 11])
    if ext = 9:
      chord.append(frequencies[root + 14])
    if ext = 11:
      chord.append(frequencies[root + 17])
    if ext = 13:
      chord.append(frequencies[root + 21])

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