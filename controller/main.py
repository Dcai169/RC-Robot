import controller
import robot

if __name__ == "__main__":
    left_motor = robot.Motor("L", 22, 24)
    right_motor = robot.Motor("R", 36, 38)
    r = robot.Robot("Banner", left_motor, right_motor)
    c = controller.Controller("192.168.29.122", 5005, r)
    c.drive()
