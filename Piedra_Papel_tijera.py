import random
print(" ---------------------- ")
print(" || Piedra Papel Tijera || ")
print(" ---------------------- ")
ListaDeObjetos = ["R","P","T"]
puntosDelJugador = 0
puntosDeLaComputadora = 0
i = 1
vecesAJugar = int(input("Cuantas partidas queres jugar?: "))
while i <= vecesAJugar:
    seleccionDeComputadora = str(random.choice(ListaDeObjetos))
    seleccionDelJugador = input("Elija entre Roca, Papel o Tijera: (Usar: R, P, T):").upper()
    if seleccionDelJugador == seleccionDeComputadora:
        print("😬 Empate, La compu y vos seleccionaron lo mismo")
    elif seleccionDelJugador == "R":
        print("La compu eligio: ", seleccionDeComputadora)
        if seleccionDeComputadora == "P":
            print("😤 Perdiste Rey! El papel le gana a la piedra")
            puntosDeLaComputadora += 1
        else:
            print("😁 Tu ganas! La piedra la rompe toda a la tijera")
            puntosDelJugador +=1
    elif seleccionDelJugador == "P":
        print("La compu elegio: ", seleccionDeComputadora)
        if seleccionDeComputadora == "T":
            print("😤 Perdiste Rey! La tijera corta el papel")
            puntosDeLaComputadora += 1
        else:
            print("😁 Tu 1 ganas! La piedra la rompe toda a la tijera")
            puntosDelJugador += 1
    elif seleccionDelJugador == "T":
        print("La compu eligio: ", seleccionDeComputadora)
        if seleccionDeComputadora == "R":
            print("😤 Perdiste Rey, La piedra la rompe toda a la tijera")
            puntosDeLaComputadora += 1
        else:
            print("😁 Tu ganas! la Tijera corta el papel")
            puntosDelJugador += 1
    else: 
        print(":(")
    print("\n\t******Puntuación******")
    print(f"\t Vos: {puntosDelJugador} | Computadora: {puntosDeLaComputadora}")
    print(f"\t***********************")
    print(f"Juego #:[{i}]")
    print("=========================================================")
    i += 1
print("\n\n#### Juego Terminado ####")
print("*******************************************")

if puntosDelJugador < puntosDeLaComputadora:
    print("😤 Perdiste  😤 \n La compu te partio la madre ganando...: ", puntosDeLaComputadora)
elif puntosDelJugador == puntosDeLaComputadora:
    print("😁 La partida quedo en empate. Juega otra vez 😁")
else:
    print("😁 Ganaste el jueguito, y estos son tus puntos...:", puntosDelJugador, "😁") 