from intervals.store import (
	get as get_interval,
	get_all as get_all_intervals
)

from notes.store import (
	get as get_note,
	get_sequence as get_notes_sequence
)

from modes.store import (
	get as get_mode,
	get_scale_from_mode
)

from chords.store import get as get_chord, get_voicing

# a0 = get_note('A', octave=0)

# chroma0 = get_notes_sequence('A#', 'C')
# for n in chroma0:
# 	print(n.describe())

ionian = get_mode('ionian')
g_maj = get_scale_from_mode(ionian, 'G')
#print(g_maj.describe())

major = get_chord('major')
c_maj_voicing = get_voicing(major, root='C')

#print(major.describe())
print(c_maj_voicing)