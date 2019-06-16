from pathlib import Path

from midiutil.MidiFile import MIDIFile

from synth.properties import output_path

def to_midi_pitch(note):
	return (note.octave * 12) + note.degree + 9 # don't ask

def init_midi(title='sample'):
	midi = MIDIFile(1)
	midi.addTrackName(0, 0, title)
	midi.addTempo(0, 0, 120)

	return midi

def add_note(midi, synth_note, time, duration):
	midi.addNote(0, 0, synth_note.midi_pitch, time, duration, 100)
	return time

def add_voicing(midi, synth_voicing, time, duration):
	for pitch in synth_voicing.midi_pitches:
		midi.addNote(0, 0, pitch, time, duration, 100)
	return time + duration

def add_scale(midi, synth_scale, t=0, spacing=2):
	time = t
	for pitch in synth_scale.midi_pitches:
		midi.addNote(0, 0, pitch, time, spacing, 100)
		time += spacing
	return time

def persist(midi, fname):
	full_output_path = str(
		output_path() / Path("{}.mid".format(fname))
	)

	with open(full_output_path, 'wb') as fout:
		midi.writeFile(fout)