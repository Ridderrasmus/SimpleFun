# Project name:  Tic Tac Toe server
# 
# Project description: 
#   To create a server for the Tic Tac Toe game.
#   The server will organise lobby and game sessions.
#   The server will also keep track of leaderboards.
# 
# Project Python Version:
#   3.11.4
# 
# Authors:
#   Rasmus Tanggaard
# 
# File name: main.py


import socket
import json
import os


class Server:
    
    ipadress = ""
    port = 0
    socket = None
    clients = []
    running = False
    
    def __init__(self) -> None:
        # Config
        cfgLoader = FileLoader("config.json", {"ipadress" : socket.gethostbyname(socket.gethostname()), "port" : 5555})
        cfgLoader.load()
        
        #Leaderboard
        lbLoader = FileLoader("leaderboard.json", {"players" : { "name" : "", "wins" : 0, "losses" : 0, "draws" : 0}})
        
        self.ipadress = cfgLoader.file["ipadress"]
        self.port = cfgLoader.file["port"]
        
        print("Starting server on " + self.ipadress + ":" + str(self.port))
        
    def start(self):
        self.running = True
        
        while self.running:
            pass
        
    def stop(self):
        self.running = False
    
    def handleClient(self, client):
        pass
                


class FileLoader:
    path = None
    file = None
    
    def __init__(self, path : str, default : dict = None) -> None:
        self.path = path
        self.file = default if default else {}
        
        self.load()

        
    def load(self):
        if os.path.isfile(self.path):
            with open(self.path, "r") as f:
                try:
                    self.file = json.load(f)
                except:
                    pass
        else:
            with open(self.path, "w") as f:
                json.dump(self.file, f)
        
    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.file, f)
        pass
    
    def getValue(self, key : str, default = None):
        self.load()
        if default == None:
            return self.file[key]
        return self.file.get(key, default)
    
    def getValues(self):
        self.load()
        return self.file
    
    def setValue(self, key : str, value):
        self.file[key] = value
        self.save()

def main():
    server = Server()



if __name__ == "__main__":
    main()