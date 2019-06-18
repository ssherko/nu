from chords.ops import build_voicing
from notes.store import get as get_note

o=2

C = get_note('C', octave=o)
Eb = get_note('D#',octave=o)
G = get_note('G',octave=o)

B = get_note('B',octave=o)
D = get_note('D',octave=o)

E = get_note('E',octave=o)
Fs = get_note('F#',octave=o)

gmaj = build_voicing([G, B, D])
bmaj = build_voicing([B, Eb, Fs])
cmaj = build_voicing([C, E, G])
cmin = build_voicing([C, Eb, G])

progression = [
	[gmaj] * 8,
	[bmaj] * 8,
	[cmaj] * 8,
	[cmin] * 8
] * 2

from synth.store import (
	synthesize_voicing 
)
from synth.utils import (
	init_midi,
	add_voicing,
	persist
)

title = 'creep'
m = init_midi(title=title)

synthesized_voicing = [
	synthesize_voicing(v) 
	for voicings in progression
	for v in voicings
]


duration = 1.70
t = 0
for synth_voicing in synthesized_voicing:
	t = add_voicing(m, synth_voicing, t, duration)

persist(m, title)

 