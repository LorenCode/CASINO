
import os
from time import sleep
clear = lambda: os.system("cls")

lista_ruleta=[]
for i in range(9):
    lista_ruleta.append([])  
for x in range(12):
    lista_ruleta[0].append('   ')
for v in range(1,8):
    for c in range(2):
        lista_ruleta[v].append('   ')
for x in range(12):
    lista_ruleta[8].append('   ')



def ruleta():
    print('''
    ┌─────────┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬─────────┐
    │         │   │   │   │   │   │   │   │   │   │   │         │
    │   15    │  3│ 24│ 36│ 13│ 1 │ 00│ 27│ 10│ 25│ 29│    12   │
    │     ╔═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╗     │
    │     ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║     │
    │     ║'''+lista_ruleta[0][0]+'''║'''+lista_ruleta[0][1]+'''║'''+lista_ruleta[0][2]+'''║'''+lista_ruleta[0][3]+'''║'''+lista_ruleta[0][4]+'''║'''+lista_ruleta[0][5]+'''║'''+lista_ruleta[0][6]+'''║'''+lista_ruleta[0][7]+'''║'''+lista_ruleta[0][8]+'''║'''+lista_ruleta[0][9]+'''║'''+lista_ruleta[0][10]+'''║'''+lista_ruleta[0][11]+'''║     │
    ├─────╫═══╬═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╬═══╫─────┤
    │     ║   ║                                       ║   ║     │
    │  34 ║'''+lista_ruleta[1][0]+'''║                                       ║'''+lista_ruleta[1][1]+'''║ 8   │
    ├─────╫═══╣                                       ╠═══╫─────┤
    │     ║   ║                                       ║   ║     │
    │  22 ║'''+lista_ruleta[2][0]+'''║                                       ║'''+lista_ruleta[2][1]+'''║ 19  │
    ├─────╫═══╣                                       ╠═══╫─────┤
    │     ║   ║                    █                  ║   ║     │
    │   5 ║'''+lista_ruleta[3][0]+'''║                    █                  ║'''+lista_ruleta[3][1]+'''║ 31  │
    ├─────╫═══╣                    █                  ╠═══╫─────┤
    │     ║   ║                  █████                ║   ║     │
    │  17 ║'''+lista_ruleta[4][0]+'''║           ▀▀▀▀▀▀▀█████▀▀▀▀▀▀▀         ║'''+lista_ruleta[4][1]+'''║ 18  │
    ├─────╫═══╣                    █                  ╠═══╫─────┤
    │     ║   ║                    █                  ║   ║     │    
    │  32 ║'''+lista_ruleta[5][0]+'''║                    █                  ║'''+lista_ruleta[5][1]+'''║ 6   │
    ├─────╫═══╣                                       ╠═══╫─────┤
    │     ║   ║                                       ║   ║     │
    │  20 ║'''+lista_ruleta[6][0]+'''║                                       ║'''+lista_ruleta[6][1]+'''║ 21  │
    ├─────╫═══╣                                       ╠═══╫─────┤
    │     ║   ║                                       ║   ║     │
    │   7 ║'''+lista_ruleta[7][0]+'''║                                       ║'''+lista_ruleta[7][1]+'''║ 33  │
    ├─────╫═══╬═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╬═══╫─────┤
    │     ║'''+lista_ruleta[8][0]+'''║'''+lista_ruleta[8][1]+'''║'''+lista_ruleta[8][2]+'''║'''+lista_ruleta[8][3]+'''║'''+lista_ruleta[8][4]+'''║'''+lista_ruleta[8][5]+'''║'''+lista_ruleta[8][6]+'''║'''+lista_ruleta[8][7]+'''║'''+lista_ruleta[8][8]+'''║'''+lista_ruleta[8][9]+'''║'''+lista_ruleta[8][10]+'''║'''+lista_ruleta[8][11]+'''║     │
    │     ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║     │
    │     ╚═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╝     │
    │   11    │ 30│ 26│  9│ 28│  0│  2│ 14│ 35│ 23│  4│    16   │
    │         │   │   │   │   │   │   │   │   │   │   │         │
    └─────────┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴─────────┘

    ''')

posx = 0
posy = 6


for a in range(6):
    clear()
    lista_ruleta[posx][posy] = ' ● '
    lista_ruleta[posx][posy-1] = '   '
    posy += 1
    ruleta()
    sleep(0.2)



if lista_ruleta[0][11] == ' ● ':
    lista_ruleta[0][11] = '   '
    for b in range(1,8):
        clear()
        lista_ruleta[b][1] = ' ● '
        lista_ruleta[b-1][1] = '   '
        ruleta()
        sleep(0.2)


posy = 11

for a in range(12):
    clear()
    lista_ruleta[8][posy-1] = ' ● '
    posy = -1
    lista_ruleta[8][posy] = '   '
    
    ruleta()
    sleep(0.2)

for c in lista_ruleta:
    print(c)