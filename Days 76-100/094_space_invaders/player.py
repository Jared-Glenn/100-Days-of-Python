import pygame
from laser import Laser

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_pos = 440
        self.y_pos = 900
        
        self.image = pygame.image.load('Graphics/Player/player_ship.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.4)
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        
        self.laser_cooldown = 50
        self.cooling = self.laser_cooldown - 1
        self.lasers = pygame.sprite.Group()
    
    def fire_laser(self):
        self.lasers.add(Laser(self.x_pos, self.y_pos, -1))
    
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.x_pos <= 730:
            self.x_pos += 10
        elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.x_pos >= 80:
            self.x_pos -= 10
        if (keys[pygame.K_SPACE]) and self.cooling == self.laser_cooldown:
            self.fire_laser()
            self.cooling -= 1
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
            

    def update(self):
        self.player_input()
        print(self.cooling)
        if self.cooling <= 0:
            self.cooling = self.laser_cooldown
        elif self.cooling <= (self.laser_cooldown - 1):
            self.cooling -= 1

