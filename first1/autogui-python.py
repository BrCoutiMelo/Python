import pyautogui as pa
import time

#pa.PAUSE(1)//
#DANDO LIKE EM UM VIDEO DO YOUTUBE AUTO
#Obs: O video está com o formato "teatro", portanto a posição do 'click' é diferente, e varia conforme o formato.

pa.hotkey("ctrl", "t")
time.sleep(3)
pa.write("https://youtu.be/gZTTP9oeCe0")
time.sleep(5)
pa.hotkey("enter")
time.sleep(7)
pa.click(x=907, y=975)
