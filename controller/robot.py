sim = False
try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
except ModuleNotFoundError:
    print("This module will run in sim mode.")
    sim = True


class Motor:
    def __init__(self, label: str, forward_pin: int, reverse_pin: int):
        self.label = label
        self.reverse_pin = reverse_pin
        self.forward_pin = forward_pin

    def gpio_setup(self):
        if sim is False:
            GPIO.setup((self.forward_pin, self.reverse_pin), GPIO.OUT)
        else:
            print("Setup GPIO pin" + str((self.forward_pin, self.reverse_pin)))

    def r_forward(self):
        if sim is False:
            GPIO.output(self.reverse_pin, False)
            GPIO.output(self.forward_pin, True)
        else:
            print("Motor {0} running forward on pin {1}".format(self.label, self.forward_pin))

    def r_reverse(self):
        if sim is False:
            GPIO.output(self.forward_pin, False)
            GPIO.output(self.reverse_pin, True)
        else:
            print("Motor {0} running reverse on pin {1}".format(self.label, self.reverse_pin))

    def r_stop(self):
        if sim is False:
            GPIO.output(self.reverse_pin, False)
            GPIO.output(self.forward_pin, False)
        else:
            print("Motor {0} stopped".format(self.label))


class Robot:
    def __init__(self, name, l_motor: Motor, r_motor: Motor):
        self.name = name
        self.l_motor = l_motor
        self.r_motor = r_motor

    def r_forward(self):
        self.l_motor.r_forward()
        self.r_motor.r_forward()
        if sim is True:
            print("moving forward")

    def r_reverse(self):
        self.l_motor.r_reverse()
        self.r_motor.r_reverse()
        if sim is True:
            print("moving reverse")

    def r_right(self):
        self.l_motor.r_forward()
        self.r_motor.r_reverse()
        if sim is True:
            print("moving right")

    def r_left(self):
        self.l_motor.r_reverse()
        self.r_motor.r_forward()
        if sim is True:
            print("moving left")

    def halt(self):
        self.l_motor.r_stop()
        self.r_motor.r_stop()
        if sim is True:
            print("halt")

    def quit(self):
        self.halt()
        if sim is False:
            GPIO.cleanup()
        else:
            print("quit")
        quit(0)
