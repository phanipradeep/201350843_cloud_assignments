#!/usr/bin/python
""" Mininet Assignment 
Author : Pradeep Anumala
Roll No. : 201350843
"""


from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
import sys
def emptyNet():

    "Create an empty network and add nodes to it."
    args=(sys.argv)
    no_of_hosts=int(args[1])
    no_of_Switches=int(args[2])

    print "no of hosts : "+no_of_hosts
    print "no of swithes : "+no_of_switches

    net = Mininet( controller=Controller )

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    info( '*** Adding hosts\n' )
    hosts=[]
    for i in range(no_of_hosts):
	hosts.append(net.addHost('h'+str(i+1)))

    info( '*** Adding switch\n' )
    switches=[]
    for i in range(no_of_hosts):
	switches.append(net.addSwitch('s'+str(i+1)))

    info( '*** Creating links\n' )
    for i in range(no_of_switches):
	if i+2 < no_of_switches:
		net.addLinks(switches[i],switches[i+2])
	if i%2 == 0 :
		net.addLinks(switches[i],hosts[2*i])
		net.addLinks(switches[i],hosts[2*i+2])
	else:
		net.addLinks(switches[i],hosts[2*i-1])
		net.addLinks(switches[i],hosts[2*i+1])

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
