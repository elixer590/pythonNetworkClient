# demo server app?
# in this we need to test creating a socket and talking to it

import socket
import convertEncodedAscii as convert

# setup some constants that we will use later
HOST = '127.0.0.1'
PORT = 1337

#I need to keep track of who is connecting AND their location
# probably will need to build a custom data type for this
# for now a dictionary can hold data like so maybe?
# data{id:(x,y))

fakePlayerID = 13337
moves = [(160, 192),(128, 192),(96, 192),(96, 160),(96, 192),(128, 192)]
fakeindex = 0

playerdict = {}
#Heres some stuff I copied from a tutorial
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
        s.listen()
        conn, addr = s.accept()        
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                playerdict[addr[1]] = data.decode('ascii')
                playerdict[fakePlayerID] = str(moves[fakeindex%len(moves)])
                fakeindex += 1
                data = convert.encode(playerdict).encode('ascii')
                conn.sendall(data)
