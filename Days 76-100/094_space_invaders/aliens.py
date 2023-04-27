import pygame
from laser import Laser
import random

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
        
        self.laser_odds = 50
        self.lasers = pygame.sprite.Group()
    
        
        self.alien_laser_list = ["Audio/alien_laser1.wav", "Audio/alien_laser2.wav", "Audio/alien_laser3.wav"]  
        
        
    def flight_path(self):
        if self.down > 0:
            self.y_pos += self.movement
        elif self.direction == "left" and self.down == 0:
            self.x_pos -= self.movement
        elif self.direction == "right" and self.down == 0:
            self.x_pos += self.movement
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
    
    def fire_laser(self):
        if self.laser_odds > 200 or self.laser_odds < 2:
            self.laser_odds == 100
        odds = random.randint(1, self.laser_odds)
        if odds == 1:
            self.lasers.add(Laser(self.x_pos, self.y_pos, 1))
            self.player_laser_sound = pygame.mixer.Sound(random.choice(self.alien_laser_list))
            self.player_laser_sound.set_volume(0.2)
            self.player_laser_sound.play(loops = 0)
            self.laser_odds += 20
        else:
            self.laser_odds -= 5
        
    def update(self, direction, down, laser_odds):
        self.laser_odds = laser_odds
        self.direction = direction
        self.down = down
        self.flight_path()
        self.fire_laser()
        self.destroy()
        
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
