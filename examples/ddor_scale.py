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


ionian = get_mode('dorian')
cdorian = get_scale_from_mode(ionian, root='C')
print(cdorian.describe())

title = 'c_dorian_scale'
m = init_midi()

_ = add_scale(
	m, synthesize_scale(cdorian), spacing=1 
)

persist(m, title)
