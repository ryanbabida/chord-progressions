import pyaudio

# Assigns the notes / octave number to a frequency in the notes dict
# Uses the frequency formula
# If the note is B, add 1 to the octave number to get the
# next octave's notes (eg. B0 --> C1)

def storing_Freq(frequencies, notes, notes_octave):
  octave_num = 0;

  for x in range(0, 88):
    freq = 400 * pow(2, float(x - 46.35)/12)
    if notes_octave[x % len(notes_octave)] == 'B':
   	  octave_num = octave_num + 1
    key = notes_octave[x % len(notes_octave)] + str(octave_num)
    notes.append(key)
    frequencies.append(freq)