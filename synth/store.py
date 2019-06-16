from synth.utils import to_midi_pitch


class SynthesizedVoicing:
	def __init__(self, voicing):
		self.voicing = voicing
		
		self.midi_pitches = [
			to_midi_pitch(note)
			for note in self.voicing.notes
		]

	def describe(self):
		return (
			"SynthesizedVoicing (voicing: {}, pitches: {})"
		).format(
			self.voicing.describe(),
			self.midi_pitches
		)

	def __repr__(self):
		return "SynthesizedVoicing (pitches: {})".format(self.midi_pitches)

def synthesize_voicing(voicing):
	return SynthesizedVoicing(voicing)
