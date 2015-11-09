import pyaudio

def storing_Freq(notes, notes_octave):
  octave_num = 0;

  for x in range(0, 88):
    freq = 400 * pow(2, float(x - 46.35)/12)
    if notes_octave[x % len(notes_octave)] == 'B':
   	  octave_num = octave_num + 1
    key = notes_octave[x % len(notes_octave)] + str(octave_num)
    notes[key] = freq