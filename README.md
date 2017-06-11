acl_wildcard_check.py 

Args: IP-network, wildcard, optional IPaddress to check wheter it's matched by network and wildcard

```
./acl_wildcard_check.py  208.67.220.220 0.0.2.2 208.67.222.222
208.67.220.220/30
208.67.220.224/27
208.67.221.0/24
208.67.222.0/25
208.67.222.128/26
208.67.222.192/28
208.67.222.208/29
208.67.222.216/30
208.67.222.220/31
208.67.222.222/32
match 208.67.222.222/32 208.67.222.222
```

network_to_wildcard_acl.py
"Converts" IPnetworks to wildcard format (Cisco access lists)

Args: IP-network with netmask. Both 192.168.0.0/24 and 192.168.0.0/255.255.255.0 is valid

```
$ ./network_to_wildcard_acl.py  10.0.0.4/30 
permit 10.0.0.4 0.0.0.3 any
$ ./network_to_wildcard_acl.py  10.0.0.4/255.255.255.252
permit 10.0.0.4 0.0.0.3 any
```

 
