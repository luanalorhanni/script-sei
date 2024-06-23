import pyautogui
import time
import pandas as pd

tabela = pd.read_csv("semus.csv", encoding='utf-8', delimiter=",")

pyautogui.PAUSE = 1.5 #Dá uma pausa ENTRE AS LINHAS DO CODIGO em segundos

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
    # pyautogui.keyDown('win')
    # pyautogui.press('up')
    # pyautogui.keyUp('win')

time.sleep(1)
pyautogui.write("https://sip.saoluis.ma.gov.br/")
pyautogui.press("enter")

time.sleep(1) #Vai fazer uma pausa entre CÓDIGO

#Login SIP
# pyautogui.write("teste")
# pyautogui.press("tab") 
# pyautogui.write("teste")
# pyautogui.press("tab")
# pyautogui.press("enter")
pyautogui.doubleClick(x=863, y=497)
pyautogui.press("tab")
pyautogui.press("enter")

pyautogui.click(x=256, y=618)
pyautogui.press("tab")
pyautogui.press("enter")
#pyautogui.write("SEMU")
#pyautogui.press("enter")
#pyautogui.press("tab")
pyautogui.press("tab")

for linha in tabela.index: #Manipulação dos dados e preenchimento automatico do formulário
    sigla = tabela.loc[linha, "SIGLA"]
    descricao = tabela.loc[linha, "DESCRIÇÃO"]
        
    #pyautogui.click(x=564, y=347)
    pyautogui.write(str(tabela.loc[linha, "SIGLA"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "DESCRIÇÃO"]))
    #pyautogui.click(x=1742, y=227)
    
