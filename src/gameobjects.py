
class PlayerCharacter:
    def __init__(self, name, character_class, health, strength, agility, intelligence):
        self.name = name
        self.character_class = character_class
        self.health_max = health
        self.health_current = health
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        
    def __str__(self):
        return f"{self.name} the {self.character_class}"
    
    def damage(self, amount):
        self.health_current -= amount
        if self.health_current < 0:
            self.health_current = 0
        elif self.health_current > self.health_max:
            self.health_current = self.health_max
            
    def damage(self):
        return self.health_current
    
    
class NPC:
    is_known = False
    
    def __init__(self, name, description, health, strength, agility, intelligence):
        self.name = name
        self.description = description
        self.health_max = health
        self.health_current = health
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        
    def __str__(self):
        if self.is_known:
            return f"{self.name}"
        return f"{self.description}"
    
    def damage(self, amount):
        self.health_current -= amount
        if self.health_current < 0:
            self.health_current = 0
        elif self.health_current > self.health_max:
            self.health_current = self.health_max
    
    def damage(self):
        return self.health_current