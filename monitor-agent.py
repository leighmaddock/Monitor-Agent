#!/usr/bin/env python
# (C) 2014, Leigh Maddock, <awesomesourcesoftware@gmail.com>
# Please see https://github.com/leighmaddock/Monitor-Agent/LICENSE for license information
#

import SocketServer, subprocess, sys, os, signal
from threading import Thread

# listen on all interfaces
IPADDR = ''
cmdfile =  "/etc/.monitor-agent.pass"
cfgfile =  "/etc/monitor-agent.cfg"

################################################################################
def usage():
	sys.stderr.write("Usage: %s\n" % sys.argv[0])

################################################################################
def getPort():
	# Just in case hostname contains domain info, split it.
	hostname=os.uname()[1].split('.')[0]
	# PORT will be default unless specifically mentioned in cfg
	for line in open(cfgfile).readlines():
		if line.strip() and not line.startswith("#"):
			row = line.split()
			if row[0] == hostname or row[0] == "default" and len(row) == 2:
				PORT = int(row[1])
	
	return PORT

################################################################################
def checkCommand(password, commandname):
	# Assume cmd is bad, unless we say it's good
	validcmd = False
	cmddata = open(cmdfile).readlines()
	for line in cmddata:
		row = line.split()
		if password == row[0] and commandname == row[1]:
			validcmd = True
	
	return validcmd

################################################################################
def pipe_command(args):
	subp = subprocess.Popen(args, stdin=None, stdout=subprocess.PIPE)
	return subp.communicate()[0], subp.returncode

################################################################################
class SingleTCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		# self.request is the client connection 1kb limit
		data = self.request.recv(1024)
		row = data.split()
		# return RC 3 if things don't go to plan
		rccode = 3
		if checkCommand(row[0], row[1]):
			reply, rccode = pipe_command(row[1:])
			if not reply:
				reply = "No output"
		else:
			reply = "Command %s not allowed to execute" % row[1]
		# Prefix message with returncode; to be parsed by caller
		reply = '%d;%s' % (rccode, reply)
		if reply:
			self.request.send(reply)
		self.request.close()

################################################################################
class SimpleServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	daemon_threads = True
	allow_reuse_address = True

	def __init__(self, serveraddr, RequestHandlerClass):
		SocketServer.TCPServer.__init__(self, serveraddr, RequestHandlerClass)

################################################################################
def main():
	PORT = getPort()
	server = SimpleServer((IPADDR, PORT), SingleTCPHandler)
	try:
		server.serve_forever()
	except:
		sys.exit(1)

################################################################################
if __name__=="__main__":
	main()

#EOF

