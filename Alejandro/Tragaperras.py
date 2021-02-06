
# CASINO
# Necesitamos un menú para escoger el juego que queremos jugar
# Necesitamos un contador con la cantidad de dinero que tienes
# Cuando ganas en los juegos obtienes dinero.
# Una tragaperras con al menos un 1% de probabilidades en base a 100.(1%/100%)
# Un Black Jack de cartas.
import random, rueda_traga, time

#time.sleep(1)

def juego(dinero,cont):
    if dinero > 0:
        jugar = str(input("\nQuieres jugar? (Tecla(Enter) o 'no') "))
        if jugar == "no":   # Si no quieres jugar dices "no"
            print("Has decidido no jugar a este juego.")
            opcion = int(input("A qué juego quieres ir ahora: "))
            
        elif jugar != "no" and dinero > 0: # Si quieres jugar puedes poner cualquier cosa menos "no"
            dinero -= 2
            cont += 1
            ganar = random.randint(1,80)
            if ganar == 80: # Probabilidades del 0.8%
                #time.sleep(1)
                rueda_traga.rueda(1,1,1)
                print("Has ganado el grande: 200€")
                dinero += grande

            elif ganar <= 16: # Probabilidades del 15.2%
                #time.sleep(1)
                rueda_traga.rueda(3,3,3)
                print("Has ganado: 5€")
                dinero += 5

            elif ganar >= 17 and ganar <= 23: # Probabilidades del 8%
                #time.sleep(1)
                rueda_traga.rueda(2,2,2)
                print("Has ganado: 10€")
                dinero += 10
                
            else: # Si el random da cualquier otra cosa que no sea 1 imprime esto
                #time.sleep(1)
                rueda_traga.aleat()
                print("No has ganado nada, vuelve a intentarlo.")
            print("Ahora tienes" ,dinero, "€")
                
    return dinero,cont

def pobre(dinero, opcion):
    if dinero <= 0: # Si no te queda dinero pierdes y te echan del casino
        print("Has perdido todo tu dinero")
        print("Te han echado del Casino y vas a morir pobre.")
        opcion = 0
    return opcion

cont= 0
dinero = 50    # El dinero que tienes
grande = 200   # El dinero que vas a obtener si ganas
tragaperras = True

# Has escoguido la TRAGAPERRAS

print("""Opciones:  5.tragaperras.5""")
        
print("Tienes" ,dinero, "€")
opcion = 5
if opcion == 5:
    while opcion == 5: # Mientras la variable tragaperras sea True el bucle se mantiene
        opcion = pobre(dinero, opcion)
        
        dinero,cont = juego(dinero,cont)
    print("Has jugado" ,cont, "veces")
        


            


