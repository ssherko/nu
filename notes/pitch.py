from math import log
from sympy import Rational

_log2 = lambda v: log(v, 2)

class Pitch:
	def __init__(self, frequency, reference_frequency):
		self.frequency = frequency
		self.reference_frequency = reference_frequency
	
	def ratio(self):
		return float(Rational(
			self.frequency, 
			self.reference_frequency
		).simplify())

	def octave(self):
		return _log2(
			self.ratio()
		)

	def halfsteps(self):
		return 12 * self.octave()

	def describe(self):
		return (
			"Pitch(f: {:.2f} Hz, +/-octave: {:.2f}, ratio: {:.2f}, +/-halfsteps: {:.2f}, (ref: {:.2f} Hz))"
		).format(
			self.frequency,
			self.octave(),
			self.ratio(),
			self.halfsteps(),
			self.reference_frequency
		)

	def __repr__(self):
		return '{:.2f} Hz'.format(self.frequency)