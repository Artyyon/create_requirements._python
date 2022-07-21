create:
	pip list > saida.txt
	python3 create_requeriments.py saida.txt
	rm saida.txt
	