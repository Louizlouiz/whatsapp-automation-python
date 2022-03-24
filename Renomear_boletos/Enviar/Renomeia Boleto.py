from cgitb import enable
from configparser import LegacyInterpolation
from faulthandler import disable
import os
from tkinter import *
from tkinter import filedialog
import PyPDF2
import pyautogui as pt
from time import sleep
from datetime import date
from pynput.keyboard import Controller



def envia_boleto(nome='luis', caminho='D:\OneDrive\Edem\Boletos', mes ='esse m^es'):

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
    sleep(5)
    pt.doubleClick()
    while True:
        if pt.locateOnScreen('Renomear_boletos/image/emote_clip.png', confidence = .8):
            pos = pt.locateOnScreen('Renomear_boletos/image/emote_clip.png', confidence = .8)
            break
        else:
            sleep(.5)
    x = pos[0]
    y = pos[1]
    pt.moveTo(x, y, duration=.2)
    pt.moveRel(200,25,duration=.2)
    pt.tripleClick()
    Controller().type(f'Oi, tudo bom?\nSege o seu boleto do colégio EDEM referente a {mes}')
    pt.moveRel(-80,0,duration=.2)
    pt.click()
 
    while True:
        if pt.locateOnScreen('Renomear_boletos/image/doc.png', confidence = .8):
            pos = pt.locateOnScreen('Renomear_boletos/image/doc.png', confidence = .8)
            break
        else:
            sleep(.5)

    x = pos[0]
    y = pos[1]
    pt.moveTo(x, y, duration=.2)
    pt.moveRel(20, 20, duration=.2)
    pt.click()

    while True:
        if pt.locateOnScreen('Renomear_boletos/image/arq.png', confidence = .8):
            pos = pt.locateOnScreen('Renomear_boletos/image/arq.png', confidence = .8)
            break
        else:
            sleep(.5)

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
    #pt.press('enter')
    #pt.press('enter')

def novo_nome(path):
    endpdf = open(path, 'rb')
    leitor = PyPDF2.PdfFileReader(endpdf)
    pagina_um = leitor.getPage(0)
    texto = pagina_um.extractText()
    pos_name = texto.find('Turma:') + 7
    nome_aluno = texto[pos_name:]
    pos_slash = nome_aluno.find('/') -1
    endpdf.close()
    return nome_aluno[:pos_slash]

def enviar_todos ():
    for nome in lista_nomes:
        envia_boleto(nome, caminho, mes)
        break


def def_caminho():
    global caminho, lista_nomes, mes
    lista_nomes = list()
    caminho = filedialog.askdirectory()
    for i in os.listdir(caminho):
        caminho_arq = f'{caminho}/{i}'
        try:
            nome_aluno = novo_nome(caminho_arq)
            novo_caminho = f'{caminho}/{nome_aluno}.pdf'
            os.rename(caminho_arq,novo_caminho)
            lista_nomes.append(nome_aluno)
        except:
            continue    
    
    lbl_2 = Label(root, text="Sucesso!")
    lbl_2.pack()
    
    meses=('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
    mes = meses[date.today().month-1]

    bt_2 = Button(root, text='Enviar', padx = 50, command = enviar_todos)
    bt_2.pack()      

root = Tk()
root.title('Renomear Boleto para nome do aluno')
root.resizable(False,False)
root.geometry('300x150')

lbl_1 = Label(root, text='Escolha a pasta dos Boletos.')
lbl_1.pack()
bt_1 = Button(root, text='Pesquisar e Renomear', padx = 50, command = def_caminho)
bt_1.pack()




root.mainloop()