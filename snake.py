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

        #move the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -1*SNAKE_SIZE
                snake_dy =0
            if event.key == pygame.K_RIGHT:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = SNAKE_SIZE
            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -1*SNAKE_SIZE
    #Get a list of all keys currently being pressed down
    #keys = pygame.key.get_pressed()   
    
    #add the head coordinate to the first index of the body coordinate list
    body_coords.insert(0, head_coord)
    body_coords.pop()

    #update the x y position of the snake head
    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)         

    #check for game over
    #print(head_rect.left, head_rect.right, head_rect.top, head_rect.bottom)
    if head_rect.left < 0 or head_rect.right > WINDOW_WIDTH or head_rect.top < 0 or head_rect.bottom > WINDOW_HEIGHT or head_coord in body_coords:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()


        #Pause the game until the player presses a key, then reset the game
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                #The player wants to play again
                if event.type == pygame.KEYDOWN:
                    score = 0

                    head_x = WINDOW_WIDTH//2
                    head_y = WINDOW_HEIGHT // 2 + 100
                    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
                    body_coords = []
                    snake_dx = 0
                    snake_dy = 0
                    is_paused = False
                #The player wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False    

    #check for collisions
    if head_rect.colliderect(apple_rect):
        score += 1
        pick_up_sound.play()

        apple_x = random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
        apple_y = random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)        
        apple_coord = (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)

        body_coords.append(head_coord)


    #update HUD
    score_text = font.render('Score: ' + str(score), True, GREEN, DARKRED)

    #Move the dragon continously
    #if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_rect.left > 0:
    #    dragon_rect.x -= PLAYER_VELOCITY
    #if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_rect.right < WINDOW_WIDTH:
    #    dragon_rect.x += PLAYER_VELOCITY
    #if keys[pygame.K_UP] and player_rect.top > 64:
    #    player_rect.y -= PLAYER_VELOCITY
    #if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
    #    player_rect.y += PLAYER_VELOCITY


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

    for body in body_coords:
        pygame.draw.rect(display_surface, DARKGREEN, body)
    apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)
    head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)


    #update display
    pygame.display.update()

    #Tick the clock
    clock.tick(FPS)


#End the game
pygame.quit()