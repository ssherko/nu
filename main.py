from interval import intervals
from mode import modes 

print('-' * 20)
print('Intervals')
print('-' * 20)
for i in intervals:
	print(i.describe())


print('-' * 20)
print('Modes')
print('-' * 20)
for m in modes:
	print(m.describe())
