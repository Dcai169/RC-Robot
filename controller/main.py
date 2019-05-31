import controller
import robot

if __name__ == "__main__":
    left_motor = robot.Motor("L", 27, 22)
    right_motor = robot.Motor("R", 23, 24)
    r = robot.Robot("Banner", left_motor, right_motor)
    c = controller.Controller("127.0.0.1", 5005, r)
    c.drive()
