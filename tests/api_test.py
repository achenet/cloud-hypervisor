import logging
import socket
import os

def test_vm_start():
    logging.warning("testing vm start")
    # how to make this call not blocking?
    os.system('../target/debug/cloud-hypervisor --unix-socket /tmp/cloud-hypervisor.sock')



