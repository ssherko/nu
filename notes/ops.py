from notes.store import iterate_notes

def add_interval(n, i):
	note_iterator = iterate_notes(start=n.name, octave=n.octave)

	accum = [next(note_iterator) for _ in range(i.halfsteps)]
	if not any(accum):
		return n

	return accum[-1]

# TODO: flatten and sharpen have issues with octaves
# irrelevant for now
def flatten(n):
	note_iterator = iterate_notes(octave=n.octave)
	prev = next(note_iterator)
	for curr in note_iterator:
		if curr.name == n.name:
			return prev
		prev = curr

def sharpen(n):
	return next(iterate_notes(start=n.name, octave=n.octave))