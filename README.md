openstack-installer-ci
======================

Automated testing


## Setup

Clone this repository and run the following within that directory.


```
$ sudo apt-add-repository ppa:cloud-installer/experimental
$ git clone https://github.com/Ubuntu-Solutions-Engineering/openstack-installer.git ~/openstack-installer
$ cd ~/openstack-installer
$ make install-dependencies
$ make deb
$ sudo dpkg -i ../openstack_*.deb
$ pip install pytest
$ git clone https://github.com/Ubuntu-Solutions-Engineering/openstack-installer-ci.git
$ cd openstack-installer-ci
$ ./runtests.sh
```

## TODO

* Add multi tests
* Add landscape deploy tests
