from intervals.store import (
	get as get_interval, 
	get_all as get_all_intervals
)

from intervals.ops import interval_between

from chords.store import Chord, Voicing
from chords.properties import get_all as get_all_properties

def __identify_kind(t, intervals):
	# Note: ignore 't' for now
	i_names = set([ i.name for i in intervals ])
	for kind, interval_info in get_all_properties().items():
		target_interval_names = set(interval_info.get('intervals'))
		if not any(i_names - target_interval_names):
			return kind

	return '?'

def build_voicing(notes, sort=False):
	 n = notes

	 if sort:
	 	n = sorted(notes, key=lambda e: e.rank)
	 
	 root = n[0]
	 
	 intervals = [
	 	interval_between(root, note, sort=sort) for note in n
	 ]
	 
	 t = 'single'
	 if len(intervals) == 2: 
	 	t = 'harmonic'
	 if len(intervals) == 3:
	 	t = 'triad'
	 if len(intervals) == 4:
	 	t = 'four-note'
	 if len(intervals) > 4:
	 	t = 'extended'

	 kind = __identify_kind(t, intervals)

	 chord = Chord(t, kind, {'intervals': [i.name for i in intervals]})
	 return Voicing(chord, root=root.name)

def invert(voicing, inversion=1):
	pass

def extend(chord, extensions):
	pass
