
.PHONY:
run:
	@`which python` main.py

.PHONY:
example:
	@PYTHONPATH=. `which python` examples/interval.py
