from twisted.internet import protocol

class RPGProtocol(protocol.Protocol):
    def connectionMade(self):
        self.player_name = None
        self.factory.addPlayer(self)

    def connectionLost(self, reason):
        self.factory.removePlayer(self)

    def dataReceived(self, data):
        command = data.decode().strip()
        response = self.factory.processCommand(self, command)
        self.transport.write(response.encode())

class RPGFactory(protocol.Factory):
    def __init__(self):
        self.players = []

    def buildProtocol(self, addr):
        protocol_instance = RPGProtocol()
        protocol_instance.factory = self
        return protocol_instance

    def addPlayer(self, player):
        self.players.append(player)

    def removePlayer(self, player):
        self.players.remove(player)

    def processCommand(self, player, command):
        if player.player_name is None and command.startswith("name "):
            player.player_name = command[5:]
            return f"Welcome, {player.player_name}!\n"
        elif player.player_name is not None:
            for p in self.players:
                if p != player:
                    p.transport.write(f"{player.player_name}: {command}\n".encode())
            return ""
        else:
            return "Please set your name with 'name <your_name>'.\n"

from twisted.internet import reactor

factory = RPGFactory()
reactor.listenTCP(12345, factory)
reactor.run()
