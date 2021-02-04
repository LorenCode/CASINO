from random import randrange
baraja=["corazones","picas","trebol","diamantes"]
cartas=[1,2,3,4,5,6,7,8,9,10,"j","q","k"]
dicc_card={1:"║  1  ║",2:"║  2  ║",3:"║  3  ║",4:"║  4  ║",5:"║  5  ║",6:"║  6  ║",7:"║  7  ║",8:"║  8  ║",9:"║  9  ║",10:"║  10 ║",11:"║  J  ║",12:"║  Q  ║",13:"║  k  ║"}
cartas_player=[]
dicc_palo={"corazones":"║♥    ║","picas":"║♠    ║","trebol":"║♣    ║","diamantes":"║♦    ║"}
dicc_palo2={"corazones":"║    ♥║","picas":"║    ♠║","trebol":"║    ♣║","diamantes":"║    ♦║"}
for i in range (2):  #--Xa obtener cartas aleatorias
    carta_player=[]
    palo=randrange(0,4)
    carta_player.append(baraja[palo])
    carta=randrange(1,13)
    carta_player.append(carta)
    cartas_player.append(carta_player) 
print (cartas_player)
num_cartas=len(cartas_player)#--Xa saber cuantas cartas
print (num_cartas)
#-------------------------------XA IMPRIMIR LAS CARTAS---------------------------------------------------------
for i in range (num_cartas):
    print ("╔═════╗",end="")
print("")
for i in range (num_cartas):    
   print (dicc_palo[cartas_player [i][0]],end="")
print("")
for i in range (num_cartas):
    print(dicc_card[cartas_player [i][1]],end="")
print("")
for i in range (num_cartas):    
   print (dicc_palo2[cartas_player [i][0]],end="")
print("")
for i in range (num_cartas):
    print("╚═════╝",end="")


