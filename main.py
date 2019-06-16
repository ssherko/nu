from modes.store import (
	get as get_mode,
	get_scale_from_mode
)
from chords.ops import from_scale as get_chord_scale, extend
from notes.ops import add_interval
from intervals.store import get as get_interval

ionian = get_mode('ionian')

dmaj_scale = get_scale_from_mode(ionian, root='D')
print('Scale: ')
print(dmaj_scale.describe())

dmaj_iterator = dmaj_scale.iterate_notes()
notes = [ next(dmaj_iterator) for _ in range(32) ]

print('Chord Scale:')
voicings = get_chord_scale(dmaj_scale)
for v in voicings:
	print(v)


tonic = voicings[0]
seventh = add_interval(tonic.notes[0], get_interval('M7'))

tonic7 = extend(tonic, [seventh])
print(tonic7)
