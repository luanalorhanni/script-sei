import pyautogui
import time
import pandas as pd

tabela = pd.read_csv("produtos.csv")

pyautogui.PAUSE = 0.5 #Dá uma pausa ENTRE AS LINHAS DO CODIGO em segundos

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=580, y=856) #Selecionar o usuário do Chrome
pyautogui.write("https://sip.saoluis.ma.gov.br/sip/login.php?sigla_orgao_sistema=PMSL&sigla_sistema=SIP")
pyautogui.press("enter")

time.sleep(3) #Vai fazer uma pausa entre CÓDIGO

pyautogui.click(x=768, y=375) #Colocar a posição em x e y com pyautogui.position()
pyautogui.write("estudosllps@gmail.com")
pyautogui.press("tab") 
pyautogui.write("Laila100%")

#Faz o login
pyautogui.press("tab")
pyautogui.press("enter")

for linha in tabela.index: #Manipulação dos dados e preenchimento automatico do formulário
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    obs = tabela.loc[linha, "obs"]
    
    #Preenchimento do campo código
    pyautogui.click(x=699, y=267)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    
    #Preenchimento do campo marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")  
    
    #Preenchimento do campo tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")  
    
    #Preenchimento do campo categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab") 
    
    #Preenchimento do campo Preco UnitariHashtago
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")  
 
    #Preenchimento do campo Custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")  
    
    #Preenchimento do campo Observações
    pyautogui.write(str(tabela.loc[linha, "obs"]))

    #Envio dos dados do formulário 
    pyautogui.press("tab") 
    
    pyautogui.doubleClick(x=875, y=912) 

    


    
    