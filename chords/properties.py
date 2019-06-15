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
			'intervals': ['perfect unison', 'minor third', 'diminished fifth'],
			# P1, m3, d5
		}
	}
}


def get(key, t='triads'):
	return __chord_properties.get(t,{}).get(key)

def get_all(t='triads'):
	return __chord_properties.get(t, {})