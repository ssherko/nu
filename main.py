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
from chords.ops import build_voicing, invert

from synth.store import (
	synthesize_voicing,
	synthesize_scale
)
from synth.utils import (
	init_midi,
	add_voicing,
	add_scale,
	persist
)

ionian = get_mode('ionian')
c_maj_scale = get_scale_from_mode(ionian, root='C')
print(c_maj_scale.describe())

cmaj_iterator = c_maj_scale.iterate_notes()

notes = [ next(cmaj_iterator) for _ in range(24) ]

synthesized = []
voicings = []
for i in range(7):
	voicing = build_voicing([
		notes[i],
		notes[i+2],
		notes[i+4]
	])
	voicings.append(voicing)
	synthesized.append(synthesize_voicing(voicing))


c_maj_chord = voicings[0]
inverted_cmaj = invert(c_maj_chord, inversion=1)

cmaj_inversions_synth = [
	synthesize_voicing(invert(c_maj_chord, inversion=i))
	for i in range(3)
]

cmaj_synth = synthesize_scale(c_maj_scale)

# print(c_maj_chord)
# print(inverted_cmaj)


# a simple I - IV - V 
title = 'cmaj_scale'
midi = init_midi(title)
t = add_scale(midi, cmaj_synth, spacing=1)
t = add_voicing(midi, synthesized[3], t, 2)
t = add_voicing(midi, synthesized[4], t, 2)
t = add_voicing(midi, cmaj_inversions_synth[-1], t, 2)
t = add_voicing(midi, synthesized[0], t, 2)

# add_voicing(midi, I, 0, 2)
# add_voicing(midi, IV, 2, 2)
# add_voicing(midi, V, 4, 2)

persist(midi, title)