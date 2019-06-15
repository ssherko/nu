TONE=2
SEMITONE=1

__mode_properties = {

	'diatonic': {

		'ionian': {
			'patterns': {
				# tone-semitone pattern for the mode
				'tones': [
					TONE, TONE, 
					SEMITONE, 
					TONE, TONE, TONE, 
					SEMITONE
				],
				# note intervals (from the root)
				'intervals': ['P1', 'M2', 'M3', 'P4', 'P5', 'M6', 'M7', 'P8']
			},
		},

	}

}

def get(name, key='diatonic'):
	return __mode_properties.get(key, {}).get(name)

def get_all():
	return [ 
		(t, name, props) 
		for t, modes in __mode_properties.items() 
		for name, props in modes.items() 
	]