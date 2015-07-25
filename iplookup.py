#!/usr/bin/env python

from __future__ import print_function
import requests
import sys
import time


# Loading bar dots....
def print_dot():
	print(".",end="")
	sys.stdout.flush()

def print_last_dot():
	print(".")
	sys.stdout.flush()


# Function to perform Geo IP lookup for 'ip' and return request's response object
def ip_lookup(ip):
	geoip_request = "http://www.telize.com/geoip/" + ip.strip()
	print_dot()
	geoip_response = requests.get(geoip_request)
	print_dot()
	return geoip_response	



# ========================================


if __name__ == "__main__":

	# open file containing list of IPs
	ip_file = open('ips.list', 'r')
	ip_addresses = ip_file.readlines()

	# empty list for collecting response objects 
	geoip_responses = []


	# iterate through IPs read from file and pass
	# into ip_lookup function, adding response objects
	# to geoip_responses list
	print("Performing Geo IP lookups...")
	for ip in ip_addresses:
		geoip_lookup = ip_lookup(ip)
		geoip_responses.append(geoip_lookup)


	# print final dot, aka include newline char
	print_last_dot()
	print("\nLookups completed:\n\n")


	# print text of each response object returned by ip_lookup
	for geolookup in geoip_responses:
		print(geolookup.text)


