from time import sleep 
import random

detras = 0
delante = 75 - detras

nombres_caballos = ['ZeeBullet','Atlantico',"Bannaby's Dream",'Delta Crucis','Run Run','Myaldagoba','Danzing De Saon','Niagara','Lenda Da Torre','Mill Valley','Spinerett']
caballos_a_competir = []        ##En esta lista vacía se añaden 4 nombres de caballos aleatoriamente

def caballos_elegidos():
    while True:
        validar = random.choice(nombres_caballos)
        if validar not in caballos_a_competir:
            caballos_a_competir.append(validar)
            
            if len(caballos_a_competir) == 4:
                break
            else:
                pass
        else:
            pass
                
def caballo(n):
    print('═'*90+'╦══╗')
    print(' '*detras,'        ,--, ',' '*delante+'║  ║')
    print(' '*detras,'  _ ___/ /\| ',' '*delante+'║  ║')
    print(' '*detras,' ;( )'+n,', )   ',' '*delante+'║  ║')
    print(' '*detras,'; // ¯¯`--;  ',' '*delante+'║  ║')
    print(' '*detras,'  \     |    ',' '*delante+'║  ║')
    print('═'*90+'╩══╝')
    
##while True:
##    detras = detras + 10
##    delante = delante - 10
##    caballo('1')
##    caballo('2')
##    caballo('3')
##    caballo('4')
##    print('\n'*3)
##    sleep(0.4)
##    print('\n'*50)
##    if detras >= 75:
##        break


def menu_caballos():
    esp1 = 23-len(caballos_a_competir[0])
    esp2 = 23-len(caballos_a_competir[1])
    esp3 = 23-len(caballos_a_competir[2])
    esp4 = 23-len(caballos_a_competir[3])
    
    print('\t\t\t┌─┐                                   ┌─┐')    
    print('\t\t\t│ │BIENVENIDO AL MUNDO DE LAS CARRERAS│ │')
    print('\t\t\t└─┼───────────────────────────────────┼─┘')
    print('\t\t\t  │ En el día de hoy tendremos a los  │\n\t\t\t  │\tsiguientes corredores:        │')
    print('\t\t\t┌─┼───────────────────────────────────┼─┐')
    print('\t\t\t│1│     ',caballos_a_competir[0],esp1*' ','    │1│')
    print('\t\t\t└─┼───────────────────────────────────┼─┘')
    print('\t\t\t  │                                   │  ')
    print('\t\t\t┌─┼───────────────────────────────────┼─┐')
    print('\t\t\t│2│     ',caballos_a_competir[1],esp2*' ','    │2│')
    print('\t\t\t└─┼───────────────────────────────────┼─┘')
    print('\t\t\t  │                                   │  ')
    print('\t\t\t┌─┼───────────────────────────────────┼─┐')
    print('\t\t\t│3│     ',caballos_a_competir[2],esp3*' ','    │3│')
    print('\t\t\t└─┼───────────────────────────────────┼─┘')
    print('\t\t\t  │                                   │  ')
    print('\t\t\t┌─┼───────────────────────────────────┼─┐')
    print('\t\t\t│4│     ',caballos_a_competir[3],esp4*' ','    │4│')
    print('\t\t\t└─┼───────────────────────────────────┼─┘')
    print('\t\t\t  │                                   │  ')
    print('\t\t\t┌─┼───────────────────────────────────┼─┐')
    print('\t\t\t│ │    La cuota se muestra al lado    │ │')
    print('\t\t\t│ │           del corredor            │ │')
    print('\t\t\t└─┘                                   └─┘')


caballos_elegidos()    
menu_caballos()


















