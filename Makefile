#
# Makefile for openstack-ci
#
NAME        = openstack-ci
TOPDIR      := $(shell basename `pwd`)
GIT_REV     := $(shell git log --oneline -n1| cut -d" " -f1)
VERSION     := $(shell ./tools/version)

$(NAME)_$(VERSION).orig.tar.gz: clean
	cd .. && tar czf $(NAME)_$(VERSION).orig.tar.gz $(TOPDIR) --exclude-vcs --exclude=debian

tarball: $(NAME)_$(VERSION).orig.tar.gz

.PHONY: install-dependencies
install-dependencies:
	sudo apt-get -yy install devscripts equivs pandoc
	sudo mk-build-deps -i -t "apt-get --no-install-recommends -y" debian/control

.PHONY: uninstall-dependencies
uninstall-dependencies:
	sudo apt-get remove openstack-ci-build-deps

clean:
	@debian/rules clean
	@rm -rf debian/cloud-install
	@rm -rf docs/_build/*
	@rm -rf ../openstack-ci_*.deb ../openstack-ci_*.tar.gz ../openstack-ci_*.dsc ../openstack-ci_*.changes \
		../openstack-ci_*.build

man-pages:
	@pandoc -s docs/openstack-ci.rst -t man -o man/en/openstack-ci.1
	@pandoc -s docs/openstack-ci-web.rst -t man -o man/en/openstack-ci-web.1

DPKGBUILDARGS = -us -uc -i'.git.*|.tox|.bzr.*|.editorconfig|.travis-yaml'
deb-src: clean update_version tarball
	@dpkg-buildpackage -S $(DPKGBUILDARGS)

deb: clean update_version man-pages tarball
	@dpkg-buildpackage -b $(DPKGBUILDARGS)

current_version:
	@echo $(VERSION)

git_rev:
	@echo $(GIT_REV)

update_version:
	wrap-and-sort
	@sed -i -r "s/(^__version__\s=\s)(.*)/\1\"$(VERSION)\"/" openstackci/__init__.py

.PHONY: ci-test pyflakes pep8 test travis-test
ci-test: pyflakes pep8 travis-test

pyflakes:
	python3 `which pyflakes` openstackci test

pep8:
	pep8 openstackci test

NOSE_ARGS = -v --with-cover --cover-package=cloudinstall --cover-html test --cover-inclusive cloudinstall
test:
	nosetests3 $(NOSE_ARGS)

all: deb
