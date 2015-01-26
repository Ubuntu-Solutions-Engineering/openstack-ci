arch: null
config_file: null
current_state: 1
edit_placement: false
extra_ppa: null
headless: false
http_proxy: null
https_proxy: null
install_only: false
install_type: Multi
killcloud: false
killcloud_noprompt: false
maascreds:
  api_host: 172.16.0.1
  api_key: y55mPM2zBzE5wsR9CF:pk7PQ563tZ6AupgZ2y:vMk3qFLuANBJ8dZ6yqHnU8yuMF883HXW
openstack_password: pass
openstack_release: null
placements:
  /MAAS/api/1.0/nodes/node-216ddf60-a122-11e4-a192-a0cec8006f97/:
    assignments: {}
    constraints: {}
  /MAAS/api/1.0/nodes/node-24ac63e0-a122-11e4-b67e-a0cec8006f97/:
    assignments:
      KVM:
      - nova-compute
      - quantum-gateway
      LXC:
      - nova-cloud-controller
      - glance
      - glance-simplestreams-sync
      - openstack-dashboard
      - keystone
      - mysql
      - rabbitmq-server
    constraints: {}
  /MAAS/api/1.0/nodes/node-4ed9ee06-a124-11e4-9f8d-a0cec8006f97/:
    assignments: {}
    constraints: {}
  /MAAS/api/1.0/nodes/node-c8e1c7ce-a123-11e4-864e-a0cec8006f97/:
    assignments: {}
    constraints: {}
  /MAAS/api/1.0/nodes/node-caba30a2-a120-11e4-b67e-a0cec8006f97/:
    assignments: {}
    constraints: {}
  /MAAS/api/1.0/nodes/node-cac127c2-a120-11e4-a192-a0cec8006f97/:
    assignments: {}
    constraints: {}
release: null
uninstall: false
upstream_deb: null
