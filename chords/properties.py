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
			'intervals': ['perfect unison', 'major third', 'minor sixth']
		}
	},
	'four-note': {
		'half-diminished': {
			'intervals': ['perfect unison', 'minor third', 'tritone', 'minor seventh'],
		},
		'dominant': {
			'intervals': ['perfect unison', 'major third', 'perfect fifth', 'minor seventh'],
		},
	}
}


def get(key, t='triads'):
	return __chord_properties.get(t,{}).get(key)

def get_all(t='triads'):
	return __chord_properties.get(t, {})