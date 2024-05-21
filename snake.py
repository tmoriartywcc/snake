import pygame, random

#initialize pygame
pygame.init()

#create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("~~Snake~~")

#Set FPS and Clock
FPS = 20
clock = pygame.time.Clock()

#Set Game Values
SNAKE_SIZE = 20

head_x = WINDOW_WIDTH//2
head_y = WINDOW_HEIGHT//2 + 100

snake_dx = 0
snake_dy = 0

score = 0

#Set Colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
RED = (255, 0, 0)
DARKRED = (150, 0, 0)
WHITE = (0, 0, 0)

#Set Fonts - using system font - no need for file
font = pygame.font.SysFont('gabriola', 48)

#Set Text
title_text = font.render('~~Snake~~', True, GREEN, DARKRED)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

score_text = font.render('Score: ' + str(score), True, GREEN, DARKRED)
score_rect = score_text.get_rect()
score_rect.topleft = (10,10)

game_over_text = font.render('GAMEOVER', True, RED, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render('Press any key to play again', True, RED, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)



#Set Sounds and Music
pick_up_sound = pygame.mixer.Sound('pick_up_sound.wav')

#Set Images (use simple rects - so just create thier coordinates)
#For a rectangle you need (x, y, width, height)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
body_coords = []

apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)
head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)


#The main game loop
running = True
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

    #Get a list of all keys currently being pressed down
    #keys = pygame.key.get_pressed()   
    

    #Move the dragon continously
    #if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_rect.left > 0:
    #    dragon_rect.x -= PLAYER_VELOCITY
    #if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_rect.right < WINDOW_WIDTH:
    #    dragon_rect.x += PLAYER_VELOCITY
    #if keys[pygame.K_UP] and player_rect.top > 64:
    #    player_rect.y -= PLAYER_VELOCITY
    #if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
    #    player_rect.y += PLAYER_VELOCITY

    #Move the coin
            '''
    if coin_rect.x < 0:
        #player missed coin
        player_lives -= 1
        miss_sound.play()
        #place coin off the end of the screen again
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)
    else:
        coin_rect.x -= coin_velocity
        #move hte coint
    #Check for collison between player and coin
    if player_rect.colliderect(coin_rect):
        score += 1
        coin_sound.play()
        coin_velocity += COIN_ACCELERATION
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

    #update HUD
    score_text = font.render('Score: ' + str(score), True, GREEN, DARKGREEN)
    lives_text = font.render('Lives: ' + str(player_lives), True, GREEN, DARKGREEN)


    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        #Pause game until player presses a key, then reset
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                #player wants to play again
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    player_rect.y = WINDOW_HEIGHT // 2
                    coin_velocity = COIN_STARTING_VELOCITY
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                #player wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False
    '''

    #Fill the display surface to cover old images
    display_surface.fill(WHITE)

    #Draw rectangles to represent rectangles
    #pygame.draw.rect(display_surface, (0,255,0), dragon_rect, 1)
    #pygame.draw.rect(display_surface, (255,0,0), coin_rect, 1)
    
    #Blit the HUD to the screen
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)

    #Blit (copy) assets to the screen
    #Still need to do the body


    pygame.draw.rect(display_surface, RED, apple_coord)
    pygame.draw.rect(display_surface, GREEN, head_coord)


    #update display
    pygame.display.update()

    #Tick the clock
    clock.tick(FPS)


#End the game
pygame.quit()