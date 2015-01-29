NAME
====

openstack-ci - Ubuntu OpenStack Installer deployment testing

SYNOPSIS
========

usage: openstack-ci [-h] [-c CONFIG_FILE] [-t TEST_NAME] [-a] [-d TEST_DIR]
                    [--with-install]

Ubuntu OpenStack Installer CI

optional arguments:

.. code::

      -h, --help            show this help message and exit
      -c CONFIG_FILE, --config CONFIG_FILE
                            Profile to apply during CI.
      -t TEST_NAME, --test TEST_NAME
                            Test to run.
      -a, --all             Run all quality/regression tests.
      -d TEST_DIR, --tests-directory TEST_DIR
                            Top level Location of quality/regression tests
      --with-install        Perform a full install and deploy before running tests

DESCRIPTION
===========

Ubuntu OpenStack Installer deployment testing provides a simple way to
test Single, Multi, and Landscape OpenStack Autopilot deployments.

ENVIRONMENT VARIABLES
=====================

**JUJU_BOOTSTRAP_TO**
define a specific MAAS host to be used for the initial juju bootstrap.

.. code::

   $ JUJU_BOOTSTRAP_TO=machine-a.maas openstack-ci -c config-multi.yaml -a --with-install

