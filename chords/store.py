from chords.properties import get, get_all
from intervals.store import get as get_interval
from notes.store import iterate_notes, get as get_note

def _get_interval(name):
	return (
		get_interval(name, key='min-maj') 
		or 
		get_interval(name, key='aug-dim')
	)


class Chord:
	def __init__(self, t, kind, props):
		self.type = t
		self.kind = kind

		intervals = props.get('intervals')
		self.intervals = [
			_get_interval(name) for name in intervals
		]

	def describe(self):
		return (
			"Chord (type: {}, kind: {}, intervals: {})"
		).format(
			self.type,
			self.kind,
			'|'.join([i.describe() for i in self.intervals])
		)

	def __repr__(self):
		return "Chord (type: {}, kind: {}, intervals: {})".format(
			self.type,
			self.kind,
			self.intervals
		)


class Voicing:
	def __init__(self, chord, root='C'):
		self.chord = chord
		self.root = root
		notes = iterate_notes(start=root)

		self.notes = []

		# root is always there
		self.notes.append(get_note(root))
		
		for interval in self.chord.intervals:
			note_iterator = iterate_notes(start=root)
			
			# advance iterator
			accum = [ next(note_iterator) for _ in range(interval.halfsteps) ]
			
			if not any(accum):
				continue

			self.notes.append(accum[-1])



	def describe(self):
		return (
			"Voicing (chord: {}, root: {}, notes: {})"
		).format(
			self.chord,
			self.root,
			'|'.join([ n.describe() for n in self.notes ])
		)

	def __repr__(self):
		return "Voicing (chord: {}, notes: {})".format(
			self.chord.kind,
			self.notes
		)

__chords_store = {
	'triads': {
		kind: Chord('triad', kind, props)
		for kind, props in get_all(t='triads').items()
	}
}


def get(kind, t='triads'):
	return __chords_store.get(t, {}).get(kind)


def get_voicing(chord, root='C'):
	return Voicing(chord, root=root)