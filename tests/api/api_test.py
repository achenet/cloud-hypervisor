import logging
import os
import requests_unixsocket

def test_vm_start():
    logging.warning("testing vm start")
    os.system('./target/debug/cloud-hypervisor --api-socket /tmp/cloud-hypervisor.sock &')

    logging.warning("VMM started")

    session = requests_unixsocket.Session()
    url = 'http+unix://%2Ftmp%2Fcloud-hypervisor.sock/api/v1/vmm.ping'
    r = session.get(url)
    logging.warning(f"response: {r.status_code} - {r.text}")

