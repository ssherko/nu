__interval_properties = [
	{
		'name': 'perfect unison',
		'min-maj': 'P1',
		'alt': 'diminished second',
		'aug-dim': 'd2'
	},
	{
		'name': 'minor second',
		'min-maj': 'm2',
		'alt': 'augmented unison',
		'aug-dim': 'A1'
	},
	{
		'name': 'major second',
		'min-maj': 'M2',
		'alt': 'diminished third',
		'aug-dim': 'd3'
	},
	{
		'name': 'minor third',
		'min-maj': 'm3',
		'alt': 'augmented second',
		'aug-dim': 'A2'
	},
	{
		'name': 'major third',
		'min-maj': 'M3',
		'alt': 'diminished fourth',
		'aug-dim': 'd4'
	},
	{
		'name': 'perfect fourth',
		'min-maj': 'P4',
		'alt': 'augmented third',
		'aug-dim': 'A3'
	},
	# why can't you be normal? -------
	{
		'name': 'Tritone',
		'min-maj': '-',
		'alt': 'augmented fourth | diminished fifth',
		'aug-dim': 'A4 | d5'
	},
	# --------------------------------
	{
		'name': 'perfect fifth',
		'min-maj': 'P5',
		'alt': 'diminished sixth',
		'aug-dim': 'd6'
	},
	{
		'name': 'minor sixth',
		'min-maj': 'm6',
		'alt': 'augmented fifth',
		'aug-dim': 'A5'
	},
	{
		'name': 'major sixth',
		'min-maj': 'M6',
		'alt': 'diminished seventh',
		'aug-dim': 'd7'
	},
	{
		'name': 'minor seventh',
		'min-maj': 'm7',
		'alt': 'augmented sixth',
		'aug-dim': 'A6'
	},
	{
		'name': 'major seventh',
		'min-maj': 'M7',
		'alt': 'diminished octave',
		'aug-dim': 'd8'
	},
	{
		'name': 'perfect octave',
		'min-maj': 'P8',
		'alt': 'augmented seventh',
		'aug-dim': 'A7'
	}
]

class Interval:
	def __init__(self, hf, props):
		
		self.name = props.get('name')
		self.min_maj = props.get('min-maj')
		self.halfsteps = hf

	def describe(self):
		return "Interval({}, {}, halfsteps: {})".format(
			self.name, self.min_maj, self.halfsteps
		)
	def __repr__(self):
		return "Interval({})".format(self.min_maj)


intervals = [
	Interval(hf, props)
	for hf, props in enumerate(__interval_properties)
]