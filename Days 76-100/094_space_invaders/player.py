import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_pos = 440
        
        self.image = pygame.image.load('Graphics/Player/player_ship.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.4)
        self.rect = self.image.get_rect(center = (self.x_pos, 950))
        


        
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x_pos += 10
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x_pos -= 10
            
    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
        
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()