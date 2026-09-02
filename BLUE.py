import time 
import os

lyrics =[
    
    "Know you're all that i want this life",
    "",
    "I'll imagine we fell in love",
    "I'll nap under moonlight skies with you",
    "I think i'll picture us, you with the waves",
    "The ocean's colors on your face",
    "I'll leave my heart with you air",
    "So let me fly with you",
    "Will you be forever with me",   
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_lyrics(lyrics):
    clear_screen()
    print("=earrlliee=\n")
    for line in lyrics:
        for char in line:
            print(char, end='', flush= True)
            time.sleep(0.09)
        print()
        time.sleep(1.2)

if __name__ == "__main__":
    display_lyrics(lyrics)