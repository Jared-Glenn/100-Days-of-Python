import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.images = []
        self.x_pos = x_pos
        self.y_pos = y_pos
        
        explosion_file_path = 'Graphics/Explosions/Alien Explosion/tile0'
        for x in range(64):
            if x > 9:
                explosion = explosion_file_path + str(x) + ".png"
                img = pygame.image.load(explosion).convert_alpha()
                img = pygame.transform.rotozoom(img, 0, 1)
                self.images.append(img)
                
            else:
                explosion = explosion_file_path + '0' + str(x) + ".png"
                img = pygame.image.load(explosion).convert_alpha()
                img = pygame.transform.rotozoom(img, 0, 1)
                self.images.append(img)
            
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        self.counter = 0
        
        def update(self):
            print(self.images)
            explosion_speed = 1
            self.counter += 1
            if self.counter >= explosion_speed and self.index < len(self.images) -1:
                self.counter = 0
                self.index += 1
                self.image = self.images[self.index]
            
            if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
                self.kill()

