from synth.store import (
	synthesize_note 
)
from synth.utils import (
	init_midi,
	add_note,
	persist
)

from intervals.store import get_all

from notes.store import (
	get as get_note
)
from notes.ops import add_interval

reference = get_note('C', octave=4)
inters = get_all()

tuples = [
	(reference, add_interval(reference, i))
	for i in inters
]

synthesized = [
	(synthesize_note(reference), synthesize_note(note))
	for reference, note in tuples
]

title = 'intervals'
m = init_midi(title=title)
t = 0
d = 2
for ref, note in synthesized:
	add_note(m, ref, t, d)
	add_note(m, note, t, d)
	t += d

persist(m, title)
