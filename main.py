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


# c0 = get_note('C', octave=0)
# e0 = get_note('E', octave=0)
# g0 = get_note('G', octave=0)


# test_maj = build_voicing([c0, e0, g0])
# print(test_maj)
# test_min = build_voicing([c0, flatten(e0), g0])
# print(test_min)

a = flatten(get_note('A'))
print(a.describe())