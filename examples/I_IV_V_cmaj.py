from modes.store import (
	get as get_mode,
	get_scale_from_mode
)

from synth.store import (
	synthesize_voicing 
)
from synth.utils import (
	init_midi,
	add_voicing,
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
	chord_voicings.append(voicing)
	synthesized.append(synthesize_voicing(voicing))

I = synthesized[0]
IV = synthesized[3]
V = synthesized[4]

# otherwise, sounds annoying
inverted_I =  synthesize_voicing(
	invert(chord_voicings[0], inversion=2)
)

title = 'I-IV-V_cmaj'
m = init_midi(title=title)

duration = 2
t = add_voicing(m, I, 0, duration)
t = add_voicing(m, IV, t, duration)
t = add_voicing(m, V, t, duration)
t = add_voicing(m, inverted_I, t, duration)

persist(m, title)
