import json

class ConfigLoader:
    def __init__(self, path, default_config=None):
        self.path = path
        
        if default_config is None:
            default_config = {}
            
        self.config = default_config
        
    def load(self):
        with open(self.path, 'r') as f:
            try:
                self.config = json.load(f)
            except:
                self.config = {}
            
    def save(self):
        with open(self.path, 'w') as f:
            json.dump(self.config, f, indent=4)
            
    def set(self, key, value):
        self.config[key] = value
        self.save()
        
    def get(self, key):
        return self.config[key]