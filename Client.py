import socket
import threading

class Client:
    def __init__(self, host='127.0.0.1', port=5005):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        self.ping = True   # <-- Boolean attribute to indicate active status
        print("[CONNECTED] Connected to server.")

    def receive_messages(self):
        while self.ping:   # Only listen if still active
            try:
                msg = self.client_socket.recv(2048).decode('utf-8')
                if msg:
                    print(f"\n[CHAT] {msg}")
            except:
                print("[ERROR] Connection lost.")
                self.ping = False
                break

    def send_messages(self):
        while self.ping:
            msg = input("")
            if msg.lower() == "quit":
                self.ping = False
                self.client_socket.close()
                break
            self.client_socket.send(msg.encode('utf-8'))

    def run(self):
        thread = threading.Thread(target=self.receive_messages)
        thread.start()
        self.send_messages()