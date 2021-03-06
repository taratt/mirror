"""Custom topology example
Two directly connected switches plus a host for each switch:
   host --- switch --- switch --- host
Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        switch1= self.addSwitch( 's1' )
        switch2 = self.addSwitch('s2')
        host1 = self.addHost( 'h1' )
        host2 = self.addHost( 'h2')
        host3 = self.addHost( 'h3')


        # Add links
        self.addLink( switch1,host1 )
        self.addLink( switch1 , host2)
        self.addLink( switch2, host3)
        self.addLink(switch2, switch1)


topos = { 'mytopo': ( lambda: MyTopo() ) }
