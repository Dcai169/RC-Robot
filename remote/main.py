import transmitter
import keyboard


if __name__ == "__main__":
    tx = transmitter.Transmitter("192.168.29.122", 5005)
    kb = keyboard.KeyboardInter(tx)
    kb.listen()
