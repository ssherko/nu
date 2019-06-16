from mpmath import power

from notes.properties import (
	get, get_all,
	_interval_ratio,
	_reference_frequency,
	_reference_octave
)

from notes.pitch import Pitch

class Note:
	def __init__(self, properties, octave=4):
		self.name = properties.get('name')
		self.alternative = properties.get('alt')
		self.degree = properties.get('deg')
		self.rank = ( octave * 12 ) + self.degree

		self.octave = octave
		octave_offset = octave - _reference_octave()

		freq = (
			_reference_frequency() 
			* 
			power(_interval_ratio(), self.degree)
		)
		
		frequency_multiplier = power(2, octave_offset)
		frequency = freq * frequency_multiplier

		self.pitch = Pitch(
			float(frequency), # Otherwise sympy goes nuts
			_reference_frequency()
		)

	def describe(self):
		return (
			"Note(name: {}, alt: {}, octave: {}, degree: {}, {})"
		).format(
			self.name, 
			self.alternative if self.alternative else '-',
			self.octave,
			self.degree, 
			self.pitch.describe()
		)

	def __repr__(self):
		return 'Note({})'.format(self.name)

def __note_iterator(properties, octave=0):
	c = 0
	o = octave

	while True:
		name, info = properties[c % len(properties)]
		props = dict(name=name, **info)

		yield Note(props, octave=o)
		
		c += 1
		if c % len(properties) == 0:
			o += 1
		

def iterate_notes(start='A', octave=0):
	it = __note_iterator(get_all(), octave=octave)
	
	for note in it:
		if note.name != start:
			continue
		break

	for note in it:
		yield note

def get(name, octave=4):
	it = __note_iterator(get_all(), octave=octave)
	for note in it:
		if note.name == name:
			return note

def get_sequence(start, end, start_octave=4):
	it = __note_iterator(get_all(), octave=start_octave)
	sequence = []
	
	for note in it:
		# Skip until `start`
		if note.name == start:
			sequence.append(note)
			break

	for note in it:
		# Continue until `end`
		if note.name != end:
			sequence.append(note)
			continue
		break
	
	sequence.append(note)
	
	return sequence