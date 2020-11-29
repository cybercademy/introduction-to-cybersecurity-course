#!/usr/bin/env python3

# Functionality: Script which scans networks via ARP request and response.
#                IP address is supplied by user and returns
#                MAC and IP address if host device is found.

import argparse
import scapy.all as scapy

# Define and print functionality of program.
print("Description: Network scanner used to scan network for supplied IP addresses. Returns IP address and MAC address.")
print("Usage: python3 network_scanner.py [-t] ip")
print("[-t]: Scan for specified IP addresses")

# Define arguments through argparse. 
def cmd_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--target', dest="target", 
            help="Target IP Address")
    args = parser.parse_args()

    if not args.target:
        parser.error("Specify an IP Address or List of IP Addresses.")

    return args
# Create and scan network with scpecified IP address supplied by user.
def scan(ip):
    answered = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst=ip               ), timeout=2)[0]

    results = []
    for i in range(0, len(answered)):
        client = {"ip": answered[i][1].psrc, "mac": answered[i][1].hwsrc}
        results.append(client)
    
    return results

# Print scan results to screen with IP and MAC Address.
def results(result):
    print("IP Address\tMAC Address")
    for i in result:
        print("{}\t{}".format(i["ip"], i["mac"]))



args = cmd_arguments()
scan_output = scan(args.target)
results(scan_output)
