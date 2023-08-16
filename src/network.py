from _socket import _Address
import socket

class ClientSocket(socket.socket):
    
    def __init__(self, host, port):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        
    def send(self, data):
        super().send(data.encode())
    
    def receive(self):
        return super().recv(1024).decode()
    
    
    
class ServerSocket(socket.socket):
    
    def __init__(self, host, port):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((host, port))
        self.listen(1)
        
    def accept(self):
        return super().accept()
    
    def send(self, data):
        super().send(data.encode())
        
    def receive(self):
        return super().recv(1024).decode()