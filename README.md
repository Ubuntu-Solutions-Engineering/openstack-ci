openstack-installer-ci
======================

Automated testing


## Setup

Clone this repository and run the following within that directory.


```
$ sudo apt-add-repository ppa:cloud-installer/testing
$ sudo apt-get install openstack
$ pip install pytest
$ py.test single/
```

## TODO

* Add multi tests
* Add landscape deploy tests
