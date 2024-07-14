import pyautogui
import time
import eventos

def magnusExorcismus():
    print('Selecionando Feitiço Magnus Exorcismus')
    pyautogui.moveTo(673 , 17, 1)
    time.sleep(1)
    eventos.doubleClick()

    time.sleep(1)

    print('Disparando Feitiço Magnus Exorcismus')
    pyautogui.moveTo(803 , 445, 1)
    eventos.leftClick()
    
def ganancia():
    print('Disparando Feitiço Ganancia')
    pyautogui.moveTo(703 , 82, 1)
    time.sleep(1)
    eventos.doubleClick()