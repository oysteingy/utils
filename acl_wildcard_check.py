#!/usr/bin/env python3
import ipaddress
import sys


#https://stackoverflow.com/questions/19944607/converting-a-cisco-wildcard-mask-to-list-of-ipnetworks-in-python

def main(address, mask):


    mask_int = int.from_bytes((ipaddress.IPv4Address(mask).packed), "big")
    address_int = int.from_bytes(ipaddress.IPv4Address(address).packed, "big")

    lower = ipaddress.IPv4Address((2 ** 32 - 1 - mask_int) & address_int)
    upper = ipaddress.IPv4Address(mask_int | address_int)

    return list(ipaddress.summarize_address_range(lower, upper))



if __name__ == '__main__':
    if (len(sys.argv) >= 3):
        networks = main(sys.argv[1], sys.argv[2])
        for net in networks:
            print("{0}".format(net))
            if (len(sys.argv) == 4):
                    if(ipaddress.ip_network(net).overlaps(ipaddress.ip_network(sys.argv[3]))):
                        print("match {0} {1}".format(net, sys.argv[3]))

    else:
        print("Incorrent arguments", file=sys.stderr)
        sys.exit(1)
