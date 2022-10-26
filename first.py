
import time
import pyautogui as py
import json
import requests

#cotação do dolar

tela= py.size()
posicao = py.position()



py.moveTo(47, 1060)

time.sleep(1)
py.click(button= 'left')
time.sleep(2)
py.write('chrome')
py.press('enter')
time.sleep(1)
py.write('Dolar ')
py.press('enter')

