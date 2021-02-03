
# CASINO
# Necesitamos un menú para escoger el juego que queremos jugar
# Necesitamos un contador con la cantidad de dinero que tienes
# Cuando ganas en los juegos obtienes dinero.
# Una tragaperras con al menos un 1% de probabilidades en base a 100.(1%/100%)
# Un Black Jack de cartas.
import random

def pobre(dinero):
    if dinero == 0: # Si no te queda dinero pierdes y te echan del casino
        print("Has perdido todo tu dinero")
        print("Te han hechado del Casino y vas a morir pobre.")
    return
    

dinero = 30    # El dinero que tienes
grande = 200   # El dinero que vas a obtener si ganas
tragaperras = True

# Has escoguido la TRAGAPERRAS

print("""Opciones:  5.tragaperras.5""")
        
print("Tienes" ,dinero, "€")
opcion = 5
if opcion == 5:
    while opcion == 5: # Mientras la variable tragaperras sea True el bucle se mantiene
        jugar = str(input("Quieres jugar? ")) # Indicamos cualquier palabra menos "no" para jugar
        if dinero == 0:
            print("Has perdido todo tu dinero")
            print("Te han hechado del Casino y vas a morir pobre.")
            opcion = 0
            
        if jugar == "no":   # Si no quieres jugar dices "no"
            print("Te has echado atrás y no vas a jugar este juego.")
            opcion = int(input("Qué opción quieres jugar ahora: "))
            
        elif jugar != "no" and dinero > 0: # Si quieres jugar puedes poner cualquier cosa menos "no"
            dinero -= 1
            ganar = random.randint(1,90)
            if ganar <= 2: # Si el random da 1 has ganado el premio
                print("Has ganado el grande:" ,grande)
                dinero += grande
                print("Ahora tienes" ,dinero, "€")
                
            else: # Si el random da cualquier otra cosa que no sea 1 imprime esto
                print("No has ganado nada, vuelve a intentarlo.")
                print("Tienes" ,dinero, "€")
            


            
        


            


