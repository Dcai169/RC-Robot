import transmitter
import keyboard


if __name__ == "__main__":
    tx = transmitter.Transmitter("127.0.0.1", 5005)
    kb = keyboard.KeyboardInter(tx)
    kb.listen()
