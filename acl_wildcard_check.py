#!/usr/bin/env python3
import ipaddress
import sys


#https://stackoverflow.com/questions/19944607/converting-a-cisco-wildcard-mask-to-list-of-ipnetworks-in-python

def main(address, mask):

    lower = ipaddress.IPv4Address((((2**32) - 1) - int(ipaddress.IPv4Address(mask)))  & int(ipaddress.IPv4Address(address)))
    upper = ipaddress.IPv4Address(int(ipaddress.IPv4Address(mask)) | int(ipaddress.IPv4Address(address))) 

    return list(ipaddress.summarize_address_range(lower, upper))



if __name__ == '__main__':
    if (len(sys.argv) >= 3):
        networks = main(sys.argv[1], sys.argv[2])
        for net in networks:
            print("{0}".format(net))
            if (len(sys.argv) == 4):
                    if(ipaddress.IPv4Network(net).overlaps(ipaddress.IPv4Network(sys.argv[3]))):
                        print("match {0} {1}".format(net, sys.argv[3]))

    else:
        print("Incorrent arguments", file=sys.stderr)
        sys.exit(1)
