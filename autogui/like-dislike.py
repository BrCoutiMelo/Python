#Achar as posições
import pyautogui
import time

time.sleep(5)
pyautogui.position()

###########################

import pyautogui as pa
import time
import pyperclip as pc

pa.PAUSE = 5

print("Insira o Link do video do Youtube: ")
link = input()

print("ESCOLHA UMA DAS OPÇÕES")
op1 = int(input("Para dar LIKE no vídeo digite 1, para dar DISLIKE digite 2\n"))

if op1 == 1:
    pa.hotkey("ctrl","t")
    pc.copy(link)
    pa.hotkey("ctrl", "v")
    pa.hotkey("enter")
    time.sleep(3)
    pa.click(x=879, y=968)
    
elif op1 == 2:
    pa.hotkey("ctrl","t")
    pc.copy(link)
    pa.hotkey("ctrl", "v")
    pa.hotkey("enter")
    time.sleep(3)
    pa.click(x=959, y=960)
    

#POSIÇÃO DOS LIKES:x=879, y=968
#POSIÇÃO DO DISLIKE:x=959, y=960
