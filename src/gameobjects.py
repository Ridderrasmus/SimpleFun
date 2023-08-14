import pygame

class Pos:
    x = 0
    y = 0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, __value: object) -> bool:
        return self.x == __value.x and self.y == __value.y
    
    def __ne__(self, __value: object) -> bool:
        return self.x != __value.x or self.y != __value.y
    
    def __add__(self, __value: object) -> object:
        return Pos(self.x + __value.x, self.y + __value.y)
    
    def __sub__(self, __value: object) -> object:
        return Pos(self.x - __value.x, self.y - __value.y)
    
    def __mul__(self, __value: object) -> object:
        return Pos(self.x * __value.x, self.y * __value.y)
    
    def __truediv__(self, __value: object) -> object:
        return Pos(self.x / __value.x, self.y / __value.y)
    
    def __floordiv__(self, __value: object) -> object:
        return Pos(self.x // __value.x, self.y // __value.y)
    
    def __mod__(self, __value: object) -> object:
        return Pos(self.x % __value.x, self.y % __value.y)
    
    def __pow__(self, __value: object) -> object:
        return Pos(self.x ** __value.x, self.y ** __value.y)
    
    def __neg__(self) -> object:
        return Pos(-self.x, -self.y)
    
    def __pos__(self) -> object:
        return Pos(+self.x, +self.y)
    
    def __abs__(self) -> object:
        return Pos(abs(self.x), abs(self.y))
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"Pos({self.x}, {self.y})"
    
    def __iter__(self):
        return iter((self.x, self.y))
    
    def __getitem__(self, __index: int) -> int:
        return (self.x, self.y)[__index]
    
    def __setitem__(self, __index: int, __value: int) -> None:
        if __index == 0:
            self.x = __value
        elif __index == 1:
            self.y = __value
        else:
            raise IndexError("Pos only has two values, x and y")
        
    def __delitem__(self, __index: int) -> None:
        raise TypeError("Pos is immutable")
    
    def __len__(self) -> int:
        return 2
    
    def __contains__(self, __value: int) -> bool:
        return __value in (self.x, self.y)
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def __lt__(self, __value: object) -> bool:
        return self.x < __value.x and self.y < __value.y
    
    def __le__(self, __value: object) -> bool:
        return self.x <= __value.x and self.y <= __value.y
    
    def __gt__(self, __value: object) -> bool:
        return self.x > __value.x and self.y > __value.y
    
    def __ge__(self, __value: object) -> bool:
        return self.x >= __value.x and self.y >= __value.y
    
    
class Area:
    
    def __init__(self, pos: Pos, size: Pos):
        self.pos = pos
        self.size = size
    
    # Checks if a point is inside the area
    def is_inside(self, pos: Pos) -> bool:
        return (self.pos.x <= pos.x <= self.pos.x + self.size.x and
                self.pos.y <= pos.y <= self.pos.y + self.size.y)
    

class Button:
    ObjPos = Pos(0, 0)
    width = 0
    height = 0
    curr_colour = (255, 0, 0)
    def_colour = (255, 0, 0)
    hover_colour = (255, 0, 0)
    symbol = " "
    
    
    def __init__(self, pos: Pos|tuple, size: tuple, colour=(255, 0, 0)):
        if type(pos) == Pos:
            self.ObjPos = pos
        else:
            self.ObjPos = Pos(pos[0], pos[1])
        
        self.width = size[0]
        self.height = size[1]
        
        self.curr_colour = colour
        self.def_colour = colour
        self.hover_colour = (colour[0] + 50, colour[1] + 50, colour[2] + 50)
        
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.curr_colour, (self.ObjPos.x, self.ObjPos.y, self.width, self.height))
        if (self.symbol == "X"):
            pygame.draw.line(screen, (0, 0, 0), (self.ObjPos.x + 10, self.ObjPos.y + 10), (self.ObjPos.x + self.width - 10, self.ObjPos.y + self.height - 10), 5)
            pygame.draw.line(screen, (0, 0, 0), (self.ObjPos.x + self.width - 10, self.ObjPos.y + 10), (self.ObjPos.x + 10, self.ObjPos.y + self.height - 10), 5)
        elif (self.symbol == "O"):
            pygame.draw.circle(screen, (0, 0, 0), (self.ObjPos.x + self.width // 2, self.ObjPos.y + self.height // 2), self.width // 2 - 10, 5)
        else:
            font = pygame.font.SysFont("segoeuiemoji", 50)
            text = font.render(self.symbol, True, (0, 0, 0))
            text_rect = text.get_rect(center=(self.ObjPos.x + self.width // 2, self.ObjPos.y + self.height // 2))
            text_rect.height = self.height
            text_rect.width = self.width
            screen.blit(text, text_rect)
        
    def is_hovered(self, pos: Pos|tuple) -> bool:
        if type(pos) != Pos:
            pos = Pos(pos[0], pos[1])
            
        return (self.ObjPos.x <= pos.x <= self.ObjPos.x + self.width and
                self.ObjPos.y <= pos.y <= self.ObjPos.y + self.height)
        
    def click(self, player):
        if(self.symbol != " "):
            return
        
        self.symbol = player.symbol
            
class Player:
    
    id = 0
    symbol = None
    
    def __init__(self, id, symbol):
        self.id = id
        self.symbol = symbol
        
        