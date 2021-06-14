# loader our newly minted testbed file
from pyats.topology import loader
from pprint import pprint
from genie.utils import Dq

# Load the testbed file
tb = loader.load("testbed.yaml")

# Assign the CSR device to a variable
csr = tb.devices["csr1000v-1"]

# Connect to the CSR device
csr.connect()

# Issue 'show version' command and parse the output
parsed_output = csr.parse("show version")
# Store the standard IOS version in a variable for future use
# Change to "16.09.03" if you want to see the IOS check pass
standard_os = "16.12.05"
# Look for the 'xe_version' key and see if it contains the standard IOS version
ios_check = Dq(parsed_output).contains(standard_os).get_values("xe_version")
# An empty list should print if there isn't a match
print(ios_check)
# Checks to see if the returned list is populated - If so, there is a match
if ios_check:
    print("IOS Check passed!")
else:
    print("IOS Check failed!")

# Disconnect from the CSR device
csr.disconnect()
