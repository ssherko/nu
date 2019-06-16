from modes.store import (
	get as get_mode,
	get_scale_from_mode
)

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

from chords.ops import build_voicing, invert

ionian = get_mode('ionian')
cmaj_scale = get_scale_from_mode(ionian, root='C')
print(cmaj_scale.describe())

cmaj_iterator = cmaj_scale.iterate_notes()
notes = [ next(cmaj_iterator) for _ in range(24) ]

chord_voicings = []
synthesized = []
for i in range(7):
	voicing = build_voicing([
		notes[i],
		notes[i+2],
		notes[i+4]
	])
	print(voicing)
	chord_voicings.append(voicing)
	synthesized.append(synthesize_voicing(voicing))

synthesized_cmaj_scale = synthesize_scale(cmaj_scale)

I = synthesized[0]
IV = synthesized[3]
V = synthesized[4]

# otherwise, sounds annoying
inverted_I =  synthesize_voicing(
	invert(chord_voicings[0], inversion=2)
)

title = 'mixed'

m = init_midi(title=title)
t = 0
d = 1
t = add_scale(m, synthesized_cmaj_scale, t=t)
t = add_voicing(m, I, t, d)
t = add_voicing(m, IV, t, d)
t = add_voicing(m, V, t, d)
_ = add_voicing(m, inverted_I, t, d)

persist(m, title)