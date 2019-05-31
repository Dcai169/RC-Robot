import curses
import transmitter


class KeyboardInter:
    # Get the curses window, turn off echoing of keyboard to screen, turn on
    # instant (no waiting) key response, and use special values for cursor keys
    def __init__(self, tx: transmitter.Transmitter) -> None:
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)
        self.tx = tx

    def listen(self) -> None:
        try:
            while True:
                char = self.screen.getch()
                if char == ord('q'):
                    self.tx.send("quit")
                    break
                elif char == curses.KEY_UP or char == ord("w"):
                    self.tx.send("forward")
                elif char == curses.KEY_DOWN or char == ord("s"):
                    self.tx.send("reverse")
                elif char == curses.KEY_RIGHT or char == ord("a"):
                    self.tx.send("right")
                elif char == curses.KEY_LEFT or char == ord("d"):
                    self.tx.send("left")
                elif char == 10 or char == ord(" "):
                    self.tx.send("halt")

        finally:
            # Close down curses properly, inc turn echo back on!
            curses.nocbreak()
            self.screen.keypad(0)
            curses.echo()
            curses.endwin()
