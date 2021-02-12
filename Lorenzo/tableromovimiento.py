from time import sleep
import os
from pynput.keyboard import Listener
clear = lambda: os.system('cls')

lista = []
for i in range(5):
    lista.append([])
    for a in range(14):
        lista[i].append('          ')


posx = 1
posy = 2

lista[posx][posy] = '    O     '

def busqueda():
    damela = 0
    for i in range(13):
        if lista[2][i] == '    O     ':
            damela = i

    return damela

def key_recorder(key):
    global posx
    global posy
    global lista

    
    key = str(key).replace("'", "")
    
    if key == 'Key.right' and posy != 13:

        if lista[3][3] ==  '    O     ':
            posx = 3
            posy = 3
        elif lista[4][6] ==  '    O     ':
            posx = 4
            posy = 6
        else:
            lista[posx][posy],lista[posx][posy+1] = lista[posx][posy+1],lista[posx][posy]
            posy = posy + 1
        if posy >= 13:
            posy = 13
            
    elif key == 'Key.left' and posy != 0:
        if lista[1][1] ==  '    O     ':
            posx = 0
            posy = 0
            lista[1][1] = '          ' 
            lista[0][0] = '    O     '
        elif lista[2][1] == '    O     ':
            posx = 0
            posy = 0
            lista[2][1] = '          ' 
            lista[0][0] = '    O     '
        elif lista[3][1] ==  '    O     ':
            posx = 3
            posy = 1
        elif lista[4][1] ==  '    O     ':
            posx = 4
            posy = 1
        else:
             lista[posx][posy],lista[posx][posy-1] = lista[posx][posy-1],lista[posx][posy]
             posy = posy - 1
        if posy <= 0:
            posy = 0

            
    elif key == 'Key.down' and posx != 4:
        posy_2 = busqueda()
        if lista[2][1] ==  '    O     ' or lista[2][2] ==  '    O     ' or lista[2][3] ==  '    O     ' or lista[2][4] ==  '    O     ':
            posx = 3
            posy = 1
            lista[2][posy_2] = '          ' 
            lista[3][1] = '    O     '
        elif lista[2][5] ==  '    O     ' or lista[2][6] ==  '    O     ' or lista[2][7] ==  '    O     ' or lista[2][8] ==  '    O     ':
            posx = 3
            posy = 2
            lista[2][posy_2] = '          ' 
            lista[3][2] = '    O     '
        elif lista[2][9] ==  '    O     ' or lista[2][10] ==  '    O     ' or lista[2][11] ==  '    O     ' or lista[2][12] ==  '    O     ':
            posx = 3
            posy = 3
            lista[2][posy_2] = '          ' 
            lista[3][3] = '    O     '
        elif lista[3][2] ==  '    O     ':
            posx = 4
            posy = 3
            lista[3][2] = '          ' 
            lista[4][3] = '    O     '
        elif lista[3][3] ==  '    O     ':
            posx = 4
            posy = 5
            lista[3][3] = '          ' 
            lista[4][5] = '    O     '
        elif lista[0][0] ==  '    O     ':
            posx = 0
            posy = 0
        elif lista[2][13] ==  '    O     ':
            posx = 2
            posy = 13
        else:
            lista[posx][posy],lista[posx+1][posy] = lista[posx+1][posy],lista[posx][posy]
            posx = posx + 1
        if posx >= 4:
            posx = 4

    elif key == 'Key.up' and posx != 0:

        if lista[3][2] ==  '    O     ':
            posx = 2
            posy = 6
            lista[3][2] = '          ' 
            lista[2][6] = '    O     '
        elif lista[3][3] ==  '    O     ':
            posx = 2
            posy = 10
            lista[3][3] = '          ' 
            lista[2][10] = '    O     '
        elif lista[4][2] ==  '    O     ':
            posx = 3
            posy = 1
            lista[4][2] = '          ' 
            lista[3][1] = '    O     '
        elif lista[4][3] ==  '    O     ':
            posx = 3
            posy = 2
            lista[4][3] = '          ' 
            lista[3][2] = '    O     '
        elif lista[4][4] ==  '    O     ':
            posx = 3
            posy = 2
            lista[4][4] = '          ' 
            lista[3][2] = '    O     '
        elif lista[4][5] ==  '    O     ':
            posx = 3
            posy = 3
            lista[4][5] = '          ' 
            lista[3][3] = '    O     '
        elif lista[4][6] ==  '    O     ':
            posx = 3
            posy = 3
            lista[4][6] = '          ' 
            lista[3][3] = '    O     '
        else:    
            lista[posx][posy],lista[posx-1][posy] = lista[posx-1][posy],lista[posx][posy]
            posx = posx - 1
        if posx <= 0:
            posx = 0
    

    l.stop()

def display():
    print('''

╔══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╗
║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║
║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║
║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║
║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║
║          ║'''+lista[0][1]+'''║'''+lista[0][2]+'''║'''+lista[0][3]+'''║'''+lista[0][4]+'''║'''+lista[0][5]+'''║'''+lista[0][6]+'''║'''+lista[0][7]+'''║'''+lista[0][8]+'''║'''+lista[0][9]+'''║'''+lista[0][10]+'''║'''+lista[0][11]+'''║'''+lista[0][12]+'''║'''+lista[0][13]+'''║
║          ╠══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╣
║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║
║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║
║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║
║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║
║          ║'''+lista[1][1]+'''║'''+lista[1][2]+'''║'''+lista[1][3]+'''║'''+lista[1][4]+'''║'''+lista[1][5]+'''║'''+lista[1][6]+'''║'''+lista[1][7]+'''║'''+lista[1][8]+'''║'''+lista[1][9]+'''║'''+lista[1][10]+'''║'''+lista[1][11]+'''║'''+lista[1][12]+'''║'''+lista[1][13]+'''║
║          ╠══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╣
║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║
║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║
║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║
║'''+lista[0][0]+'''║'''+lista[2][1]+'''║'''+lista[2][2]+'''║'''+lista[2][3]+'''║'''+lista[2][4]+'''║'''+lista[2][5]+'''║'''+lista[2][6]+'''║'''+lista[2][7]+'''║'''+lista[2][8]+'''║'''+lista[2][9]+'''║'''+lista[2][10]+'''║'''+lista[2][11]+'''║'''+lista[2][12]+'''║'''+lista[2][13]+'''║
║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║
╚══════════╬══════════╩══════════╩══════════╩══════════╬══════════╩══════════╩══════════╩══════════╬══════════╩══════════╩══════════╩══════════╬══════════╝
           ║                                           ║                                           ║                                           ║
           ║                                           ║                                           ║                                           ║
           ║                                           ║                                           ║                                           ║
           ║                                           ║                                           ║                                           ║
           ║                               '''+lista[3][1]+'''  ║                               '''+lista[3][2]+'''  ║                               '''+lista[3][3]+'''  ║
           ╠═════════════════════╦═════════════════════╬═════════════════════╦═════════════════════╬═════════════════════╦═════════════════════╣
           ║                     ║                     ║                     ║                     ║                     ║                     ║
           ║                     ║                     ║                     ║                     ║                     ║                     ║
           ║                     ║                     ║                     ║                     ║                     ║                     ║
           ║                     ║                     ║                     ║                     ║                     ║                     ║
           ║           '''+lista[4][1]+'''║           '''+lista[4][2]+'''║           '''+lista[4][3]+'''║           '''+lista[4][4]+'''║           '''+lista[4][5]+'''║           '''+lista[4][6]+'''║
           ╚═════════════════════╩═════════════════════╩═════════════════════╩═════════════════════╩═════════════════════╩═════════════════════╝
''')


while True:
    clear()
    for i in lista:
        print(i)
    display()
    print(busqueda())
    posy_2 = busqueda()
    print(posy_2)
    with Listener(on_press=key_recorder) as l:
        l.join()

