from re import I
import pyautogui as pt
from time import sleep
from pynput.keyboard import Controller


def get_message(nome='luis', caminho='D:\OneDrive\Edem\Boletos', mes ='esse mês'):

    if pt.locateOnScreen('Renomear_boletos/image/lupa.png', confidence = .6):
        pos = pt.locateOnScreen('Renomear_boletos/image/lupa.png', confidence = .6)
    else:
        pos = pt.locateOnScreen('Renomear_boletos/image/seta.png', confidence = .6)
    x = pos[0]
    y = pos[1]
    pt.moveTo(x, y, duration=.2)
    pt.moveRel(120,25, duration=.2)
    pt.tripleClick()
    pt.typewrite(nome, interval=.01)
    pt.moveRel(0, 190, duration=.2)
    pt.doubleClick()
    pos = pt.locateOnScreen('Renomear_boletos/image/emote_clip.png', confidence = .6)
    x = pos[0]
    y = pos[1]
    pt.moveTo(x, y, duration=.2)
    pt.moveRel(200,25,duration=.2)
    pt.tripleClick()
    sleep(.5)
    Controller().type(f'Oi, tudo bom? Sege o seu boleto do colégio EDEM referente a {mes}')
    sleep (.5)
    pt.moveRel(-80,0,duration=.2)
    pt.click()
    sleep(.25)
    while True:
        if pt.locateOnScreen('Renomear_boletos/image/doc.png', confidence = .8):
            pos = pt.locateOnScreen('Renomear_boletos/image/doc.png', confidence = .8)
            break
        else:
            sleep(.5)
            pt.click()
    x = pos[0]
    y = pos[1]
    pt.moveTo(x, y, duration=.2)
    pt.moveRel(20, 20, duration=.2)
    pt.click()
    sleep(1)
    pos = pt.locateOnScreen('Renomear_boletos/image/arq.png', confidence = .6)
    x = pos[0]
    y = pos[1]
    pt.moveTo(x, y, duration=.2)
    pt.moveRel(670,30,duration=.2)
    pt.click()
    pt.write(caminho)
    pt.press('enter')
    pt.moveRel(300,0,duration=.2)
    pt.click()
    sleep(1)
    pt.write(nome)
    sleep(1)
    pt.press('enter')
    pt.moveRel(-300,160,duration=2)
    pt.click()
    pt.press('enter')
    sleep(1)
    pt.press('enter')
    sleep(.5)
    pt.press('enter')

mes = 'março'
nome="luis"
caminho='D:\OneDrive\Edem\Boletos\Abril'
mensagem=f'Oi, tudo bom?\nSege o seu boleto do colégio EDEM de {mes}'
i= 0 
while i < 3:
    get_message(nome, caminho, mes)
    i +=1

