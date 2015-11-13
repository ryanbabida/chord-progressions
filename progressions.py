def hasOctaveNum(inputString):
  return any(char.isdigit() for char in inputString)

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