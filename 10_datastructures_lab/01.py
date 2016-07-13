import sys
hosts = {}

#read all hosts from file
with open('4.Collections\\hosts', 'r') as f:
    for line in f:
        keyvalue = line.split("=")
        hosts[keyvalue[0]] = keyvalue[1][:-1] # dont take last character as it is \n

# find all requested hosts in dictionary
for host in sys.argv[1:]:
    if host in hosts:
        print "IP of {} is {}".format(host, hosts[host])
    else:
        print "IP of {} is unknown".format(host)
