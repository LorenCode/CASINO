from time import sleep
import os
from pynput.keyboard import Listener
from colorama import init, Fore, Back, Style

clear = lambda: os.system('cls')

random = "1"

# Se crean las listas para almacenar el tablero
lista = []
for i in range(5):
    lista.append([])
    for a in range(14):
        lista[i].append('          ')

#Se crea la lista que contendra las apuestas
# l_fichas = []
# for i in range(49):
#     l_fichas.append(" ")

d_fichas = {}

for i in range(37):
    d_fichas[str(i)] = ""
d_fichas["2 to 1 1"] = ""
d_fichas["2 to 1 2"] = ""
d_fichas["2 to 1 3"] = ""
d_fichas["1rd 12"] = ""
d_fichas["2rd 12"] = ""
d_fichas["3rd 12"] = ""
d_fichas["1-18"] = ""
d_fichas["even"] = ""
d_fichas["rojo"] = ""
d_fichas["negro"] = ""
d_fichas["odd"] = ""
d_fichas["19-36"] = ""


#Posicion inicial del jugador
posx = 1
posy = 2

lista[posx][posy] = '    O     '

#Busca en la lista 2 la posición del jugador
def busqueda():
    damela = 0
    for i in range(13):
        if lista[2][i] == '    O     ':
            damela = i

    return damela

#Movimientos del jugador
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
    #MONEDAS
    #Apostar con la ficha de 5
    elif key == 'a':
        if d_fichas[b_posicion()] != "":
            d_fichas[b_posicion()] += 5
        else:
            d_fichas[b_posicion()] = 5  

    #Apostar con la ficha de 25
    elif key == 's':
        if d_fichas[b_posicion()] != "":
            d_fichas[b_posicion()] += 25
        else:
            d_fichas[b_posicion()] = 25

    #Apostar con la ficha de 50
    elif key == 'd':
        if d_fichas[b_posicion()] != "":
            d_fichas[b_posicion()] += 50
        else:
            d_fichas[b_posicion()] = 50
            
    l.stop()

#Tablero
def display():
    init()
    print('''

╔══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╗
║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║
║          ║'''+Back.RED+"3".center(10)+'''║'''+Back.BLACK+"6".center(10)+'''║'''+Back.RED+"9".center(10)+'''║'''+Back.BLACK+"12".center(10)+'''║'''+Back.RED+"15".center(10)+'''║'''+Back.BLACK+"18".center(10)+'''║'''+Back.RED+"21".center(10)+'''║'''+Back.BLACK+"24".center(10)+'''║'''+Back.RED+"27".center(10)+'''║'''+Back.BLACK+"30".center(10)+'''║'''+Back.RED+"33".center(10)+'''║'''+Back.BLACK+"36".center(10)+'''║'''+Back.GREEN+"2 to 1".center(10)+Back.BLACK+'''║
║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║
║          ║'''+str(d_fichas["3"]).center(10)+'''║'''+str(d_fichas["6"]).center(10)+'''║'''+str(d_fichas["9"]).center(10)+'''║'''+str(d_fichas["12"]).center(10)+'''║'''+str(d_fichas["15"]).center(10)+'''║'''+str(d_fichas["18"]).center(10)+'''║'''+str(d_fichas["21"]).center(10)+'''║'''+str(d_fichas["24"]).center(10)+'''║'''+str(d_fichas["27"]).center(10)+'''║'''+str(d_fichas["30"]).center(10)+'''║'''+str(d_fichas["33"]).center(10)+'''║'''+str(d_fichas["36"]).center(10)+'''║'''+str(d_fichas["2 to 1 1"]).center(10)+'''║
║          ║'''+lista[0][1]+'''║'''+lista[0][2]+'''║'''+lista[0][3]+'''║'''+lista[0][4]+'''║'''+lista[0][5]+'''║'''+lista[0][6]+'''║'''+lista[0][7]+'''║'''+lista[0][8]+'''║'''+lista[0][9]+'''║'''+lista[0][10]+'''║'''+lista[0][11]+'''║'''+lista[0][12]+'''║'''+lista[0][13]+'''║
║          ╠══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╣
║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║
║          ║'''+Back.BLACK+"2".center(10)+'''║'''+Back.RED+"5".center(10)+'''║'''+Back.BLACK+"8".center(10)+'''║'''+Back.RED+"11".center(10)+'''║'''+Back.BLACK+"14".center(10)+'''║'''+Back.RED+"17".center(10)+'''║'''+Back.BLACK+"20".center(10)+'''║'''+Back.RED+"23".center(10)+'''║'''+Back.BLACK+"26".center(10)+'''║'''+Back.RED+"29".center(10)+'''║'''+Back.BLACK+"32".center(10)+'''║'''+Back.RED+"35".center(10)+'''║'''+Back.GREEN+"2 to 1".center(10)+Back.BLACK+'''║
║'''+Back.GREEN+"0".center(10)+Back.BLACK+'''║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║
║          ║'''+str(d_fichas["2"]).center(10)+'''║'''+str(d_fichas["5"]).center(10)+'''║'''+str(d_fichas["8"]).center(10)+'''║'''+str(d_fichas["11"]).center(10)+'''║'''+str(d_fichas["14"]).center(10)+'''║'''+str(d_fichas["17"]).center(10)+'''║'''+str(d_fichas["20"]).center(10)+'''║'''+str(d_fichas["23"]).center(10)+'''║'''+str(d_fichas["26"]).center(10)+'''║'''+str(d_fichas["29"]).center(10)+'''║'''+str(d_fichas["32"]).center(10)+'''║'''+str(d_fichas["35"]).center(10)+'''║'''+str(d_fichas["2 to 1 2"]).center(10)+'''║
║          ║'''+lista[1][1]+'''║'''+lista[1][2]+'''║'''+lista[1][3]+'''║'''+lista[1][4]+'''║'''+lista[1][5]+'''║'''+lista[1][6]+'''║'''+lista[1][7]+'''║'''+lista[1][8]+'''║'''+lista[1][9]+'''║'''+lista[1][10]+'''║'''+lista[1][11]+'''║'''+lista[1][12]+'''║'''+lista[1][13]+'''║
║          ╠══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╣
║'''+str(d_fichas["0"]).center(10)+'''║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║
║          ║'''+Back.RED+"1".center(10)+'''║'''+Back.BLACK+"4".center(10)+'''║'''+Back.RED+"7".center(10)+'''║'''+Back.BLACK+"10".center(10)+'''║'''+Back.RED+"13".center(10)+'''║'''+Back.BLACK+"16".center(10)+'''║'''+Back.RED+"19".center(10)+'''║'''+Back.BLACK+"22".center(10)+'''║'''+Back.RED+"25".center(10)+'''║'''+Back.BLACK+"28".center(10)+'''║'''+Back.RED+"31".center(10)+'''║'''+Back.BLACK+"34".center(10)+'''║'''+Back.GREEN+"2 to 1".center(10)+Back.BLACK+'''║
║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║          ║
║          ║'''+str(d_fichas["1"]).center(10)+'''║'''+str(d_fichas["4"]).center(10)+'''║'''+str(d_fichas["7"]).center(10)+'''║'''+str(d_fichas["10"]).center(10)+'''║'''+str(d_fichas["13"]).center(10)+'''║'''+str(d_fichas["16"]).center(10)+'''║'''+str(d_fichas["19"]).center(10)+'''║'''+str(d_fichas["22"]).center(10)+'''║'''+str(d_fichas["25"]).center(10)+'''║'''+str(d_fichas["28"]).center(10)+'''║'''+str(d_fichas["31"]).center(10)+'''║'''+str(d_fichas["34"]).center(10)+'''║'''+str(d_fichas["2 to 1 3"]).center(10)+'''║
║'''+lista[0][0]+'''║'''+lista[2][1]+'''║'''+lista[2][2]+'''║'''+lista[2][3]+'''║'''+lista[2][4]+'''║'''+lista[2][5]+'''║'''+lista[2][6]+'''║'''+lista[2][7]+'''║'''+lista[2][8]+'''║'''+lista[2][9]+'''║'''+lista[2][10]+'''║'''+lista[2][11]+'''║'''+lista[2][12]+'''║'''+lista[2][13]+'''║
╚══════════╬══════════╩══════════╩══════════╩══════════╬══════════╩══════════╩══════════╩══════════╬══════════╩══════════╩══════════╩══════════╬══════════╝
           ║                                           ║                                           ║                                           ║
           ║'''+Back.GREEN+"1rd 12".center(43)+'''║'''+"2rd 12".center(43)+'''║'''+"3rd 12".center(43)+Back.BLACK+'''║
           ║                                           ║                                           ║                                           ║
           ║'''+str(d_fichas["1rd 12"]).center(43)+'''║'''+str(d_fichas["2rd 12"]).center(43)+'''║'''+str(d_fichas["3rd 12"]).center(43)+'''║
           ║                               '''+lista[3][1]+'''  ║                               '''+lista[3][2]+'''  ║                               '''+lista[3][3]+'''  ║
           ╠═════════════════════╦═════════════════════╬═════════════════════╦═════════════════════╬═════════════════════╦═════════════════════╣
           ║                     ║                     ║                     ║                     ║                     ║                     ║
           ║'''+Back.GREEN+"1-18".center(21)+'''║'''+"EVEN".center(21)+'''║'''+Back.RED+"ROJO".center(21)+'''║'''+Back.BLACK+"NEGRO".center(21)+'''║'''+Back.GREEN+"ODD".center(21)+'''║'''+"19-36".center(21)+Back.BLACK+'''║
           ║                     ║                     ║                     ║                     ║                     ║                     ║
           ║'''+str(d_fichas["1-18"]).center(21)+'''║'''+str(d_fichas["even"]).center(21)+'''║'''+str(d_fichas["rojo"]).center(21)+'''║'''+str(d_fichas["negro"]).center(21)+'''║'''+str(d_fichas["odd"]).center(21)+'''║'''+str(d_fichas["19-36"]).center(21)+'''║
           ║           '''+lista[4][1]+'''║           '''+lista[4][2]+'''║           '''+lista[4][3]+'''║           '''+lista[4][4]+'''║           '''+lista[4][5]+'''║           '''+lista[4][6]+'''║
           ╚═════════════════════╩═════════════════════╩═════════════════════╩═════════════════════╩═════════════════════╩═════════════════════╝
''')
#Saber donde esta el jugador para poder añadir fichas en la casilla de apuesta
def b_posicion():
    if posx == 0 and posy == 0:
        return "0"
    elif posx == 0 and posy == 1:
        return "3"
    elif posx == 0 and posy == 2:
        return "6"
    elif posx == 0 and posy == 3:
        return "9"
    elif posx == 0 and posy == 4:
        return "12"
    elif posx == 0 and posy == 5:
        return "15"
    elif posx == 0 and posy == 6:
        return "18"
    elif posx == 0 and posy == 7:
        return "21"
    elif posx == 0 and posy == 8:
        return "24"
    elif posx == 0 and posy == 9:
        return "27"
    elif posx == 0 and posy == 10:
        return "30"
    elif posx == 0 and posy == 11:
        return "33"
    elif posx == 0 and posy == 12:
        return "36"
    elif posx == 0 and posy == 13:
        return "2 to 1 1"
    #segunda fila
    elif posx == 1 and posy == 1:
        return "2"
    elif posx == 1 and posy == 2:
        return "5"
    elif posx == 1 and posy == 3:
        return "8"
    elif posx == 1 and posy == 4:
        return "11"
    elif posx == 1 and posy == 5:
        return "14"
    elif posx == 1 and posy == 6:
        return "17"
    elif posx == 1 and posy == 7:
        return "20"
    elif posx == 1 and posy == 8:
        return "23"
    elif posx == 1 and posy == 9:
        return "26"
    elif posx == 1 and posy == 10:
        return "29"
    elif posx == 1 and posy == 11:
        return "32"
    elif posx == 1 and posy == 12:
        return "35"
    elif posx == 1 and posy == 13:
        return "2 to 1 2"
    #Tercera fila
    elif posx == 2 and posy == 1:
        return "1"
    elif posx == 2 and posy == 2:
        return "4"
    elif posx == 2 and posy == 3:
        return "7"
    elif posx == 2 and posy == 4:
        return "10"
    elif posx == 2 and posy == 5:
        return "13"
    elif posx == 2 and posy == 6:
        return "16"
    elif posx == 2 and posy == 7:
        return "19"
    elif posx == 2 and posy == 8:
        return "22"
    elif posx == 2 and posy == 9:
        return "25"
    elif posx == 2 and posy == 10:
        return "28"
    elif posx == 2 and posy == 11:
        return "31"
    elif posx == 2 and posy == 12:
        return "34"
    elif posx == 2 and posy == 13:
        return "2 to 1 3"
    #Quarta fila
    elif posx == 3 and posy == 1:
        return "1rd 12"
    elif posx == 3 and posy == 2:
        return "2rd 12"
    elif posx == 3 and posy == 3:
        return "3rd 12"
    #Quinta fila
    elif posx == 4 and posy == 1:
        return "1-18"
    elif posx == 4 and posy == 2:
        return "even"
    elif posx == 4 and posy == 3:
        return "rojo"
    elif posx == 4 and posy == 4:
        return "negro"
    elif posx == 4 and posy == 5:
        return "odd"
    elif posx == 4 and posy == 6:
        return "19-36"

#Comprueba la apuesta
def comprobar_apuesta():
    for i in d_fichas:
        if d_fichas[i] != "":
            print("o")
            if i == random:
                print("Victoria")
            else:
                print("Tal vez")




#Bucle para poder jugar
while True:
    clear()
    display()
    posy_2 = busqueda()
    # comprobar_apuesta()
    print(b_posicion())
    print(d_fichas.keys())
    with Listener(on_press=key_recorder) as l:
       l.join()

