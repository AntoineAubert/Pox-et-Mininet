#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
import time


class Mytopo(Topo):
	
	def __init__(self):
		"Create custom topo."
		
		# Initialize topo
		Topo.__init__(self)
		
		###### Create the first sub-network (servers part)
		# Network nodes
		web_server	= self.addHost("web")
		traff1		= self.addHost("traff1")
		traff2		= self.addHost("traff2")
		
		# The Switch 
		s1			= self.addSwitch("s1")
		
		###### Create the scond sub-network (hots part)
		# Network nodes
		# ~ attacker	= self.addHost("attacker")
		# ~ client1		= self.addHost("client1")
		# ~ client2		= self.addHost("client2")
		
		# The Switch 
		s2			= self.addSwitch("s2")
		
		# The aggregator switch
		# ~ s3		= self.addSwitch("s3")
		
		# The links
		self.addLink(web_server, s1)
		self.addLink(traff1, s1)
		self.addLink(traff2, s1)
		# ~ self.addLink(attacker, s2)
		# ~ self.addLink(client1, s2)
		# ~ self.addLink(client2, s2)
		# ~ self.addLink(s1,s3)
		# ~ self.addLink(s2,s3)
		
					
def run():
	c0 = RemoteController('c0', '192.168.122.3', 6633)
	my_topo = Mytopo()
	net = Mininet(topo=my_topo, controller=None)
	net.addController(c0)
	net.start()
	net.stop()
	
if __name__ == '__main__':
	run()
