import pygame
import socket

def welcome():
    print("\n\t~~~~~~~~~~ WELCOME TO ONLINE MULTIPLAYER GAME ~~~~~~~~~~")
    print("Move your square with arrow keys and see the other player move in real-time!\n")

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "127.0.0.1"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(1024).decode()

    def send(self, data):
        self.client.send(str.encode(data))
        return self.client.recv(1024).decode()

def parse_position(pos_str):
    x, y = map(int, pos_str.split(','))
    return x, y

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Multiplayer Game")
    clock = pygame.time.Clock()

    n = Network()
    x, y = parse_position(n.pos)
    other_x, other_y = 0, 0
    run = True

    while run:
        clock.tick(60)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: x -= 5
        if keys[pygame.K_RIGHT]: x += 5
        if keys[pygame.K_UP]: y -= 5
        if keys[pygame.K_DOWN]: y += 5

        pos_str = f"{x},{y}"
        try:
            other_x, other_y = parse_position(n.send(pos_str))
        except:
            print("Disconnected from server")
            run = False

        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 255), (x, y, 50, 50))        # You
        pygame.draw.rect(screen, (255, 0, 0), (other_x, other_y, 50, 50))  # Opponent
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

# Loop to allow replays
while True:
    welcome()
    main()
    again = input("Play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Goodbye!")
        break
