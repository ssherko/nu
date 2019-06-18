
.PHONY:
run:
	@`which python` main.py

.PHONY:
example:
	@PYTHONPATH=. `which python` examples/interval.py
	@PYTHONPATH=. `which python` examples/c_maj_scale.py
	@PYTHONPATH=. `which python` examples/cmaj_chord_inversions.py
	@PYTHONPATH=. `which python` examples/mixed.py
	@PYTHONPATH=. `which python` examples/I_IV_V_cmaj.py
	@PYTHONPATH=. `which python` examples/7th_extensions.py
	@PYTHONPATH=. `which python` examples/creep.py