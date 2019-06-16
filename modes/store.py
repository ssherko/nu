from modes.properties import get_all as get_all_properties
from intervals.store import get as get_interval
from notes.store import iterate_notes, get as get_note

class Mode:
	def __init__(self, t, name, props):
		self.type = t
		self.name = name
		self.tone_pattern = props.get('patterns', {}).get('tones')
		self.interval_pattern = props.get('patterns', {}).get('intervals')

	def describe(self):
		return (
			"Mode (type: {}, name: {}, intervals: {})"
		).format(
			self.type,
			self.name,
			"|".join([str(i) for i in self.interval_pattern])
		)

	def __repr__(self):
		return "Mode (type: {}, name: {})".format(self.type, self.name)


class Scale():
	def __init__(self, mode, root='C', octave=4):
		self.mode = mode
		self.notes = []

		# root is always there
		self.notes.append(get_note(root, octave=octave))
		
		for interval_name in self.mode.interval_pattern:
			note_iterator = iterate_notes(start=root, octave=4)
			interval = get_interval(interval_name)
			
			# advance iterator
			accum = [ next(note_iterator) for _ in range(interval.halfsteps) ]
			
			if not any(accum):
				continue

			self.notes.append(accum[-1])

	# TODO: wrong way to do it, to-be-fixed
	def iterate_notes(self):
		distinct = self.notes[:-1] # omit the octave
		c = 0
		while True:
			yield distinct[c % len(distinct)]
			c += 1

	def describe(self):
		return (
			"Scale ({}, notes:{})".format(
				self.mode,
				self.notes
			)
		)

__modes_store = {
	name: Mode(t, name, props)
	for t, name, props in get_all_properties()
}

def get(name):
	return __modes_store.get(name)

def get_type(t='diatonic'):
	# TODO
	return []

def get_scale_from_mode(mode, root):
	return Scale(mode, root=root)