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

```
$ cd openstack-tests
$ sudo openstack-ci -c /etc/openstack-ci/profiles/landscape.yaml \
    -t regressions/00_test_service_deploy
```
