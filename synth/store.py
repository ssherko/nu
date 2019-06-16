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

class SynthesizedNote:
	def __init__(self, note):
		self.note = note
		self.midi_pitch = to_midi_pitch(note)

	def describe(self):
		return (
			"SynthesizedNote (note:{}, pitch: {})"
		).format(
			self.note.describe(), 
			self.midi_pitch
		)

	def __repr__(self):
		return ""

class SynthesizedScale:
	def __init__(self, scale):
		self.scale = scale
		self.midi_pitches = [
			to_midi_pitch(note)
			for note in self.scale.notes
		]

	def describe(self):
		return ""

	def __repr__(self):
		return ""


def synthesize_voicing(voicing):
	return SynthesizedVoicing(voicing)

def synthesize_scale(scale):
	return SynthesizedScale(scale)

def synthesize_note(note):
	return SynthesizedNote(note)
