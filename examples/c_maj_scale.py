from modes.store import (
	get as get_mode,
	get_scale_from_mode
)

from synth.store import (
	synthesize_scale 
)
from synth.utils import (
	init_midi,
	add_scale,
	persist
)


ionian = get_mode('ionian')
c_maj_scale = get_scale_from_mode(ionian, root='C')
print(c_maj_scale.describe())

title = 'cmaj_scale'
m = init_midi()

_ = add_scale(
	m, synthesize_scale(c_maj_scale)
)

persist(m, title)
