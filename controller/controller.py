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
                data = str(data.decode("UTF-8"))
                # print("command {0} from {1}".format(data, addr[0]))
                if data == "quit":
                    self.dt.quit()
                    break
                if data == "forward":
                    self.dt.r_forward()
                if data == "reverse":
                    self.dt.r_reverse()
                if data == "right":
                    self.dt.r_right()
                if data == "left":
                    self.dt.r_left()
                if data == "halt":
                    self.dt.halt()
        finally:
            self.dt.quit()
