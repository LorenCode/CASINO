

import random

# Las intrucciones para imprimir las imagenes del tragaperras.
# Flata implementarla en el tragaperras como un modulo.

def rueda(pri,seg,ter): # Requerimos de 3 valores para sacar las imagenes.
    print("\t ╔" + "═"*11 + "╗\t ╔" + "═"*11 + "╗\t ╔" + "═"*11 + "╗") # primera linea
    for x in range(6): # Bucle for para sacar la imagen entera
        print("\t",dicc[pri][x],"\t",dicc[seg][x],"\t",dicc[ter][x]) 
    print("\t ╚" + "═"*11 + "╝\t ╚" + "═"*11 + "╝\t ╚" + "═"*11 + "╝") # ultima linea

# El bucle usa los numeros para imprimir la variable del diccionario.
# Ejemplo: diccionario con clave[1] y valor numerico[0] imprime la variable (0) de la clave (1)
# Explicación: Le damos un valor que la funcion recoge como una clave del diccionario y este imprime la imagen.

def aleat(): # Una función para mostrar aleatoriamente las imagenes que te da el juego.
    # Los valores se dan de esta forma debido a que no se puede hacer usando un bucle.
    pri=random.randint(1,3) 
    seg=random.randint(1,3)
    ter=random.randint(1,3)
    if pri==seg==ter: # Valida si todos las imagenes son iguales.
        seg += 1 # Le suma 1 al valor de la segunda imagen, para que sea diferente del resto.
        if seg not in dicc: # Si el valor de la segunda imagen no esta asociado a ninguna clave del diccionario hace esta acción.
            seg -= 2 # Le resta 2 al valor de la segunda imagen, para que sea diferente del resto.
    rueda(pri,seg,ter) # Llama a la función que muestra las imagenes.
    return


# Variables para mostrar un diamante
di1="║ " + "╔"+"═"*7+"╗"+ " ║"
di2="║ " + "╚╗"+" "*5+"╔╝" + " ║"
di3="║  " + "╚╗"+" "*3+"╔╝" + "  ║"
di4="║   " + "╚╗"+" "+"╔╝" "   ║"
di5="║    " + "╚"+"═"+"╝" + "    ║"
di6="║" + " "*11 + "║"
diam=[di1,di2,di3,di4,di5,di6]
# Variables para mostrar una fresa
fre1="║ " + " "*5+"╔═╗" + "  ║"
fre2="║ " + "╔"+"═"*4+"╝ ╚╗" + " ║"
fre3="║ " + "║"+" "*5+"╔═╝" + " ║"
fre4="║ " +"║"+" "*5+"║" + "   ║"
fre5="║ " +"╚"+"═"*5+"╝" + "   ║"
fre6="║" + " "*11 + "║"
fres=[fre1,fre2,fre3,fre4,fre5,fre6]
# Variables para mostrar otra imagen
ot1="║ "+"╗"+" "*7+"╔"+" ║"
ot2="║ "+"╚═╗"+" "*3+"╔═╝"+" ║"
ot3="║   "+"╚═╗"+"═╝"+" "*2+" ║"
ot4="║   "+"╔═╝"+"═╗"+" "*2+" ║"
ot5="║ "+"╔═╝"+" "*3+"╚═╗"+" ║"
ot6="║ "+"╝"+" "*7+"╚"+" ║"
otr=[ot1,ot2,ot3,ot4,ot5,ot6]

dicc={1:diam,2:fres,3:otr}

# rueda(1,2,3)





