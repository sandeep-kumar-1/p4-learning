from p4utils.utils.network_API import NetworkAPI

net = NetworkAPI()

# Network general options
net.setLogLevel('info')
net.setCompiler(p4rt=True)
net.execScript('python controller.py', reboot=True)

# Network definition
net.addP4RuntimeSwitch('s1')
net.setP4Source('s1','./p4src/l2_basic_forwarding.p4')
net.addHost('h1')
net.addHost('h2')
net.addHost('h3')
net.addHost('h4')
net.addLink('s1', 'h1')
net.addLink('s1', 'h2')
net.addLink('s1', 'h3')
net.addLink('s1', 'h4')

# Assignment strategy
net.l2()

# Nodes general options
net.disablePcapDumpAll()
net.disableLogAll()
net.enableCli()
net.startNetwork()