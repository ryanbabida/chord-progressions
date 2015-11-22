def hasOctaveNum(inputString):
  return any(char.isdigit() for char in inputString)


# If octave number is not specified,
# defaults to octave 4 (eg. C -> C4)
def getScale(notes, frequencies, scales_choices):
  if hasOctaveNum(scales_choices[0]) == False:
  	scales_choices[0] += '4'

  root = notes[scales_choices[0]]

  scale = list()

  if scales_choices[1] == 1:
    scale = [frequencies[root], frequencies[root + 2], 
           frequencies[root + 4], frequencies[root + 5],
           frequencies[root + 7], frequencies[root + 9], 
           frequencies[root + 11], frequencies[root + 12]]

  elif scales_choices[1] == 2:
    scale = [frequencies[root], frequencies[root + 2], 
           frequencies[root + 3], frequencies[root + 5],
           frequencies[root + 7], frequencies[root + 8], 
           frequencies[root + 10], frequencies[root + 12]]

  return scale