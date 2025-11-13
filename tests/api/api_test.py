import logging
import os
import requests_unixsocket

def test_vm_start():
    logging.warning("testing vm start")
    os.system('cargo run -- --api-socket /tmp/cloud-hypervisor.sock &')

    logging.warning("VMM started")

    url = 'http+unix://tmp/cloud-hypervisor.sock/api/v1/vmm.ping'
    session = requests_unixsocket.Session()
    response = session.get(url)
    assert response.status_code == 200



