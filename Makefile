GIT_REMOTE_URL = $(shell git config --get remote.origin.url)
GIT_PIP_FETCH_URL ?= git://$(subst :,/,$(GIT_REMOTE_URL:git@%=%))\#egg=ENML2HTML
VENV_NAME = .venv

test_local_pip_venv: test_pipvenv_bootstrap test_pipvenv_install_local test_pipvenv_check
	
test_git_pip_venv: test_pipvenv_bootstrap test_pipvenv_install_git_latest test_pipvenv_check

test_pipvenv_bootstrap:
	rm -rf $(VENV_NAME)
	virtualenv $(VENV_NAME)
	. $(VENV_NAME)/bin/activate ; pip install 'beautifulsoup4>=4.3.2'

test_pipvenv_check:
	. $(VENV_NAME)/bin/activate ; \
	(cd /tmp ; \
	echo 'from ENML_PY import ENMLToHTML ; print "ENML_PY module imported!"' | python)
	$(RM) -r $(VENV_NAME)

test_pipvenv_install_local:
	. $(VENV_NAME)/bin/activate ; pip install -v -v -v -e .

test_pipvenv_install_git_latest:
	. $(VENV_NAME)/bin/activate ; pip install -v -v -v -e $(GIT_PIP_FETCH_URL)
