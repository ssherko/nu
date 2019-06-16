from synth.store import (
	synthesize_voicing 
)
from synth.utils import (
	init_midi,
	add_voicing,
	persist
)

from chords.store import (
	get as get_chord,
	get_voicing
)
from chords.ops import invert

major_triad = get_chord('major')
cmaj = get_voicing(major_triad, root='C')

inversions = [
	invert(cmaj, inversion=i)
	for i in range(1, 4) # invert to 4, to make it sound nicer
]

print(cmaj)
for inversion in inversions:
	print(inversion)

synthesized_voicing = [
	synthesize_voicing(cmaj),
	*[
		synthesize_voicing(v)
		for v in inversions
	]
]

title = 'cmaj_inversions'
m = init_midi(title=title)

duration = 2
t = 0
for synth_voicing in synthesized_voicing:
	t = add_voicing(m, synth_voicing, t, duration)

persist(m, title)

