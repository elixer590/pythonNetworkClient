# demo server app?
# in this we need to test creating a socket and talking to it

import socket
import convertEncodedAscii as convert
import _thread

class gameState:
    def __init__(self):
        self.fakePlayerID = 13337
        self.moves = [(160, 192),(128, 192),(96, 192),(96, 160),(96, 192),(128, 192)]
        self.fakeindex = 0
        self.playerdict = {}

def clientHandler(_conn, _addr, _state):
    with _conn:
            print('Connected by', _addr)
            while True:
                data = _conn.recv(1024)
                if not data:
                    break
                _state.playerdict[_addr[1]] = data.decode('ascii')
                _state.playerdict[_state.fakePlayerID] = str(_state.moves[_state.fakeindex % len(_state.moves)])
                _state.fakeindex += 1
                data = convert.encode(_state.playerdict).encode('ascii')
                _conn.sendall(data)

  

# setup some constants that we will use later
HOST = '127.0.0.1'
PORT = 1337

state = gameState()  # Using this to keep game state information synchronized between threads

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
        print('i am about to set port tolisten')
        s.listen()
        print('i am waiting on a connection')
        conn, addr = s.accept()
        print('connection received')
        _thread.start_new_thread(clientHandler,(conn, addr, state)) #this is one I need to learn
