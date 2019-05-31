import socket
import robot


class Controller:
    def __init__(self, target_ip: str, target_port: int, dt: robot.Robot):
        self.target_ip = target_ip
        self.target_port = target_port
        self.sock = socket.socket(socket.AF_INET,  # Internet
                                  socket.SOCK_DGRAM)  # UDP
        self.sock.bind((self.target_ip, self.target_port))
        self.dt = dt

    def drive(self):
        try:
            while True:
                data, addr = self.sock.recvfrom(1024)  # buffer size is 1024 bytes
                data = data.decode("UTF-8")
                if data is "quit":
                    self.dt.quit()
                    break
                if data is "forward":
                    self.dt.r_forward()
                if data is "reverse":
                    self.dt.r_reverse()
                if data is "right":
                    self.dt.r_right()
                if data is "left":
                    self.dt.r_left()
                if data is "halt":
                    self.dt.halt()
        finally:
            self.dt.quit()
