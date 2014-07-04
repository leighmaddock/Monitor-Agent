
Monitor-Agent
=============

A python based Remote Execution Agent.
A nice lightweight agent that can be used with nagios.

This was written as a lightweight python version of the NRPE agent.

Management of Files:
---------
These files should be centrally managed, to be pushed out via a configuration tool (ansible/puppet/chef etc.).
Ansible playbook coming soon. monitor-agent.cfg should live on the nagios server, so that get_single_status.py knows how to connect.



Description of each file below:
monitor-agent.cfg
---------
Location: /etc/monitor-agent.cfg
This configuration file specifies which port an agent is listening for a given hostname. IP of said hostname can also be provided if using a monitoring tool that connects via IP instead (e.g. nagios). Specifying IP will not affect the agent operation.

monitor-agent.init
---------
Location: /etc/init.d/monitor-agent.init
Basic init script that has been written to be as cross-OS as possible.

monitor-agent.py
---------
Location: /usr/local/bin/monitor-agent.py
Core python agent. Due to the nature of the program running anything after arg 0, it's ideal this program doesn't run as any important users due to potential security issues. The pass file has not been locked down to allow flexability in nagios arg lists.

.monitor-agent.pass
---------
Location: /etc/.monitor-agent.pass
A password file which contains the commands the agent is allowed to run.

get_single_status.py
---------
Location: Nagios server, a good place would be the plugins directory.
This is a client written for nagios (but could be used for others) to grab the results of the remote call.
Simply pass <hostname>, password and commandname + args.

(C) 2014, Leigh Maddock, <awesomesourcesoftware@gmail.com>
Please see https://github.com/leighmaddock/Monitor-Agent/LICENSE for license informati
on
