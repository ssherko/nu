from intervals.store import (
	get as get_interval,
	get_all as get_all_intervals
)
from intervals.ops import interval_between, augment_interval, diminish_interval


from notes.store import (
	get as get_note,
	get_sequence as get_notes_sequence
)
from notes.ops import (
	add_interval,
	sharpen,
	flatten
)

from modes.store import (
	get as get_mode,
	get_scale_from_mode
)

from chords.store import (
	get as get_chord, 
	get_voicing
)
from chords.ops import build_voicing


ionian = get_mode('ionian')
c_maj_scale = get_scale_from_mode(ionian, root='G')
print(c_maj_scale.describe())

cmaj_iterator = c_maj_scale.iterate_notes()

notes = [ next(cmaj_iterator) for _ in range(24) ]

for i in range(7):
	chord = build_voicing([
		notes[i],
		notes[i+2],
		notes[i+4]
	])
	print(chord)
