# loader our newly minted testbed file
from pyats.topology import loader
from pprint import pprint

# Load the testbed file
tb = loader.load("testbed.yaml")

# Assign the CSR device to a variable
csr = tb.devices["csr1000v-1"]

# Connect to the CSR device
csr.connect()

# Learn platform features using Genie models
csr.learn("platform")

# Disconnect from the CSR device
csr.disconnect()
