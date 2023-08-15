from twisted.internet import protocol, reactor

class RPGClient(protocol.Protocol):
    def dataReceived(self, data):
        print(data.decode().strip())
        
    def connectionMade(self):
        input_arg = input("Enter your name: ")
        self.transport.write(b"name " + input_arg.encode())

class RPGClientFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return RPGClient()

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed.")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost.")
        reactor.stop()

reactor.connectTCP('localhost', 12345, RPGClientFactory())
reactor.run()
