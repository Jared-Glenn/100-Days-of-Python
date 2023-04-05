import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x_pos = x
        self.y_pos = y
        self.direction = "left"
        self.down = 0
        self.movement = 1.5
        
        self.image = pygame.image.load('Graphics/Aliens/Alien-HeavyCruiser.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.17)
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        
    def flight_path(self):
        if self.down > 0:
            self.y_pos += self.movement
        elif self.direction == "left" and self.down == 0:
            self.x_pos -= self.movement
        elif self.direction == "right" and self.down == 0:
            self.x_pos += self.movement
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
    
        
    def update(self, direction, down):
        self.direction = direction
        self.down = down
        self.flight_path()
        self.destroy()
        
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
