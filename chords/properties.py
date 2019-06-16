__chord_properties = {
	'triads': {
		'major': {
			'intervals': ['perfect unison', 'major third', 'perfect fifth'],
			# P1, M3, P5

		},
		'minor': {
			'intervals': ['perfect unison', 'minor third', 'perfect fifth'],
			# P1, m3, P5
		},
		'diminished': {
			'intervals': ['perfect unison', 'minor third', 'tritone'],
			# P1, m3, d5
		},
		'augmented': {
			'intervals': ['perfect unison', 'major third', 'minor sixth'],
			# P1, M3, m6
		},
		'sus2': {
			'intervals': ['perfect unison', 'major second', 'perfect fifth'],
			# P1, M2, P5
		},
		'sus4': {
			'intervals': ['perfect unison', 'perfect fourth', 'perfect fifth'],
			# P1, P4, P5
		}
	},
	'four-note': {
		'half-diminished': {
			'intervals': ['perfect unison', 'minor third', 'tritone', 'minor seventh'],
		},
		'dominant': {
			'intervals': ['perfect unison', 'major third', 'perfect fifth', 'minor seventh'],
		},
		'major seventh': {
			'intervals': ['perfect unison', 'major third', 'perfect fifth', '']
		},
		'minor seventh': {
			'intervals': ['perfect unison', 'minor third', 'perfect fifth', '']
		}
	}
}

def get(key, t='triads'):
	return __chord_properties.get(t,{}).get(key)

def get_all(t='triads'):
	return __chord_properties.get(t, {})