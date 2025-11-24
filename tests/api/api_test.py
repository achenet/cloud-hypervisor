import logging
import time
import os
import requests_unixsocket

def test_vmm_ping():
    logging.info("testing vmm ping")

    logging.info("clean up existing socket file, shutdown any running instances of cloud-hypervisor")
    if os.path.exists("/tmp/cloud-hypervisor.sock"):
        os.remove("/tmp/cloud-hypervisor.sock")

    os.system("killall cloud-hypervisor")

    logging.info("starting Cloud Hypervisor")
    os.system("./target/debug/cloud-hypervisor --api-socket /tmp/cloud-hypervisor.sock &")

    max_wait = 30 # in seconds
    waited = 0
    while not os.path.exists("/tmp/cloud-hypervisor.sock") and waited < max_wait:
        time.sleep(0.1)
        waited += 0.1
        logging.info("waiting for creation of socket file")
    assert os.path.exists("/tmp/cloud-hypervisor.sock")

    logging.info("VMM started")


    session = requests_unixsocket.Session()
    url = 'http+unix://%2Ftmp%2Fcloud-hypervisor.sock/api/v1/vmm.ping'
    r = session.get(url)
    logging.info(f"response: {r.status_code} - {r.text}")
    assert r.status_code == 200

    os.system('killall cloud-hypervisor')
    logging.info("vmm shutdown")


