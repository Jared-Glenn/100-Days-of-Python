import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x_pos = x
        self.y_pos = y
        self.direction = "left"
        self.down = 0
        self.movement = 3
        
        self.image = pygame.image.load('Graphics/Aliens/Alien-HeavyCruiser.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.2)
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        
    def flight_path(self):
        if self.down >= 5:
                self.y_pos += self.movement
                self.down = 0
        elif self.down > 0:
                self.y_pos += self.movement
                self.down += 1
        elif self.direction == "left" and self.down == 0:
            if self.x_pos < 750:
                self.x_pos += self.movement
            elif self.x_pos >= 750:
                self.y_pos += self.movement
                self.direction = "right"
                self.down += 1
        elif self.direction == "right" and self.down == 0:
            if self.x_pos > 50:
                self.x_pos -= self.movement
            elif self.x_pos <= 50:
                self.y_pos += self.movement
                self.direction = "left"
                self.down += 1
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        
    def update(self):
        self.flight_path()
        self.destroy()
        
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
