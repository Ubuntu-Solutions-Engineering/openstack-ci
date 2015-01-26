openstack-ci
============

Automated testing


## Setup

Install `openstack` and `openstack-ci`.

```
$ sudo apt-add-repository ppa:cloud-installer/experimental
$ sudo apt-get update
$ sudo apt-get install openstack openstack-ci
```

Git clone the tests repository:

```
$ git clone https://github.com/Ubuntu-Solutions-Engineering/openstack-tests.git
```

## Running

A single test, with a test sitting in `quality/00_agents_started.py`

```
$ cd openstack-tests
$ sudo openstack-ci -t 00_agents_started
```

Running tests after performing a deploy

```
$ cd openstack-tests
$ JUJU_BOOTSTRAP_TO=authorized-seat.maas openstack-ci -c config.yaml --with-install
```

Depending on if the install passed/failed it will switch to the functional tests and
continue on.
