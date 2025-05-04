import socket
import _thread

server = "127.0.0.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))

s.listen()
print("[SERVER] Waiting for connections...")

positions = [(50, 50), (100, 100)]

def handle_client(conn, player):
    conn.send(str.encode(str(positions[player])))
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            x, y = map(int, data.split(','))
            positions[player] = (x, y)
            other_player = 1 - player
            reply = str(positions[other_player])
            conn.sendall(str.encode(reply))
        except:
            break

    print(f"[DISCONNECT] Player {player} disconnected.")
    conn.close()

player_count = 0
while True:
    conn, addr = s.accept()
    print(f"[NEW CONNECTION] {addr}")
    _thread.start_new_thread(handle_client, (conn, player_count))
    player_count += 1
