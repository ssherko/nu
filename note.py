from sympy import Rational
from mpmath import power

# TODO:
#from dataclasses import dataclass

from pitch import Pitch

def _interval_ratio():
	return power(2, Rational(1,12))

def _reference_frequency():
	return 440.0 #Hz, concert-tuning A4

def _reference_octave():
	return 4

__note_properties = list(enumerate([
	{
		'name': 'A',
		'alt': None, # alternative name
	},
	{
		'name': 'A#',
		'alt': 'Bb',
	},
	{
		'name': 'B',
		'alt': None,
	},
	{
		'name': 'C',
		'alt': None,
	},
	{
		'name': 'C#',
		'alt': 'Db',
	},
	{
		'name': 'D',
		'alt': None, 
	},
	{
		'name': 'D#',
		'alt': 'Eb',
	},
	{
		'name': 'E',
		'alt': None,
	},
	{
		'name': 'F',
		'alt': None,
	},
	{
		'name': 'F#',
		'alt': 'Gb',
	},
	{
		'name': 'G',
		'alt': None,
	},
	{
		'name': 'G#',
		'alt': 'Ab',
	}
]))

def _get_note_properties(note_name):
	def __with_name(e):
		is_actual_name = ( e[1].get('name') == note_name )
		is_alternative_name = ( e[1].get('alt') == note_name )
		return is_actual_name or is_alternative_name

	props = list(filter(__with_name, __note_properties))
	if any(props):
		degree, properties = props[0]
		return degree, properties

	return None, None

# TODO: make dataclass
class Note:
	def __init__(self, name, octave=4):
		degree, properties = _get_note_properties(name)

		self.name = properties.get('name')
		self.alternative = properties.get('alternative')
		self.degree = degree

		self.octave = octave
		octave_offset = octave - _reference_octave()

		freq = (
			_reference_frequency() 
			* 
			power(_interval_ratio(), degree)
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
			self.degree + 1, # should start from 1
			self.pitch.describe()
		)

	def __repr__(self):
		return 'Note({})'.format(self.name)


chromas = [
	Note(note_property.get('name'), octave=o)
	for o in range(3, 6) 
	for _, note_property in __note_properties
]