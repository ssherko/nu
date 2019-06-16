from intervals.store import (
	get as get_interval,
	get_all as get_all_intervals
)
from intervals.ops import (
	interval_between, 
	augment_interval, 
	diminish_interval
)

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

from synth.store import synthesize_voicing
from synth.utils import (
	init_midi,
	add_voicing,
	persist
)

ionian = get_mode('ionian')
c_maj_scale = get_scale_from_mode(ionian, root='C')
print(c_maj_scale.describe())

cmaj_iterator = c_maj_scale.iterate_notes()

notes = [ next(cmaj_iterator) for _ in range(24) ]

synthesized = []
for i in range(7):
	voicing = build_voicing([
		notes[i],
		notes[i+2],
		notes[i+4]
	])
	synthesized.append(synthesize_voicing(voicing))


# a simple I - IV - V 
title = 'I-IV-V_in_Cmaj'
midi = init_midi(title)
I = synthesized[0]
print(I.describe())

IV = synthesized[3]
print(IV.describe())

V = synthesized[4]
print(V.describe())

add_voicing(midi, I, 0, 2)
add_voicing(midi, IV, 2, 2)
add_voicing(midi, V, 4, 2)

persist(midi, title)