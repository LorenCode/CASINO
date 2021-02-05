from os import system

dinero = 0
monedas = {5:0, 10:0, 25:0, 100:0, 500:0, 1000:0 }
apuesta = 0


opcion = int(input("ELIGE UNA OPCIÓN\n 1-¡Quieres apostar!\n 2-Dinero\n 3-Salir\nTu opción: "))

while opcion != 3:
    if opcion == 1:
        system("cls") 
        print("Tu dinero:",dinero,"€")
        print("Monedas: ", "'5' = ",monedas[5], "| '10' = ",monedas[10], "| '25' = ",monedas[25],"| '100' = ",monedas[100], "| '500' = ",monedas[500],"| '1000' = ",monedas[1000])
        terminar_monedas = ""
        while terminar_monedas != 2:
            moneda_elegida = int(input("'5','10','25','100','500','1000'\n¿Que moneda quieres apostar? "))
            cantidad_monedas = int(input("¿Cuanta cantidad? "))
            monedas[moneda_elegida] += cantidad_monedas 
            apuesta += (moneda_elegida*cantidad_monedas)
            print("Donde quieres poner las monedas ")
            moneda_color = input("Elige: 'rojo', 'negro','1columna','2columna','3columna','1fila','2filla','3fila'")
            moneda_posicion = int(input("Elige el número (0-36): "))
            system("cls")

            print("Total apostado: ",apuesta)
            terminar_monedas = int(input("¿Quieres apostar más?\n 1-Si\n 2-No\n¿Que vas hacer?"))
            print(apuesta)
            system("cls")
        

    elif opcion == 2:
        opcion_dinero = 0
        while opcion_dinero != 2:
            system("cls")
            print("Dinero: ", dinero,"€")
            print("Monedas: ", "'5' = ",monedas[5], "| '10' = ",monedas[10], "| '25' = ",monedas[25],"| '100' = ",monedas[100], "| '500' = ",monedas[500],"| '1000' = ",monedas[1000])
            print()
            opcion_dinero = int(input("ESTAS EN LA BANCA DEL CASINO\n 1-Conseguir monedas\n 2-Salir de la banca\n ¿Que vas hacer? "))
            if opcion_dinero == 1:
                system("cls")
                moneda_elegida = int(input("'5','10','25','100','500','1000'\n¿Que moneda quieres apostar? "))
                cantidad_monedas = int(input("¿Cuanta cantidad? "))
                monedas[moneda_elegida] += cantidad_monedas

    else:
        print("No quiero ir")
    system("cls")
    opcion = int(input("ELIGE UNA OPCIÓN\n 1-¡Quieres apostar!\n 2-Dinero\n 3-Salir\nTu opción: "))