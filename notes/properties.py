from collections import OrderedDict

from sympy import Rational
from mpmath import power


def _interval_ratio():
	return power(2, Rational(1,12))

def _reference_frequency():
	return 440.0 #Hz, concert-tuning A4

def _reference_octave():
	return 4


__note_properties = OrderedDict([
	('A', {'alt': None, 'deg': 0}),
	('A#', {'alt': 'Bb', 'deg': 1}),
	('B', {'alt': None, 'deg': 2}),
	('C', {'alt': None, 'deg': 3}),
	('C#', {'alt': 'Db', 'deg': 4}),
	('D', {'alt': None, 'deg': 5}),
	('D#', {'alt': 'Eb', 'deg': 6}),
	('E', {'alt': None, 'deg': 7}),
	('F', {'alt': None, 'deg': 8}),
	('F#', {'alt': 'Gb', 'deg': 9}),
	('G', {'alt': None, 'deg': 10}),
	('G#', {'alt': 'Ab', 'deg': 11})
])

def get(name):
	return __note_properties.get(name)

def get_all():
	return list(__note_properties.items())
