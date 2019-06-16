from notes.store import (
	get as get_note,
	iterate_notes
)

def add_interval(n, i):
	note_iterator = iterate_notes(start=n.name, octave=n.octave)

	accum = [next(note_iterator) for _ in range(i.halfsteps)]
	

	if not any(accum):
		return n

	return accum[-1]

def flatten(n):
	note_iterator = iterate_notes(octave=0)
	prev = next(note_iterator)
	
	for curr in note_iterator:
		if curr.name == n.name and curr.octave == n.octave:
			return prev
		prev = curr

def sharpen(n):
	return next(iterate_notes(start=n.name, octave=n.octave))

