from collections import OrderedDict

from intervals.properties import get, get_all

class Interval:
	def __init__(self, hf, props):
		self.name = props.get('name')
		self.min_maj = props.get('min-maj')
		self.alt = props.get('alt')
		self.aug_dim = props.get('aug-dim')

		self.halfsteps = hf

	def describe(self):
		return "Interval({}, {}, halfsteps: {})".format(
			self.name, self.min_maj, self.halfsteps
		)
	def __repr__(self):
		return "Interval({})".format(self.min_maj)


__intervals = [
	Interval(hf, props) for hf, props in enumerate(get_all())
]

from collections import OrderedDict
__store = {
	'name': OrderedDict(
		[
			(i.name, i)
			for i in __intervals
		]
	),
	'alt': OrderedDict(
		[
			(i.alt, i)
			for i in __intervals
		]
	),
	'min-maj': OrderedDict(
		[
			(i.min_maj, i)
			for i in __intervals
		]
	),
	'aug-dim': OrderedDict(
		[
			(i.aug_dim, i)
			for i in __intervals
		]
	),
	'halfsteps': [
		i for i in __intervals
	]
}

def get(value, key='min-maj'):
	if key == 'halfsteps':
		return __store.get('halfsteps')[value]

	return __store.get(key, {}).get(value)

def get_all():
	intervals_by_name = __store.get('name')
	return [
		interval
		for _, interval in intervals_by_name.items()
	]
