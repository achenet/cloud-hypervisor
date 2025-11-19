import logging
import os
import requests_unixsocket

def test_vm_start():
    logging.info("testing vm start")
    os.system('./target/debug/cloud-hypervisor --api-socket /tmp/cloud-hypervisor.sock &')

    logging.info("VMM started")

    session = requests_unixsocket.Session()
    url = 'http+unix://%2Ftmp%2Fcloud-hypervisor.sock/api/v1/vmm.ping'
    r = session.get(url)
    logging.info(f"response: {r.status_code} - {r.text}")
    assert r.status_code == 200

    os.system('killall cloud-hypervisor')
    logging.info("vmm shutdown")
