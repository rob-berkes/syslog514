from pymongo import Connection
from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol

class Echo(DatagramProtocol):
	def datagramReceived(self,data,(host,port)):
		print "received %r from %s:%d" %(data,host,port)
		IREC={"host":host,"port":port,"data":data}
		db.log.insert(IREC)



conn=Connection()
db=conn.syslog

reactor.listenUDP(514,Echo())
reactor.run()
