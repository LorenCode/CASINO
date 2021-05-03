from time import sleep
import os
from pynput.keyboard import Listener
from colorama import init, Fore, Back, Style
from random import choice
import movimiento_ruleta
import ganar
import perder

clear = lambda: os.system('cls')


# Resultado aleatoria
# l_tablero_random = ["2 to 1 1", "2 to 1 2", "2 to 1 3","1rd 12", "2rd 12", "3rd 12", "1-18", "even", "rojo", "negro", "odd", "19-36"]
l_random = [i for i in range(37)]
# for a in l_tablero_random:
#     l_random.append(a)

#Inteructor de ayuda
in_help = False

# Se crean las listas para almacenar el tablero
lista = []
for i in range(5):
    lista.append([])
    for a in range(14):
        lista[i].append('          ')

#Se crea el dicionario que contendra las apuestas
d_fichas = {}

def b_fichas():   

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

#Dinero del jugador
dinero = 100

#Copia del dinero
copia_dinero = []
def hacer_copia_dinero():
    global copia_dinero 
    copia_dinero = []
    copia_dinero.append(dinero)

#Posicion inicial del jugador
posx = 1
posy = 2

lista[posx][posy] = '    O     '


def busqueda():
    """Busca en la lista 2 la posición del jugador"""
    damela = 0
    for i in range(13):
        if lista[2][i] == '    O     ':
            damela = i

    return damela


def key_recorder(key):
    """Movimientos del jugador"""
    global posx
    global posy
    global lista
    global dinero
    global in_help

    
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
        if dinero > 0 and dinero >= 5:
            dinero -= 5
            if d_fichas[b_posicion()] != "":
                    d_fichas[b_posicion()] += 5
            else:
                d_fichas[b_posicion()] = 5  

    #Apostar con la ficha de 25
    elif key == 's':
        if dinero > 0 and dinero >= 25:
            dinero -= 25
            if d_fichas[b_posicion()] != "":
                d_fichas[b_posicion()] += 25
            else:
                d_fichas[b_posicion()] = 25

    #Apostar con la ficha de 50
    elif key == 'd':
         if dinero > 0 and dinero >= 50:
            dinero -= 50
            if d_fichas[b_posicion()] != "":
                d_fichas[b_posicion()] += 50
            else:
                d_fichas[b_posicion()] = 50

    #Apostar con la ficha de 100
    elif key == 'q':
         if dinero > 0 and dinero >= 100:
            dinero -= 100
            if d_fichas[b_posicion()] != "":
                d_fichas[b_posicion()] += 100
            else:
                d_fichas[b_posicion()] = 100

    #Apostar con la ficha de 500
    elif key == 'w':
         if dinero > 0 and dinero >= 500:
            dinero -= 500
            if d_fichas[b_posicion()] != "":
                d_fichas[b_posicion()] += 500
            else:
                d_fichas[b_posicion()] = 500
            
    #Apostar con la ficha de 1000
    elif key == 'd':
         if dinero > 0 and dinero >= 1000:
            dinero -= 1000
            if d_fichas[b_posicion()] != "":
                d_fichas[b_posicion()] += 1000
            else:
                d_fichas[b_posicion()] = 1000

    #Validar apuesta
    elif key == 'Key.enter':
        global ciclos
        global p_intro


        #Almazena las apuestas para saber si a apostado
        t_apuesta = 0 
    
        #Busca en el tablero donde se a apostado y lo almazena en el diccionario
        for i in d_fichas:
            if d_fichas[i] != "":
                t_apuesta += 1 

        if t_apuesta > 0 :
            p_intro = True
        else:
            pass
    
    #borrar apuesta
    # elif key == 'Key.backspace':
    #     if d_fichas[b_posicion()] != "":
    #         d_fichas[b_posicion()] = ""

    elif key == 'h':
        if in_help:
            in_help = False
        else:
            in_help = True

    elif key == 't':
        b_fichas()
        dinero = copia_dinero[0]

    elif key == 'Key.space':
        global interructor_seguir
        if p_intro == True: 
            interructor_seguir = True
            
    elif key == 'Key.esc':
        global int_terminar
        if p_intro == True: 
            int_terminar = True
            
    l.stop()


def display():
    """Tablero"""
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
           ║'''+Back.GREEN+"1-18".center(21)+'''║'''+"PAR".center(21)+'''║'''+Back.RED+"ROJO".center(21)+'''║'''+Back.BLACK+"NEGRO".center(21)+'''║'''+Back.GREEN+"IMPAR".center(21)+'''║'''+"19-36".center(21)+Back.BLACK+'''║
           ║                     ║                     ║                     ║                     ║                     ║                     ║
           ║'''+str(d_fichas["1-18"]).center(21)+'''║'''+str(d_fichas["even"]).center(21)+'''║'''+str(d_fichas["rojo"]).center(21)+'''║'''+str(d_fichas["negro"]).center(21)+'''║'''+str(d_fichas["odd"]).center(21)+'''║'''+str(d_fichas["19-36"]).center(21)+'''║
           ║           '''+lista[4][1]+'''║           '''+lista[4][2]+'''║           '''+lista[4][3]+'''║           '''+lista[4][4]+'''║           '''+lista[4][5]+'''║           '''+lista[4][6]+'''║
           ╚═════════════════════╩═════════════════════╩═════════════════════╩═════════════════════╩═════════════════════╩═════════════════════╝
''')

def help():
    print('''
           ╔═════════════════════════════════════╗
           ║   Q= 100     W= 500       E= 1000   ║   
           ║                                     ║
           ║   A= 5       S = 25       D = 50    ║
           ║                                     ║
           ║   T= Limpiar tablero                ║
           ║   Intro= Terminar apuesta           ║
           ║                                     ║
           ╚═════════════════════════════════════╝
    ''')

def menu_seguir_terminar():
    print('''
           ╔═════════════════════════════════════╗
           ║                                     ║
           ║   QUIERES VOLVER A APOSTAR          ║
           ║   espacio=Si o Esc=No               ║
           ║                                     ║
           ╚═════════════════════════════════════╝
    ''')

def b_posicion():
    """Saber donde esta el jugador para poder añadir fichas en la casilla de apuesta"""
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

def fichas_apuesta():
    """Comprueba la apuesta"""
    def c_premio(a1,mul):
        """ Calcula el premio"""
        at = a1*mul+a1
        return at

    global dinero
    # global random

    #valor al azar
    random = choice(l_random)

    #Premio
    premio = 0

    #Almazena las apuestas
    d_apuesta = {} 
    
    #Busca en el tablero donde se a apostado y lo almazena en el diccionario
    for i in d_fichas:
        if d_fichas[i] != "":
            d_apuesta[i] = d_fichas[i]

    #Variables para utilizar a la hora de comprobar las apuestas.

    #Apuestas sencillas
    rojo = [i for i in range(1,36,2)]   #x1
    negro = [i for i in range(2,37,2)]  #x1

    #Saber el color de random
    g_color = ""
    if random in rojo:
        g_color = "rojo"
    elif random in negro:
        g_color = "negro"

    #Apuestas múltiples
    c1 = [i for i in range(3,37,3)] #Columna x2 -Doble columna x0.5
    c2 = [i for i in range(2,36,3)] #Columna x2
    c3 = [i for i in range(1,35,3)] #Columna x2
    d1 = [i for i in range(1,13)]   #Docena x2  - Doble docena x0.5
    d2 = [i for i in range(13,25)]  #Docena x2
    d3 = [i for i in range(25,37)]  #Docena x2
    a1_18 = [i for i in range(1,19)]    #x1
    a19_36 = [i for i in range(19,37)]  #x1
    par = [i for i in range(2,37,2)]
    impar = [i for i in range(1,36,2)]

    #Comprobando la apuesta
    print("Ruleta:",random)

    for v1 in d_apuesta:
        premio = 0
        # print("random: ",random)
        # print("apuesta", v1)
        if v1.isdigit():
            if int(v1) == random:
                premio += c_premio(d_apuesta[v1],35)
        else:
            if v1 == "rojo":
                premio += c_premio(d_apuesta[v1],1)
            elif v1 == "negro":
                premio += c_premio(d_apuesta[v1],1)
            elif v1 == "1rd 12":
                if random in d1:
                    premio += c_premio(d_apuesta[v1],2)
            elif v1 == "2rd 12":
                if random in d2:
                    premio += c_premio(d_apuesta[v1],2)
            elif v1 == "3rd 12":
                if random in d3:
                    premio += c_premio(d_apuesta[v1],2)
            elif v1 == "2 to 1 1":
                if random in c1:
                    premio += c_premio(d_apuesta[v1],2)
            elif v1 == "2 to 1 2":
                if random in c2:
                    premio += c_premio(d_apuesta[v1],2)
            elif v1 == "2 to 1 3":
                if random in c3:
                    premio += c_premio(d_apuesta[v1],2)
            elif v1 == "1-18":
                if random in a1_18:
                    premio += c_premio(d_apuesta[v1],1)
            elif v1 == "19-36":
                if random in a19_36:
                    premio += c_premio(d_apuesta[v1],1)
            elif v1 == "even": 
                if random in par:
                    premio += c_premio(d_apuesta[v1],1)
            elif v1 == "odd": 
                if random in impar:
                    premio += c_premio(d_apuesta[v1],1)
        dinero += premio
    if premio > 0:
        print("Has gando: ",premio)
        ganar.g_img() 
    else:
        perder.p_img()
    


#Bucle para poder jugar
ciclos = True
p_intro = False
interructor_seguir = False
int_terminar = False
b_fichas()
hacer_copia_dinero()
while ciclos != False:   
    clear()
    display()
    posy_2 = busqueda()
    if in_help:
        help()
    print("Dinero: ", dinero)
    with Listener(on_press=key_recorder) as l:
       l.join()
    clear()
    #Condicion para decidir seguir o terminar la partida. Tambien se da la victoria o derrota.
    if p_intro == True: 
        borrar_teclas = input("")
        clear()
        movimiento_ruleta.ruleta_total()
    
        fichas_apuesta()
        menu_seguir_terminar()
        while interructor_seguir == False and int_terminar == False: # Seguir con terminar ESC
            with Listener(on_press=key_recorder) as l:
                l.join()
                
        if interructor_seguir == True:
            print("Seguir jugando")
            p_intro = False
            b_fichas()
            hacer_copia_dinero()
            interructor_seguir = False
        elif int_terminar == True:
            # borrar_teclas = input("")
            clear()
            perder.p_img()
            print("Fin de la partida")
            ciclos = False
            


        