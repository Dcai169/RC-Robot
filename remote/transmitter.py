import socket


class Transmitter:
    def __init__(self, target_ip: str, target_port: int):
        self.target_ip = target_ip
        self.target_port = target_port
        self.sock = socket.socket(socket.AF_INET,  # Internet
                                  socket.SOCK_DGRAM)  # UDP

    def send(self, message) -> None:
        self.sock.sendto(bytes(str(message), encoding="UTF-8"), (self.target_ip, self.target_port))
