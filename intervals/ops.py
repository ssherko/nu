from intervals.store import get

# TODO: need to look a bit closer into these

def interval_between(n1, n2):
	# don't really care about octaves
	root, other = sorted([n1, n2], key=lambda e: e.degree)
	halfsteps = other.degree - root.degree
	return get(halfsteps, key='halfsteps') 


def augment_interval(i):
	hf = i.halfsteps + 1
	aug = get(hf, key='halfsteps')
	
	if aug.name == 'perfect unison': # was an octave, should skip P1
		return get(hf + 1, key='halfsteps')

	return get(hf, key='halfsteps')

def diminish_interval(i):
	hf = i.halfsteps - 1
	dim = get(hf, key='halfsteps')

	if dim.name == 'perfect octave': # was an unison, should skip P8
		return get(hf - 1, key='halfsteps')

	return get(hf, key='halfsteps')
