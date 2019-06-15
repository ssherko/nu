from notes.store import iterate_notes

def add_interval(n, i):
	note_iterator = iterate_notes(start=n.name)

	accum = [next(note_iterator) for _ in range(i.halfsteps)]
	if not any(accum):
		return n

	return accum[-1]