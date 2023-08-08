class StreamerManager:
    
    streamers = []
    
    def __init__(self):
        pass
    
    def addStreamer(self, streamer):
        self.streamers.append(streamer)
        
    def removeStreamer(self, streamer):
        self.streamers.remove(streamer)
        
    def getStreamers(self):
        return self.streamers
    
    def getStreamer(self, name):
        for streamer in self.streamers:
            if streamer.getName() == name:
                return streamer
        return None
        
    