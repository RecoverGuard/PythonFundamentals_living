#input and check an ipv4 address

ipchk = input('Apply an IP address: ')

if ipchk == '192.168.1.1':
    print('The IP address of the gateway was set: ' + ipchk + ' This is not recommended.')
elif ipchk:
    print('Looks like the IP address was set: ' + ipchk)
else:
    print('you did not provide any input')