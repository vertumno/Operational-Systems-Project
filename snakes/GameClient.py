import curses
import time
import sys
import threading
import socket
import pickle
from random import randint
from Snake import Snake
from Field import Field

serverAddress = (socket.gethostname(), 5010)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bufferSize = 8192
field = None

def main(screen):
    screen.timeout(0)

    player_name = sys.argv[1]
    player = Snake(player_name)
    playerBytes = pickle.dumps(player)

    #send new player to the game
    clientSocket.connect(serverAddress)
    clientSocket.sendall(playerBytes)

    #handle the player moves
    while True:
        ch = screen.getch()
        if ch == ord('q'):
            break
        elif ch != -1:
            clientSocket.sendall(pickle.dumps(ch))

        dataBytes = clientSocket.recv(bufferSize)
        if dataBytes:
            data = pickle.loads(dataBytes)
            if data == 'CLOSE':
                screen.refresh()
                screen.addstr(field.size, 0, "disconnected by server", curses.A_BOLD)
                field = None
            else:
                field = data

        if field:
            screen.refresh()
            field.render(screen)
            time.sleep(.4)

    clientSocket.shutdown(2)
    clientSocket.close()

def gameThread():
    if (len(sys.argv) != 2):
        print("Usage: python {} [player name]".format(sys.argv[0]))
    else:
        curses.wrapper(main)

if __name__=='__main__':
    gt = threading.Thread(target=gameThread)
    gt.start()
