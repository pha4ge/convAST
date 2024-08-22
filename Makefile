.PHONY : check 
check :
	black convast
	ruff check convast
	pytest -v --color=yes tests/ 

.PHONY : build
build :
	rm -rf *.egg-info/
	python -m build
