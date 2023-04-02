import pygame
from laser import Laser
import random


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_pos = 440
        self.y_pos = 900
        self.speed = 5
        
        self.image = pygame.image.load('Graphics/Player/player_ship.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.4)
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        
        self.laser_cooldown = 10
        self.cooling = self.laser_cooldown - 1
        self.lasers = pygame.sprite.Group()
    
        
        self.player_laser_list = ["Audio/player_laser1.wav", "Audio/player_laser2.wav", "Audio/player_laser3.wav", "Audio/player_laser4.wav", "Audio/player_laser5.wav"]
        
    
    def fire_laser(self):
        self.lasers.add(Laser(self.x_pos, self.y_pos, -1))
        self.player_laser_sound = pygame.mixer.Sound(random.choice(self.player_laser_list))
        self.player_laser_sound.set_volume(0.2)
        self.player_laser_sound.play(loops = 0)
    
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.x_pos <= 730:
            self.x_pos += self.speed
        elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.x_pos >= 80:
            self.x_pos -= self.speed
        if (keys[pygame.K_SPACE]) and self.cooling == self.laser_cooldown:
            self.fire_laser()
            self.cooling -= 1
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
            

    def update(self):
        self.player_input()
        if self.cooling <= 0:
            self.cooling = self.laser_cooldown
        elif self.cooling <= (self.laser_cooldown - 1):
            self.cooling -= 1

