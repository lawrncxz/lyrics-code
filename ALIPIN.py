import time
import sys

print("\n\n")

lyrics = [
    ("Akoy alipin mo kahit hindi batid", 1.60, 0.13),
    ("Aaminin kong minsan ako'y manhid", 2.0, 0.15),
    ("Sana ay iyong naririnig...", 2.1, 0.18),
    ("Sa'iyong yakap ako'y nasasabik", 0.7, 0.15),
]
 
def type_out(text, char_delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def play_lyrics(lyrics):
    for line, line_delay, char_delay in lyrics:
        type_out(line, char_delay)
        time.sleep(line_delay)

if __name__ == "__main__":
    play_lyrics(lyrics)
        