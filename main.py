from intervals.store import (
	get as get_interval,
	get_all as get_all_intervals
)
from intervals.ops import interval_between, augment_interval, diminish_interval


from notes.store import (
	get as get_note,
	get_sequence as get_notes_sequence
)
from notes.ops import add_interval

from modes.store import (
	get as get_mode,
	get_scale_from_mode
)

from chords.store import get as get_chord, get_voicing

a0 = get_note('A', octave=0)
a1 = get_note('A#', octave=1)

a0_a1_interval = interval_between(a0, a1)
print(a0_a1_interval)
print(diminish_interval(a0_a1_interval))

print(add_interval(a0, a0_a1_interval))

# chroma0 = get_notes_sequence('A#', 'C')
# for n in chroma0:
# 	print(n.describe())

# ionian = get_mode('ionian')
# g_maj = get_scale_from_mode(ionian, 'G')
# print(g_maj.describe())

# major = get_chord('major')
# c_maj_voicing = get_voicing(major, root='C')

# print(major.describe())
# print(c_maj_voicing)