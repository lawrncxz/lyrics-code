import threading
import time

lock = threading.Lock()

lyrics = [
    ("Isang himala na lang", 0, 150),
    ("Kung mapapasa 'kin ka", 4000, 160),
    ("Parang panaginip", 13000, 160),
    ("Pag ika'y aking kapiling", 19000, 150),
    ("Huwag kang tumingin sa 'kin", 26000, 150),
    ("Ako ay nahuhumaling", 33500, 160),
    ("Ako ay nahuhumaling", 40000, 160),
    ("Sa 'yo", 48000, 180),
    ("Sa 'yo", 50000, 180),
    ("Sa 'yo", 52000, 200),
]

def animate_text(text: str, delay_per_char: int):
    with lock:
        for char in text:
            print(char, end="", flush=True)
            time.sleep(delay_per_char / 1000)
        print()

def play_lyrics():
    start_time = time.time()

    for text, start_delay, char_delay in lyrics:
        while (time.time() - start_time) * 1000 < start_delay:
            time.sleep(0.01)

        animate_text(text, char_delay)

if __name__ == "__main__":
    play_lyrics()