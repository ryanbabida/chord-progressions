def menu():
  print "Welcome to Chord Progressions"
  print "Choose one:"
  print "1. Scales"
  print "2. Chords"
  print "3. Progressions"
  print "0. Quit"
  choice = int(input())
  return choice

def scales_prompt():
  choices = list()

  print "For the scale, choose the desired key: "
  choices.append(raw_input())

  print "1. Major Scale"
  print "2. Natural Minor Scale"
  choices.append(int(raw_input()))
  return choices

def chords_prompt():
  print "Enter the desired chord (eg. Cm7 -> C4 Minor 7): "
  return (raw_input())

def progressions_prompt():
  choices = list()

  print "For the progression, choose the desired key: "
  choices.append(raw_input())

  print "For the progression, type the progression: "
  choices.append(raw_input())
  return choices

def display_result(result):
  print "Result: "
  for x in result:
    print x.note_name,
  print "\n"

def display_prog(result):
  print "Result: "
  for x in result:
    print "Root note:", x[0].note_name, "\nChord:"
    for y in x:
      print y.note_name,
    print "\n"




