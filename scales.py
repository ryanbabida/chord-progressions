def getScale(notes, frequencies, scales_choices):
  root = notes[scales_choices[0]]

  if scales_choices[1] == 1:
    scale = [frequencies[root], frequencies[root + 2], 
           frequencies[root + 4], frequencies[root + 5],
           frequencies[root + 7], frequencies[root + 9], 
           frequencies[root + 11], frequencies[root + 12]]

  else:
    scale = [frequencies[root], frequencies[root + 2], 
           frequencies[root + 3], frequencies[root + 5],
           frequencies[root + 7], frequencies[root + 8], 
           frequencies[root + 10], frequencies[root + 12]]

  return scale