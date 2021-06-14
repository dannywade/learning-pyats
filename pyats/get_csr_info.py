# loader our newly minted testbed file
from pyats.topology import loader
from pprint import pprint

# Load the testbed file
tb = loader.load("testbed.yaml")

# Assign the CSR device to a variable
csr = tb.devices["csr1000v-1"]

# Connect to the CSR device
csr.connect()

# Issue 'show version' command and print the output
pprint(csr.parse("show version"))

# Disconnect from the CSR device
csr.disconnect()
