"""
beep
echo stdin
beep n times
"""

import sys
import termios
import tty

# save state of tty
tty_attrs = termios.tcgetattr(0)
tty.setcbreak(0)  # removes echo in terminal, so you don't see it


def run():
    while True:
        ch = sys.stdin.read(1)  # read 1 character from the input
        if 1 <= int(ch) <= 9:
            for _ in range(int(ch)):
                sys.stdout.buffer.write(b"\x07")
        sys.stdout.buffer.flush()


try:
    run()
finally:
    termios.tcsetattr(0, termios.TCSADRAIN, tty_attrs)
