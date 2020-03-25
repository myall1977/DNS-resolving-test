#!/usr/bin/env python2
import sys
import dns.resolver
test_nameservers = ['168.126.63.1','202.46.34.75']
test_file = sys.argv[1].strip()
# Test file format
# {org_GTM},{custom_GTM}
# downloadcenter.samsung.com.edgekey.net.globalredir.akadns.net,downloadcenter.samsung.com.edgekey.net.globalredir-samsung.akadns.net
test_list = open(test_file,'r').readlines()

def DNS_resolving(_hostname,_record,_resolver):
	myResolver = dns.resolver.Resolver()
	myResolver.nameservers = [_resolver]
	r = [_hostname]
	try:
		myAnswers = myResolver.query(_hostname,_record)
		for rdata in myAnswers:
			r.append(rdata.to_text())
	except:
			r.append('error')
	return ",".join(r)
	# downloadcenter.samsung.com.edgekey.net.globalredir.akadns.net,e1722.d.akamaiedge.net.

for dns_ip in test_nameservers:
	print dns_ip
	for items in test_list:
		result = []
		for item in items.split(","):
			result.append(DNS_resolving(item.strip(),'CNAME',dns_ip))
		print ",".join(result)
