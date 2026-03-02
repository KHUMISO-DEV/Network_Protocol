import socket
import threading

class Server:
    def __init__(self, host='127.0.0.1', port=5005):
        self.host = host
        self.port = port
        self.clients = {}  # store {conn: ping_status}
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"[SERVER STARTED] Listening on {self.host}:{self.port}")

    def broadcast(self, message, sender_conn):
        for client_conn, ping in list(self.clients.items()):
            if client_conn != sender_conn and ping:
                try:
                    client_conn.send(message.encode('utf-8'))
                except:
                    self.clients[client_conn] = False  # mark inactive

    def handle_client(self, conn, addr):
        print(f"[CONNECTION]: {addr} .")
        self.clients[conn] = True  # mark as active
        while self.clients[conn]:
            try:
                msg = conn.recv(2048).decode('utf-8')
                if not msg:
                    break
                print(f"[{addr}] {msg}")
                self.broadcast(msg, conn)
            except:
                break
        conn.close()
        self.clients[conn] = False
        print(f"[DISCONNECTED]: {addr}")

    def run(self):
        while True:
            conn, addr = self.server_socket.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()