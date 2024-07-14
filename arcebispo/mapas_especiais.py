import pydirectinput
import pyautogui
import time
import win32api, win32con
import habilidades

i = 0
mover = True

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def doubleClick():
    leftClick()
    time.sleep(0.1)
    leftClick()
    
def curar():
    print('Selecionando Feitiço Cura')
    pyautogui.moveTo(701 , 17, 1)
    time.sleep(1)
    doubleClick()

    print('Disparando Feitiço Cura')
    pyautogui.moveTo(803 , 445, 1)
    leftClick()
    
# def ganancia():
#     print('Disparando Feitiço Ganancia')
#     pyautogui.moveTo(703 , 82, 1)
#     time.sleep(1)
#     doubleClick()
    
def kyrieEleison():
    print('Selecionando Feitiço Kyrie Eleison')
    pyautogui.moveTo(791 , 18, 1)
    time.sleep(1)
    doubleClick()

    print('Disparando Feitiço Kyrie Eleison')
    pyautogui.moveTo(803 , 445, 1)
    leftClick()
    
# def magnusExorcismus():
#     print('Selecionando Feitiço Magnus Exorcismus')
#     pyautogui.moveTo(673 , 17, 1)
#     time.sleep(1)
#     doubleClick()

#     time.sleep(1)

#     print('Disparando Feitiço Magnus Exorcismus')
#     pyautogui.moveTo(803 , 445, 1)
#     leftClick()
    
def moverDireita():
    print('Movendo p/ Direita')
    pyautogui.moveTo(1200 , 445, 1)
    leftClick()
    return False

def moverEsquerda():
    print('Movendo p/ Esquerda')
    pyautogui.moveTo(400 , 445, 1)
    leftClick()
    return True


while i < 400:
    print('==== Iniciando ciclo ====')
    
    habilidades.magnusExorcismus()

    # time.sleep(1)

    # curar()

    time.sleep(7.5)

    # kyrieEleison()

    # time.sleep(1)
    
    habilidades.ganancia()
    
    # time.sleep(0.5)
    
    # if mover == True:
    #     mover = moverDireita()
    # else:
    #     mover = moverEsquerda()
    
    i += 1

    print('==== Fim do ciclo ' + str(i) + ' ==== \n')