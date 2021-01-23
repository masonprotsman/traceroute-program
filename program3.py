
#filename = #"Masons-Macbook-Pro-2/Users/mason/sampletcpdump.txt"
file = open(filename, 'r')
readFile = file.read()
for line in readFile:
    for part in line.split()
        try:
            IPaddress = part.split('IP')
            IpNum = address[1]
            print(IpNum)
        except ValueError:
            pass # not in the right format
        else:
            # do something with part, or address and network, or whatever

