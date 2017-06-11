#!/usr/bin/env python3

import ipaddress
import sys


def convert():
    #get netmask from ip_network object
    try:
        netmask = ipaddress.IPv4Network(sys.argv[1]).netmask
    except ValueError as err:
        print("Incorrect IPv4 addr {}".format(err))
        sys.exit(1)
    #reuse netmask object as IPv4Address 
    netmask = int(ipaddress.IPv4Address(netmask))
    #wildcard = netmask XOR 255.255.255.255
    wildcard = netmask ^ int(ipaddress.IPv4Address('255.255.255.255'))
    #return wildcard and ip network 
    return (str(ipaddress.IPv4Network(sys.argv[1]).network_address), str(ipaddress.IPv4Address(wildcard)))

def main():
    if (len(sys.argv) != 2):
        print("{} network/mask ".format(sys.argv[0]))
        sys.exit(1)
    net_and_wc = (convert())
    print("permit {} {} any".format(net_and_wc[0], net_and_wc[1]))

if __name__ == '__main__':
    main()

