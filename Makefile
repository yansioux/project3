venv := virtual_env
dict_in := project3/dicts/project3_russian.dict
dict_out := dist/project3_russian.dict
start_script := dist/start.sh

all: clean prepare generate assembly info
.PHONY: all

clean:
	-rm -f -r dist
	-rm -f -r $(venv)
	
prepare:
	python3 -m venv $(venv)
	source $(venv)/bin/activate; \
	pip install -r requirements.txt;

generate:
	source $(venv)/bin/activate; \
	pyinstaller cli.py --name project3 --onefile --path $(venv)/lib/*/site-packages;

assembly:
	cp $(dict_in) $(dict_out)
	touch $(start_script)
	echo "#!/bin/sh\n./project3 `basename $(dict_out)`" > $(start_script)
	chmod 555 $(start_script)

info:
	@echo '\033[0;32mСборка завершена. В папке dist находится готовое к работе приложение.\033[0m'

