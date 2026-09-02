import sys
import time

def printLyrics():
    lines = [
        ("Nandito akoooo", 0.20),
        ("Umiibig sayooo", 0.18),
        ("Kahit naaa", 0.10),
        ("Nagdurugo ang pusooooo", 0.18),
        ("At kung sakaling", 0.09),
        ("Iwanan ka nyaaaaaaa", 0.19),
        ("Wag kang mag-alala", 0.18),
        ("May nagmamahal sayooo", 0.15),
        ("Nandito akoooooooooooo ohhh ohhh ohhh", 0.20),
        ("sakit mo naman", 0.15),
    ]

    delays = [0.9, 0.8, 1, 1.5, 1, 0.17, 0.14, 0.8, 0.10, 0.20]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            sys.stdout.write(ORANGE + char + RESET)
            sys.stdout.flush()
            time.sleep(char_delay)
        print()
        time.sleep(delays[i])













GOLD = "\033[33m"
ORANGE = "\033[38;5;208m"
RESET = "\033[0m"

if __name__ == "__main__":
    printLyrics()