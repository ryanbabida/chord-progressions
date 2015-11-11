def menu():
  print "Welcome to Chord Progressions"
  print "Choose one:"
  print "1. Scales"
  print "2. Progressions"
  print "0. Quit"
  choice = int(input())
  return choice

def scales():
  print "For the scale, choose the desired key: "
  choice = raw_input()
  return choice

def progressions():
  choices = list()

  print "For the progression, choose the desired key: "
  choices.append(raw_input())

  print "For the progression, type the progression: "
  choices.append(raw_input())
  return choices



