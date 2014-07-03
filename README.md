
Monitor-Agent
=============

A python based Remote Execution Agent.
A nice lightweight agent that can be used with nagios.

This was written as a lightweight python version of the NRPE agent.

Description of each file below:
monitor-agent.cfg
---------
This configuration file specifies which port an agent is listening for a given hostname. IP of said hostname can also be provided if using a monitoring tool that connects via IP instead (e.g. nagios). Specifying IP will not affect the agent operation.

monitor-agent.init
---------
Basic init script that has been written to be as cross-OS as possible.

monitor-agent.py
---------
Core python agent

.monitor-agent.pass
---------
A password file which contains the commands the agent is allowed to run.

get_single_status.py
---------
This is a client written for nagios (but could be used for others) to grab the results of the remote call.

(C) 2014, Leigh Maddock, <awesomesourcesoftware@gmail.com>
Please see https://github.com/leighmaddock/Monitor-Agent/LICENSE for license informati
on
