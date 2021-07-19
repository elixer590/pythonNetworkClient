#test client
import pygame
import socket
import convertEncodedAscii as convert

class playerContainer:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.body = pygame.Surface((32,32))
        self.body.fill((0,0,255))

class ServerConnection:
    def __init__(self, socket):
        self.socket = socket
        self.lastupdate = 0
        self.playersDict = {}

    def handleNetworking(self, timer, data):
        if timer - self.lastupdate > 10:
            self.socket.sendall(str(data).encode('ascii'))
            information = self.socket.recv(1024) #1024 - is this a packet size??
            information = information.decode('ascii')
            self.playersDict = convert.decode(information)
            print(self.playersDict)
            self.lastupdate = timer

            
    
# initilize screen
pygame.init() # start the pygame display
screen = pygame.display.set_mode((960, 640)) # screen is an object. this initializes the screen as 800x600
background = pygame.Surface(screen.get_size()).convert() # background color. converting the image is better for draw performance?
background.fill((255,255,255)) # fills the background with a single color (RGB)
screen.blit(background, (0,0))
pygame.display.flip()

#initialize networking
HOST = '127.0.0.1'  
PORT = 1337 

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.connect((HOST, PORT))
# below was used for sending a single one-shot message
# we want to reference this in a network function
'''with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for msg in msglist:
        s.sendall(msg)
        data = s.recv(1024)
        print('Received', repr(data))'''

#create player
player = playerContainer()

#necessary vars
MOVESPEED = 32
timeplayed = pygame.time.Clock()
timer = timeplayed.tick()
serverConn = ServerConnection(serversocket)
myID = serverConn.socket.getsockname()[1] # gets the port number which I am using to determine the id of the session

#for now a discrete alternate player object
otherPlayer = playerContainer()
otherPlayer.body.fill((255,0,0))

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

    serverConn.handleNetworking(timer, (player.x, player.y))
    screen.blit(background, (0,0))
    for key in serverConn.playersDict.keys():
        if key == myID:
            continue
        coords = serverConn.playersDict[key]
        screen.blit(otherPlayer.body, coords)
    screen.blit(player.body, (player.x, player.y))
    pygame.display.flip()

    timer += timeplayed.tick()

pygame.quit()

