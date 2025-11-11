import logging
import socket
import os
import requests

def test_vm_start():
    logging.warning("testing vm start")
    os.system('./target/debug/cloud-hypervisor --api-socket /tmp/cloud-hypervisor.sock &')

    logging.warning("VMM started")

    url = 'http://localhost/api/v1/vmm.ping'
    r = requests.get(url)
    logging.warning("response", r)



# test_vm_start()
