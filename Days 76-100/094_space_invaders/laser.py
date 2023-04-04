import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.x_pos = x
        self.y_pos = y
        self.direction = direction
        self.speed = 6
        
        self.image = pygame.Surface((4, 20))
        self.image.fill("white")
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
    
        
    def update(self):
        self.y_pos += self.direction * self.speed
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))