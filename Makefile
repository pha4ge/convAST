.PHONY : docs
docs :
	rm -rf docs/build/
	sphinx-autobuild -b html --watch convast/ docs/source/ docs/build/

.PHONY : run-checks
run-checks :
	black --check .
	ruff check .
	pytest -v --color=yes --doctest-modules tests/ convast/

.PHONY : build
build :
	rm -rf *.egg-info/
	python -m build
