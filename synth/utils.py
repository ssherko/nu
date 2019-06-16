from pathlib import Path

from midiutil.MidiFile import MIDIFile

from synth.properties import output_path

def to_midi_pitch(note):
	return (note.octave * 12) + note.degree + 9# don't ask

def init_midi(title='sample'):
	midi = MIDIFile(1)
	midi.addTrackName(0, 0, title)
	midi.addTempo(0, 0, 120)

	return midi

def add_note(midi, pitch, time, duration):
	midi.addNote(0, 0, pitch, time, duration, 100)

def add_voicing(midi, synth_voicing, time, duration):
	for pitch in synth_voicing.midi_pitches:
		add_note(midi, pitch, time, duration)

def persist(midi, fname):
	full_output_path = str(
		output_path() / Path("{}.mid".format(fname))
	)

	with open(full_output_path, 'wb') as fout:
		midi.writeFile(fout)