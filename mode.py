from note import chromas
from interval import intervals

__mode_properties = {
	'diatonic': [
		{
			'name': 'ionian',
			'pattern': 'W-W-H-W-W-W-H'
		}
	]
}

def _pattern_to_intervals(pattern):
	steps = pattern.split('-')
	hf = 0
	i = [intervals[0]]
	for step in steps:
		if step == 'W':
			hf += 2 
		if step == 'H':
			hf += 1

		i.append(intervals[hf])

	return i

class Mode:
	def __init__(self, t, props):
		self.type = t
		self.name = props.get('name') 
		self.intervals = _pattern_to_intervals(props.get('pattern'))

	def with_root(root):
		pass

	def describe(self):
		return (
			"Mode(type: {}, name: {}, intervals: {})"
		).format(
			self.type,
			self.name,
			"|".join([str(i) for i in self.intervals])
		)

	def __repr__(self):
		pass

modes = [
	Mode(t, m)
	for t, l in __mode_properties.items()
	for m in l
	
]