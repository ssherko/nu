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


# a0 = get_note('A', octave=0)

# chroma0 = get_notes_sequence('A#', 'C')
# for n in chroma0:
# 	print(n.describe())

ionian = get_mode('ionian')
c_maj = get_scale_from_mode(ionian, 'C')
csharp_maj = get_scale_from_mode(ionian, 'C#')
d_maj = get_scale_from_mode(ionian, 'D')

#print(ionian.describe())

print(c_maj.describe())
print(csharp_maj.describe())
print(d_maj.describe())