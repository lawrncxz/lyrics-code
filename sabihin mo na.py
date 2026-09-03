import time
import sys

print("\n\n")

lyrics = [
    ("Sabihin mo naaa", 1.13, 0.10),
    ("Kung anong gusto mooo", 1.13, 0.10),
    ("Kahit ano'y gagawin",  1.15, 0.18),
    ("Para lamang sayooo",  1.13, 0.10),
    ("Sabihin na naaaa", 1.13, 0.10),
    ("Kung papaano mooo", 1.13, 0.13),
    ("Mapapatawad......",1.13, 0.13 ),
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
        time.sleep(line_delay)
        type_out(line, char_delay)


if __name__ == "__main__":
    play_lyrics(lyrics)