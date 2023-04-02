import pygame
from sys import exit
import os
from player import Player
from aliens import Alien
    

os.chdir("100 Days of Python/Days 76-100/094_space_invaders/")
pygame.init()
screen = pygame.display.set_mode((800,1000))
pygame.display.set_caption('Space Invaders')
clock = pygame.time.Clock()
title_font = pygame.font.Font('Font/Pixeltype.ttf', 90)
instructions_font = pygame.font.Font('Font/Pixeltype.ttf', 40)
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('Audio/mist_city.mp3')
bg_music.set_volume(0.4)
bg_music.play(loops = -1)

space_background = pygame.image.load('Graphics/Space/Stars.png').convert_alpha()

# Intro Screen
player_ship = pygame.image.load('Graphics/Player/player_ship.png').convert_alpha()
# player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_ship_rect = player_ship.get_rect(center = (400, 200))

title = title_font.render('SPACE INVADERS', False, (111,196,169))
title_rect = title.get_rect(center = (400, 400))

instructions = instructions_font.render('Press space to blast off!', False, (111,196,169))
instructions_rect = instructions.get_rect(center = (400, 500))


# Game Proper
# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

alien_group =  pygame.sprite.Group()
for i in range(10):
    for j in range(5):
        x = (i*50) + 100
        y = (j*50) + 100
        alien_group.add(Alien(x, y))

alien_direction = "right"
alien_down = 0
alien_down_distance = 10


def collision_checks():
    # Player Lasers
    if player.sprite.lasers:
        for laser in player.sprite.lasers:
            if pygame.sprite.spritecollide(laser, alien_group, True):
                laser.kill()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()
                
    if game_active:
        screen.fill((0,0,0))
        screen.blit(space_background, (0, 0))
        
        player.sprite.lasers.draw(screen)
        player.sprite.lasers.update()
        
        player.draw(screen)
        player.update()
        
        # Check if aliens should be moving down.
        if alien_down >= alien_down_distance:
            alien_down = 0
        elif alien_down >= 1:
            alien_down += 1
        # If not and aliens are moving out of bounds, reverse direction and start moving down.
        else:
            all_aliens = alien_group.sprites()
            for alien in all_aliens:
                if alien_direction == "right" and alien.rect.right >= 780 and alien_down == 0:
                    alien_direction = "left"
                    alien_down = 1
                elif alien_direction == "left" and alien.rect.left <= 20 and alien_down == 0:
                    alien_direction = "right"
                    alien_down = 1
        
        alien_group.draw(screen)
        alien_group.update(alien_direction, alien_down)
    
        collision_checks()
        
    else:
        screen.fill((0,0,0))
        screen.blit(space_background, (0, 0))
        screen.blit(player_ship, player_ship_rect)

        screen.blit(title, title_rect)

        if score == 0:
            screen.blit(instructions, instructions_rect)
        else:
            # screen.blit(score_message, score_message_rect)
            pass
    
    pygame.display.update()
    clock.tick(60)