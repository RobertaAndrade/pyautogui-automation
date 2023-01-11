# p1: entrar no sistema da empresa (link)
# p2: navegar até o  local do relatório (pasta exp)
# p3: exportar o relatório (download)
# p4: calcular os indicadores (faturam. e quant. de prod)

# pyautogui.click 
# pyautogui.write
# pyautogui.press 
# pyautogui.hotkey

# print(pyautogui.position())
 
import pyautogui
import pyperclip 

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True 

pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")

pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter") 

import time 

time.sleep(5)
pyautogui.click(x=332, y=312, clicks=2)
time.sleep(2)

pyautogui.click(x=413, y=372)
pyautogui.click(x=1127, y=192)
pyautogui.click(x=972, y=585)
time.sleep(5)
pyautogui.click(x=505, y=430)
time.sleep(5)

import pandas as pd

tabela = pd.read_excel(r"C:\Users\Ronnie\Desktop\roberta\aut\Vendas - Dez.xlsx")

faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()
print(faturamento, quantidade)