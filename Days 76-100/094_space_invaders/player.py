import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_pos = 440
        self.y_pos = 900
        
        self.image = pygame.image.load('Graphics/Player/player_ship.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.4)
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        


        
    def player_input(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.x_pos <= 730:
            self.x_pos += 10
        elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.x_pos >= 80:
            self.x_pos -= 10
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
            
        
    def update(self):
        self.player_input()

