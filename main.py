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
from notes.ops import add_interval, sharpen, flatten

reference = get_note('G#', octave=4)

print('Reference:')
print(reference.describe())

print('Sharpened:')
print(sharpen(reference).describe())
