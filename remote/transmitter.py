import socket


class Transmitter:
    def __init__(self, target_ip: str, target_port: int):
        self.target_ip = target_ip
        self.target_port = target_port
        self.sock = socket.socket(socket.AF_INET,  # Internet
                                  socket.SOCK_DGRAM)  # UDP

    def send(self, message):
        self.sock.sendto(bytes(str(message), encoding="UTF-8"), (self.target_ip, self.target_port))
        # print("Message {0} sent to IP {1} on Port {2}".format(message, self.target_ip, self.target_port))
