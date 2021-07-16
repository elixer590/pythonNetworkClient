#test client
import pygame

class playerContainer:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.body = pygame.Surface((32,32))
        self.body.fill((0,0,255))



# initilize screen

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init() # start the pygame display
screen = pygame.display.set_mode((960, 640)) # screen is an object. this initializes the screen as 800x600
background = pygame.Surface(screen.get_size()).convert() # background color. converting the image is better for draw performance?
background.fill((255,255,255)) # fills the background with a single color (RGB)
screen.blit(background, (0,0))
pygame.display.flip()

#create player
player = playerContainer()

#necessary vars
MOVESPEED = 32
#main loop
running = True
while running:
    ## ---------------------------------------------------------------------------------------------
    ## This is the event handler - turn this into a functioncall do it doesnt eat the game loop
    ## ---------------------------------------------------------------------------------------------
    for event in pygame.event.get(): # returns a list of events. This will clear the event list each time so all event get objects should typially be handled here
        if event.type == pygame.QUIT: #X pressed to close window
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
            if event.key == pygame.K_UP:
               player.y -= MOVESPEED
                
            if event.key == pygame.K_DOWN:
                player.y += MOVESPEED
                
            if event.key == pygame.K_LEFT:
                player.x -= MOVESPEED

            if event.key == pygame.K_RIGHT:
                player.x += MOVESPEED
                
    screen.blit(background, (0,0))
    screen.blit(player.body, (player.x, player.y))
    pygame.display.flip()

pygame.quit()

