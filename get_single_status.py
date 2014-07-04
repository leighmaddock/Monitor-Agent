#!/usr/bin/env python
# (C) 2014, Leigh Maddock, <awesomesourcesoftware@gmail.com>
# Please see https://github.com/leighmaddock/Monitor-Agent/LICENSE for license information
#

import os, sys, socket
cfgfile = "/etc/monitor-agent.cfg"

################################################################################
def usage():
	sys.stderr.write("Usage: %s <hostname/ipaddress> <commandpass> <commandname> .... <commandargs> \n" % sys.argv[0])
	sys.exit(1)

################################################################################
def getPort(hostname):
	# PORT will be default unless specifically mentioned in cfg
	for line in open(cfgfile).readlines():
		if line.strip() and not line.startswith("#"):
			row = line.split()
			if row[0] == hostname or row[0] == "default":
				PORT = int(row[1])

	return PORT

################################################################################
def getResults(HOST, PORT, remotecmd, remotepass):
	message = "%s %s" % (remotepass, " ".join(remotecmd))
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		sock.connect((HOST, PORT))
		sock.send(message)
		# 1kb limit
		rccode = sock.recv(10, socket.MSG_OOB)
		reply = sock.recv(1024)
		sock.close()
	except:
		print "Connection issues, please investigate"
		sock.close()
		sys.exit(2)
	message = reply


	return int(rccode), message

################################################################################
def main():
	# Variables
	if len(sys.argv) < 4:
		usage()
	HOST = sys.argv[1]
	remotepass = sys.argv[2]
	remotecmd = sys.argv[3:]

	PORT = getPort(HOST)
	rccode, message = getResults(HOST, PORT, remotecmd, remotepass)
	print message
	sys.exit(rccode)

################################################################################
if __name__=="__main__":
    main()

#EOF

