import time 
import os

lyrics =[
    "Pwede bang pag-isipan huwag ka munang lumiban ",
    "Baka sakali na ito ay maisalba pa",
    "Lumalamig abg gabi",
    "Hindi na tulad ng dati ",
    "May pag asa pa ba kung susuko ka na",
    "Larawan mo ba'y lulukutin ko na",
    "Sa hirap at ginhawa tayo ay nagsama",
    "Damdamin mo tilay napagod na",
    "Ikaw at ako ay alaala na lang kung susuko ka na",  
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