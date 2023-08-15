# Project Name: 
#   TBD
#
# Project Description: 
#   Let's create Tic Tac Toe in Python!
#
# Project Python Version:
#   3.11.4
# 
# Authors: 
#   Rasmus Tanggaard, Malthe Sørensen, Jonas Søgaard Frederiksen
from twisted.internet import protocol
from twisted.internet.protocol import connectionDone
from twisted.python import failure

class Application:
    def __init__(self):
        self.game_loop()

    def game_loop(self):
        while self.game.running:
            self.game.get_events()
            self.game.update()
            self.game.draw()
        self.game.quit()

class RPGFactory(protocol.Factory):
    def __init__(self):
        self.players = []
    
    def buildProtocol(self, addr):
        return RPGProtocol()
    
    def addPlayer(self, player):
        self.players.append(player)
        
    def removePlayer(self, player):
        self.players.remove(player)
        
    def processCommand(self, player, command):
        pass

class RPGProtocol(protocol.Protocol):
    def connectionMade(self):
        self.factory.addPlayer(self)
        
    def connectionLost(self):
        self.factory.removePlayer(self)
    
    def dataReceived(self, data):
        command = data.decode().strip()
        response = self.factory.processCommand(self, command)
        self.transport.write(response.encode())


class GameLogic:
    
    def __init__(self):
        pass


if __name__ == "__main__":
    app = Application()