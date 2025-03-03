from tkinter import ttk
import random
from tkinter import *

def centra(ventana, ancho, alto): 
    """ centra las ventanas en la pantalla """ 
    x = ventana.winfo_screenwidth() // 2 - ancho // 2 
    y = ventana.winfo_screenheight() // 2 - alto // 2 
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}')
    return ventana

def lanzarDados(dados, primerDado, segundoDado, movimientos):
    global imagenDado1, imagenDado2, lanzamientoDado1, lanzamientoDado2
    lanzamientoDado1 = random.randint(1, 6)
    lanzamientoDado2 = random.randint(1, 6)
    for i in range(0,2):
        if i == 0:
            imagenDado1 = PhotoImage(file = 'Dado'+ str(lanzamientoDado1) +'.png')
            dados.itemconfig(primerDado, image=imagenDado1)
        else:
            imagenDado2 = PhotoImage(file = 'Dado'+ str(lanzamientoDado2) +'.png')
            dados.itemconfig(segundoDado, image=imagenDado2)
    movimientos.config(text= str(lanzamientoDado1) + ' - ' + str(lanzamientoDado2))
    lanzar.config(state="disabled")
    if jugador.cget("text") == "Jugador 1":
        estadoFicha1 = tableroJuego.gettags(FVJ1)
        estadoFicha2 = tableroJuego.gettags(FVJ2)
        estadoFicha3 = tableroJuego.gettags(FVJ3)
        estadoFicha4 = tableroJuego.gettags(FVJ4)
        if "capturada" in estadoFicha1:
            if "capturada" in estadoFicha2:
                if "capturada" in estadoFicha3:
                    if "capturada" in estadoFicha4:
                        if lanzamientoDado1 == 5 and lanzamientoDado2 == 5:
                            tableroJuego.dtag(FVJ1, "capturada")
                            tableroJuego.addtag_withtag("fuera", FVJ1)
                            tableroJuego.addtag_withtag("0", FVJ1)
                            tableroJuego.dtag(FVJ2, "capturada")
                            tableroJuego.addtag_withtag("fuera", FVJ2)
                            tableroJuego.addtag_withtag("0", FVJ2)
                            movimientos.config(text= '0 - 0')
                        elif lanzamientoDado1 == 5:
                            tableroJuego.dtag(FVJ1, 'capturada')
                            tableroJuego.addtag_withtag("fuera", FVJ1)
                            tableroJuego.addtag_withtag("0", FVJ1)
                            movimientos.config(text= '0 - ' + str(lanzamientoDado2))
                            mover(FVJ1, lanzamientoDado2, movimientos)
                        elif lanzamientoDado2 == 5:
                            tableroJuego.dtag(FVJ1, 'capturada')
                            tableroJuego.addtag_withtag("fuera", FVJ1)
                            tableroJuego.addtag_withtag("0", FVJ1)
                            movimientos.config(text= str(lanzamientoDado1) + ' - 0')
                            mover(FVJ1, lanzamientoDado1, movimientos)
        if "ganadora" in estadoFicha1:
            if "ganadora" in estadoFicha2:
                if "ganadora" in estadoFicha3:
                    if "ganadora" in estadoFicha4:
                        print("Gana el Jugador 1")
                        return
    elif jugador.cget("text") == "Jugador 2":
        estadoFicha1 = tableroJuego.gettags(FAJ1)
        estadoFicha2 = tableroJuego.gettags(FAJ2)
        estadoFicha3 = tableroJuego.gettags(FAJ3)
        estadoFicha4 = tableroJuego.gettags(FAJ4)
        if "capturada" in estadoFicha1:
            if "capturada" in estadoFicha2:
                if "capturada" in estadoFicha3:
                    if "capturada" in estadoFicha4:
                        if lanzamientoDado1 == 5 and lanzamientoDado2 == 5:
                            tableroJuego.dtag(FAJ1, "capturada")
                            tableroJuego.addtag_withtag("fuera", FAJ1)
                            tableroJuego.addtag_withtag("25", FAJ1)
                            tableroJuego.dtag(FAJ2, "capturada")
                            tableroJuego.addtag_withtag("fuera", FAJ2)
                            tableroJuego.addtag_withtag("25", FAJ2)
                            movimientos.config(text= '0 - 0')
                        elif lanzamientoDado1 == 5:
                            tableroJuego.dtag(FAJ1, 'capturada')
                            tableroJuego.addtag_withtag("fuera", FAJ1)
                            tableroJuego.addtag_withtag("25", FAJ1)
                            movimientos.config(text= '0 - ' + str(lanzamientoDado2))
                            mover(FAJ1, lanzamientoDado2, movimientos)
                        elif lanzamientoDado2 == 5:
                            tableroJuego.dtag(FAJ1, 'capturada')
                            tableroJuego.addtag_withtag("fuera", FAJ1)
                            tableroJuego.addtag_withtag("25", FAJ1)
                            movimientos.config(text= str(lanzamientoDado1) + ' - 0')
                            mover(FAJ1, lanzamientoDado1, movimientos)
        if "ganadora" in estadoFicha1:
            if "ganadora" in estadoFicha2:
                if "ganadora" in estadoFicha3:
                    if "ganadora" in estadoFicha4:
                        print("Gana el Jugador 2")
                        return
    elif jugador.cget("text") == "Jugador 3":
        estadoFicha1 = tableroJuego.gettags(FAmJ1)
        estadoFicha2 = tableroJuego.gettags(FAmJ2)
        estadoFicha3 = tableroJuego.gettags(FAmJ3)
        estadoFicha4 = tableroJuego.gettags(FAmJ4)
        if "capturada" in estadoFicha1:
            if "capturada" in estadoFicha2:
                if "capturada" in estadoFicha3:
                    if "capturada" in estadoFicha4:
                        if lanzamientoDado1 == 5 and lanzamientoDado2 == 5:
                            tableroJuego.dtag(FAmJ1, "capturada")
                            tableroJuego.addtag_withtag("fuera", FAmJ1)
                            tableroJuego.addtag_withtag("50", FAmJ1)
                            tableroJuego.dtag(FAmJ2, "capturada")
                            tableroJuego.addtag_withtag("fuera", FAmJ2)
                            tableroJuego.addtag_withtag("50", FAmJ2)
                            movimientos.config(text= '0 - 0')
                        elif lanzamientoDado1 == 5:
                            tableroJuego.dtag(FAmJ1, 'capturada')
                            tableroJuego.addtag_withtag("fuera", FAmJ1)
                            tableroJuego.addtag_withtag("50", FAmJ1)
                            movimientos.config(text= '0 - ' + str(lanzamientoDado2))
                            mover(FAmJ1, lanzamientoDado2, movimientos)
                        elif lanzamientoDado2 == 5:
                            tableroJuego.dtag(FAmJ1, 'capturada')
                            tableroJuego.addtag_withtag("fuera", FAmJ1)
                            tableroJuego.addtag_withtag("50", FAmJ1)
                            movimientos.config(text= str(lanzamientoDado1) + ' - 0')
                            mover(FAmJ1, lanzamientoDado1, movimientos)
        if "ganadora" in estadoFicha1:
            if "ganadora" in estadoFicha2:
                if "ganadora" in estadoFicha3:
                    if "ganadora" in estadoFicha4:
                        print("Gana el Jugador 3")
                        return
    else:
        estadoFicha1 = tableroJuego.gettags(FRJ1)
        estadoFicha2 = tableroJuego.gettags(FRJ2)
        estadoFicha3 = tableroJuego.gettags(FRJ3)
        estadoFicha4 = tableroJuego.gettags(FRJ4)
        if "capturada" in estadoFicha1:
            if "capturada" in estadoFicha2:
                if "capturada" in estadoFicha3:
                    if "capturada" in estadoFicha4:
                        if lanzamientoDado1 == 5 and lanzamientoDado2 == 5:
                            tableroJuego.dtag(FRJ1, "capturada")
                            tableroJuego.addtag_withtag("fuera", FRJ1)
                            tableroJuego.addtag_withtag("75", FRJ1)
                            tableroJuego.dtag(FRJ2, "capturada")
                            tableroJuego.addtag_withtag("fuera", FRJ2)
                            tableroJuego.addtag_withtag("75", FRJ2)
                            movimientos.config(text= '0 - 0')
                        elif lanzamientoDado1 == 5:
                            tableroJuego.dtag(FRJ1, 'capturada')
                            tableroJuego.addtag_withtag("fuera", FRJ1)
                            tableroJuego.addtag_withtag("75", FRJ1)
                            movimientos.config(text= '0 - ' + str(lanzamientoDado2))
                            mover(FRJ1, lanzamientoDado2, movimientos)
                        elif lanzamientoDado2 == 5:
                            tableroJuego.dtag(FRJ1, 'capturada')
                            tableroJuego.addtag_withtag("fuera", FRJ1)
                            tableroJuego.addtag_withtag("75", FRJ1)
                            movimientos.config(text= str(lanzamientoDado1) + ' - 0')
                            mover(FRJ1, lanzamientoDado1, movimientos)
        if "ganadora" in estadoFicha1:
            if "ganadora" in estadoFicha2:
                if "ganadora" in estadoFicha3:
                    if "ganadora" in estadoFicha4:
                        print("Gana el Jugador 4")
                        return
    finalTurno.config(state="normal")

def finTurno():
    if jugador.cget("text") == "Jugador 1":
        jugador.config(text= "Jugador 2")
    elif jugador.cget("text") == "Jugador 2":
        jugador.config(text= "Jugador 3")
    elif jugador.cget("text") == "Jugador 3":
        jugador.config(text= "Jugador 4")
    else:
        jugador.config(text= "Jugador 1")
    lanzar.config(state="normal")
    finalTurno.config(state="disabled")

def mover(ficha, mueve, movimientos):
    casillas = {
    "0": (94, 345), "1": (122, 345), "2": (150, 345), "3": (178, 345), "4": (206, 345), "5": (246, 380), "6": (246, 408), "7": (246, 436), "8": (246, 464), "9": (246, 492), "10": (246, 520), "11": (246, 548), "12": (246, 576), "13": (275, 580),
    "14": (275, 550), "15": (275, 520), "16": (275, 492), "17": (275, 464), "18": (275, 436), "19": (275, 408), "20": (275, 380), "21": (294, 343), #Casillas Azul
    "22": (342, 580), "23": (342, 550), "24": (342, 520), "25": (342, 492), "26": (342, 464), "27": (342, 436), "28": (342, 408), "29": (342, 380),"30": (380, 341), "31": (408, 341), "32": (436, 341), "33": (464, 341), "34": (492, 341), "35": (520, 341), "36": (548, 341), "37": (576, 341), "38": (580, 312), 
    "39": (548, 312), "40": (520, 312), "41": (492, 312), "42": (464, 312), "43": (436, 312), "44": (408, 312), "45": (380, 312), "46": (343, 294), #Casillas Amarillo
    "47": (580, 245), "48": (548, 245), "49": (520, 245), "50": (492, 245), "51": (464, 245), "52": (436, 245), "53": (408, 245), "54": (380, 245), "55": (340, 208), "56": (340, 180), "57": (340, 152), "58": (340, 124), "59": (340, 96), "60": (340, 68), "61": (340, 40), "62": (340, 12), "63": (312, 12), 
    "64": (312, 40), "65": (312, 68), "66": (312, 96), "67": (312, 124), "68": (312, 152), "69": (312, 180), "70": (312, 208), "71": (294, 243), #Casillas Rojo
    "72": (246, 12), "73": (246, 40), "74": (246, 68), "75": (246, 96), "76": (246, 124), "77": (246, 152), "78": (246, 180), "79": (246, 208), "80": (206, 245), "81": (178, 245), "82": (150, 245), "83": (122, 245), "84": (94, 245), "85": (68, 245), "86": (38, 245), "87": (10, 245), "88": (10, 276), 
    "89": (38, 276), "90": (68, 276), "91": (94, 276), "92": (122, 276), "93": (150, 276), "94": (178, 276), "95": (206, 276), "96": (245, 294), #Casillas Verde
    "97": (10, 345), "98": (38, 345), "99": (68, 345)
    }
    if jugador.cget("text") == "Jugador 1":
        tags = tableroJuego.gettags(ficha)
        casillaActual = tags[2]
        try:
            casillaSiguiente = int(casillaActual) + mueve
        except:
            casillaActual = tags[1]
            casillaSiguiente = int(casillaActual) + mueve
        if casillaSiguiente >= 100:
            casillaSiguiente = casillaSiguiente - 100
        if casillaSiguiente > 13 and casillaSiguiente < 22:
            casillaSiguiente = casillaSiguiente + 8
        elif casillaSiguiente > 38 and casillaSiguiente < 47:
            casillaSiguiente = casillaSiguiente + 8
        elif casillaSiguiente > 63 and casillaSiguiente < 72:
            casillaSiguiente = casillaSiguiente + 8
        tableroJuego.dtag(ficha, casillaActual)
        tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
        nuevaPosicion = casillas[str(casillaSiguiente)]
        tableroJuego.coords(ficha, nuevaPosicion)
        movimientos.config(text = '0 - 0')
    elif jugador.cget("text") == "Jugador 2":
        tags = tableroJuego.gettags(ficha)
        casillaActual = tags[2]
        try:
            casillaSiguiente = int(casillaActual) + mueve
        except:
            casillaActual = tags[1]
            casillaSiguiente = int(casillaActual) + mueve
        if casillaSiguiente >= 100:
            casillaSiguiente = casillaSiguiente - 100
        if casillaSiguiente > 88 and casillaSiguiente < 97:
            casillaSiguiente = casillaSiguiente + 8
        elif casillaSiguiente > 38 and casillaSiguiente < 47:
            casillaSiguiente = casillaSiguiente + 8
        elif casillaSiguiente > 63 and casillaSiguiente < 72:
            casillaSiguiente = casillaSiguiente + 8
        tableroJuego.dtag(ficha, casillaActual)
        tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
        nuevaPosicion = casillas[str(casillaSiguiente)]
        tableroJuego.coords(ficha, nuevaPosicion)
        movimientos.config(text = '0 - 0')
    elif jugador.cget("text") == "Jugador 3":
        tags = tableroJuego.gettags(ficha)
        casillaActual = tags[2]
        try:
            casillaSiguiente = int(casillaActual) + mueve
        except:
            casillaActual = tags[1]
            casillaSiguiente = int(casillaActual) + mueve
        if casillaSiguiente >= 100:
            casillaSiguiente = casillaSiguiente - 100
        if casillaSiguiente > 13 and casillaSiguiente < 22:
            casillaSiguiente = casillaSiguiente + 8
        elif casillaSiguiente > 88 and casillaSiguiente < 97:
            casillaSiguiente = casillaSiguiente + 8
        elif casillaSiguiente > 63 and casillaSiguiente < 72:
            casillaSiguiente = casillaSiguiente + 8
        tableroJuego.dtag(ficha, casillaActual)
        tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
        nuevaPosicion = casillas[str(casillaSiguiente)]
        tableroJuego.coords(ficha, nuevaPosicion)
        movimientos.config(text = '0 - 0')
    else:
        tags = tableroJuego.gettags(ficha)
        casillaActual = tags[2]
        try:
            casillaSiguiente = int(casillaActual) + mueve
        except:
            casillaActual = tags[1]
            casillaSiguiente = int(casillaActual) + mueve
        if casillaSiguiente >= 100:
            casillaSiguiente = casillaSiguiente - 100
        if casillaSiguiente > 13 and casillaSiguiente < 22:
            casillaSiguiente = casillaSiguiente + 8
        elif casillaSiguiente > 38 and casillaSiguiente < 47:
            casillaSiguiente = casillaSiguiente + 8
        elif casillaSiguiente > 88 and casillaSiguiente < 97:
            casillaSiguiente = casillaSiguiente + 8
        tableroJuego.dtag(ficha, casillaActual)
        tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
        nuevaPosicion = casillas[str(casillaSiguiente)]
        tableroJuego.coords(ficha, nuevaPosicion)
        movimientos.config(text = '0 - 0')

def moverFicha(ficha, movimientos):
    casillas = {
    "0": (94, 345), "1": (122, 345), "2": (150, 345), "3": (178, 345), "4": (206, 345), "5": (246, 380), "6": (246, 408), "7": (246, 436), "8": (246, 464), "9": (246, 492), "10": (246, 520), "11": (246, 548), "12": (246, 576), "13": (275, 580),
    "14": (275, 550), "15": (275, 520), "16": (275, 492), "17": (275, 464), "18": (275, 436), "19": (275, 408), "20": (275, 380), "21": (294, 343), #Casillas Azul
    "22": (342, 580), "23": (342, 550), "24": (342, 520), "25": (342, 492), "26": (342, 464), "27": (342, 436), "28": (342, 408), "29": (342, 380),"30": (380, 341), "31": (408, 341), "32": (436, 341), "33": (464, 341), "34": (492, 341), "35": (520, 341), "36": (548, 341), "37": (576, 341), "38": (580, 312), 
    "39": (548, 312), "40": (520, 312), "41": (492, 312), "42": (464, 312), "43": (436, 312), "44": (408, 312), "45": (380, 312), "46": (343, 294), #Casillas Amarillo
    "47": (580, 245), "48": (548, 245), "49": (520, 245), "50": (492, 245), "51": (464, 245), "52": (436, 245), "53": (408, 245), "54": (380, 245), "55": (340, 208), "56": (340, 180), "57": (340, 152), "58": (340, 124), "59": (340, 96), "60": (340, 68), "61": (340, 40), "62": (340, 12), "63": (312, 12), 
    "64": (312, 40), "65": (312, 68), "66": (312, 96), "67": (312, 124), "68": (312, 152), "69": (312, 180), "70": (312, 208), "71": (294, 243), #Casillas Rojo
    "72": (246, 12), "73": (246, 40), "74": (246, 68), "75": (246, 96), "76": (246, 124), "77": (246, 152), "78": (246, 180), "79": (246, 208), "80": (206, 245), "81": (178, 245), "82": (150, 245), "83": (122, 245), "84": (94, 245), "85": (68, 245), "86": (38, 245), "87": (10, 245), "88": (10, 276), 
    "89": (38, 276), "90": (68, 276), "91": (94, 276), "92": (122, 276), "93": (150, 276), "94": (178, 276), "95": (206, 276), "96": (245, 294), #Casillas Verde
    "97": (10, 345), "98": (38, 345), "99": (68, 345)
    }

    ficha1 = tableroJuego.gettags(FVJ1)
    ficha2 = tableroJuego.gettags(FVJ2)
    ficha3 = tableroJuego.gettags(FVJ3)
    ficha4 = tableroJuego.gettags(FVJ4)
    ficha5 = tableroJuego.gettags(FAJ1)
    ficha6 = tableroJuego.gettags(FAJ2)
    ficha7 = tableroJuego.gettags(FAJ3)
    ficha8 = tableroJuego.gettags(FAJ4)
    ficha9 = tableroJuego.gettags(FAmJ1)
    ficha10 = tableroJuego.gettags(FAmJ2)
    ficha11 = tableroJuego.gettags(FAmJ3)
    ficha12 = tableroJuego.gettags(FAmJ4)
    ficha13 = tableroJuego.gettags(FRJ1)
    ficha14 = tableroJuego.gettags(FRJ2)
    ficha15 = tableroJuego.gettags(FRJ3)
    ficha16 = tableroJuego.gettags(FRJ4)

    movimientosARealizar = movimientos.cget("text")
    movimiento1 = int(movimientosARealizar[0])
    movimiento2 = int(movimientosARealizar[4])
    
    if jugador.cget("text") == "Jugador 1" and (ficha == FVJ1 or ficha == FVJ2 or ficha == FVJ3 or ficha == FVJ4):
        tags = tableroJuego.gettags(ficha)
        if tags[1] == "capturada":
            if movimiento1 == 5:
                tableroJuego.dtag(ficha, "capturada")
                tableroJuego.addtag_withtag("fuera", ficha)
                tableroJuego.addtag_withtag("0", ficha)
                movimientos.config(text= '0 - ' + str(movimiento2))
                nuevaPosicion = casillas["0"]
                tableroJuego.coords(ficha, nuevaPosicion)
                return
            elif movimiento2 == 5:
                tableroJuego.dtag(ficha, "capturada")
                tableroJuego.addtag_withtag("fuera", ficha)
                tableroJuego.addtag_withtag("0", ficha)
                movimientos.config(text= str(movimiento1) + ' - 0')
                nuevaPosicion = casillas["0"]
                tableroJuego.coords(ficha, nuevaPosicion)
                return
        if movimiento1 == 0:
            tags = tableroJuego.gettags(ficha)
            casillaActual = tags[2]
            try:
                casillaSiguiente = int(casillaActual) + movimiento2
            except:
                casillaActual = tags[1]
                casillaSiguiente = int(casillaActual) + movimiento2
            if casillaSiguiente >= 97:
                return
            if casillaSiguiente == 96:
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.dtag(ficha, "dentro")
                tableroJuego.addtag_withtag("ganadora", ficha)
                tableroJuego.addtag_withtag(casillaActual, ficha)
            tags = tableroJuego.gettags(ficha)
            if tags[1] == "ganadora":
                return
            if casillaSiguiente >= 100:
                casillaSiguiente = casillaSiguiente - 100
            if casillaSiguiente > 13 and casillaSiguiente < 22:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 38 and casillaSiguiente < 47:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 63 and casillaSiguiente < 72:
                casillaSiguiente = casillaSiguiente + 8
            tableroJuego.dtag(ficha, casillaActual)
            tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
            nuevaPosicion = casillas[str(casillaSiguiente)]
            tableroJuego.coords(ficha, nuevaPosicion)
            movimientos.config(text = '0 - 0')

            ##Fichas Azules
            try:
                if ficha5[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ1, (438, 435))
            except:
                print("Error")
            try:
                if ficha6[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ2, (438, 550))
            except:
                print("Error")
            try:
                if ficha7[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ3, (550, 435))
            except:
                print("Error")
            try:
                if ficha8[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ4, (550, 550))
            except:
                print("Error")

            #Fichas Amarillas
            try:
                if ficha9[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ1, (438, 35))
            except:
                print("Error")
            try:
                if ficha10[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ2, (438, 150))
            except:
                print("Error")
            try:
                if ficha11[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ3, (550, 35))
            except:
                print("Error")
            try:
                if ficha12[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ4, (550, 150))
            except:
                print("Error")
            
            
            #Fichas Roja
            try:
                if ficha13[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ1, (38, 35))
            except:
                print("Error")
            try:
                if ficha14[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ2, (38, 150))
            except:
                print("Error")
            try:
                if ficha15[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ3, (148, 35))
            except:
                print("Error")
            try:
                if ficha16[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ4, (148, 150))
            except:
                print("Error")

        elif movimiento2 == 0:
            tags = tableroJuego.gettags(ficha)
            casillaActual = tags[2]
            try:
                casillaSiguiente = int(casillaActual) + movimiento2
            except:
                casillaActual = tags[1]
                casillaSiguiente = int(casillaActual) + movimiento2
            if casillaSiguiente >= 97:
                return
            if casillaSiguiente == 96:
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.dtag(ficha, "dentro")
                tableroJuego.addtag_withtag("ganadora", ficha)
                tableroJuego.addtag_withtag(casillaActual, ficha)
            tags = tableroJuego.gettags(ficha)
            if tags[1] == "ganadora":
                return
            if casillaSiguiente >= 100:
                casillaSiguiente = casillaSiguiente - 100  
            if casillaSiguiente > 13 and casillaSiguiente < 22:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 38 and casillaSiguiente < 47:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 63 and casillaSiguiente < 72:
                casillaSiguiente = casillaSiguiente + 8
            tableroJuego.dtag(ficha, casillaActual)
            tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
            nuevaPosicion = casillas[str(casillaSiguiente)]
            tableroJuego.coords(ficha, nuevaPosicion)
            movimientos.config(text = '0 - 0')
            try:
                if ficha5[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ1, (438, 435))
            except:
                print("Error")
            try:
                if ficha6[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ2, (438, 550))
            except:
                print("Error")
            try:
                if ficha7[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ3, (550, 435))
            except:
                print("Error")
            try:
                if ficha8[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ4, (550, 550))
            except:
                print("Error")

            #Fichas Amarillas
            try:
                if ficha9[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ1, (438, 35))
            except:
                print("Error")
            try:
                if ficha10[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ2, (438, 150))
            except:
                print("Error")
            try:
                if ficha11[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ3, (550, 35))
            except:
                print("Error")
            try:
                if ficha12[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ4, (550, 150))
            except:
                print("Error")
            
            
            #Fichas Rojas
            try:
                if ficha13[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ1, (38, 35))
            except:
                print("Error")
            try:
                if ficha14[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ2, (38, 150))
            except:
                print("Error")
            try:
                if ficha15[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ3, (148, 35))
            except:
                print("Error")
            try:
                if ficha16[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ4, (148, 150))
            except:
                print("Error")
        else:
            tags = tableroJuego.gettags(ficha)
            casillaActual = tags[2]
            try:
                casillaSiguiente = int(casillaActual) + movimiento2
            except:
                casillaActual = tags[1]
                casillaSiguiente = int(casillaActual) + movimiento2
            if casillaSiguiente >= 97:
                return
            if casillaSiguiente == 96:
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.dtag(ficha, "dentro")
                tableroJuego.addtag_withtag("ganadora", ficha)
                tableroJuego.addtag_withtag(casillaActual, ficha)
            tags = tableroJuego.gettags(ficha)
            if tags[1] == "ganadora":
                return
            if casillaSiguiente >= 100:
                casillaSiguiente = casillaSiguiente - 100    
            if casillaSiguiente > 13 and casillaSiguiente < 22:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 38 and casillaSiguiente < 47:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 63 and casillaSiguiente < 72:
                casillaSiguiente = casillaSiguiente + 8
            tableroJuego.dtag(ficha, casillaActual)
            tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
            nuevaPosicion = casillas[str(casillaSiguiente)]
            tableroJuego.coords(ficha, nuevaPosicion)
            movimientos.config(text = '0 - ' + str(movimiento2))
            try:
                if ficha5[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ1, (438, 435))
            except:
                print("Error")
            try:
                if ficha6[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ2, (438, 550))
            except:
                print("Error")
            try:
                if ficha7[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ3, (550, 435))
            except:
                print("Error")
            try:
                if ficha8[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ4, (550, 550))
            except:
                print("Error")

            #Fichas Amarillas
            try:
                if ficha9[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ1, (438, 35))
            except:
                print("Error")
            try:
                if ficha10[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ2, (438, 150))
            except:
                print("Error")
            try:
                if ficha11[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ3, (550, 35))
            except:
                print("Error")
            try:
                if ficha12[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ4, (550, 150))
            except:
                print("Error")
            
            
            #Fichas Rojas
            try:
                if ficha13[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ1, (38, 35))
            except:
                print("Error")
            try:
                if ficha14[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ2, (38, 150))
            except:
                print("Error")
            try:
                if ficha15[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ3, (148, 35))
            except:
                print("Error")
            try:
                if ficha16[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ4, (148, 150))
            except:
                print("Error")
    elif jugador.cget("text") == "Jugador 2" and (ficha == FAJ1 or ficha == FAJ2 or ficha == FAJ3 or ficha == FAJ4):
        tags = tableroJuego.gettags(ficha)
        if tags[1] == "capturada":
            if movimiento1 == 5:
                tableroJuego.dtag(ficha, "capturada")
                tableroJuego.addtag_withtag("fuera", ficha)
                tableroJuego.addtag_withtag("25", ficha)
                movimientos.config(text= '0 - ' + str(movimiento2))
                nuevaPosicion = casillas["25"]
                tableroJuego.coords(ficha, nuevaPosicion)
                return
            elif movimiento2 == 5:
                tableroJuego.dtag(ficha, "capturada")
                tableroJuego.addtag_withtag("fuera", ficha)
                tableroJuego.addtag_withtag("25", ficha)
                movimientos.config(text= str(movimiento1) + ' - 0')
                nuevaPosicion = casillas["25"]
                tableroJuego.coords(ficha, nuevaPosicion)
                return
        if movimiento1 == 0:
            tags = tableroJuego.gettags(ficha)
            casillaActual = tags[2]
            try:
                casillaSiguiente = int(casillaActual) + movimiento2
            except:
                casillaActual = tags[1]
                casillaSiguiente = int(casillaActual) + movimiento2
            if casillaSiguiente == 21:
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.dtag(ficha, "dentro")
                tableroJuego.addtag_withtag("ganadora", ficha)
                tableroJuego.addtag_withtag(casillaActual, ficha)
            tags = tableroJuego.gettags(ficha)
            if tags[1] == "ganadora":
                return
            if casillaSiguiente >= 13 and casillaSiguiente <= 21:
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.dtag(ficha, "fuera")
                tableroJuego.addtag_withtag("dentro", ficha)
                tableroJuego.addtag_withtag(casillaActual, ficha)
            tags = tableroJuego.gettags(ficha)
            if casillaSiguiente >= 22 and tags[1] == "dentro":
                casillaSiguiente = casillaSiguiente - movimiento2
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
                nuevaPosicion = casillas[str(casillaSiguiente)]
                tableroJuego.coords(ficha, nuevaPosicion)
                return
            if casillaSiguiente >= 100:
                casillaSiguiente = casillaSiguiente - 100
            if casillaSiguiente > 88 and casillaSiguiente < 97:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 38 and casillaSiguiente < 47:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 63 and casillaSiguiente < 72:
                casillaSiguiente = casillaSiguiente + 8
            tableroJuego.dtag(ficha, casillaActual)
            tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
            nuevaPosicion = casillas[str(casillaSiguiente)]
            tableroJuego.coords(ficha, nuevaPosicion)
            movimientos.config(text = '0 - 0')
            try:
                if ficha1[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ1, (38, 435))
            except:
                print("Error")
            try:
                if ficha2[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ2, (38, 550))
            except:
                print("Error")
            try:
                if ficha3[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ3, (148, 435))
            except:
                print("Error")
            try:
                if ficha4[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ4, (148, 550))
            except:
                print("Error")

            #Fichas Amarillas
            try:
                if ficha9[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ1, (438, 35))
            except:
                print("Error")
            try:
                if ficha10[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ2, (438, 150))
            except:
                print("Error")
            try:
                if ficha11[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ3, (550, 35))
            except:
                print("Error")
            try:
                if ficha12[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ4, (550, 150))
            except:
                print("Error")
            
            
            #Fichas Rojas
            try:
                if ficha13[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ1, (38, 35))
            except:
                print("Error")
            try:
                if ficha14[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ2, (38, 150))
            except:
                print("Error")
            try:
                if ficha15[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ3, (148, 35))
            except:
                print("Error")
            try:
                if ficha16[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ4, (148, 150))
            except:
                print("Error")
        elif movimiento2 == 0:
            tags = tableroJuego.gettags(ficha)
            casillaActual = tags[2]
            try:
                casillaSiguiente = int(casillaActual) + movimiento2
            except:
                casillaActual = tags[1]
                casillaSiguiente = int(casillaActual) + movimiento2
            if casillaSiguiente == 21:
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.dtag(ficha, "dentro")
                tableroJuego.addtag_withtag("ganadora", ficha)
                tableroJuego.addtag_withtag(casillaActual, ficha)
            tags = tableroJuego.gettags(ficha)
            if tags[1] == "ganadora":
                return
            if casillaSiguiente >= 13 and casillaSiguiente <= 21:
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.dtag(ficha, "fuera")
                tableroJuego.addtag_withtag("dentro", ficha)
                tableroJuego.addtag_withtag(casillaActual, ficha)
            tags = tableroJuego.gettags(ficha)
            if casillaSiguiente >= 22 and tags[1] == "dentro":
                casillaSiguiente = casillaSiguiente - movimiento1
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
                nuevaPosicion = casillas[str(casillaSiguiente)]
                tableroJuego.coords(ficha, nuevaPosicion)
                return
            if casillaSiguiente >= 100:
                casillaSiguiente = casillaSiguiente - 100
            if casillaSiguiente > 88 and casillaSiguiente < 100:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 38 and casillaSiguiente < 47:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 63 and casillaSiguiente < 72:
                casillaSiguiente = casillaSiguiente + 8
            tableroJuego.dtag(ficha, casillaActual)
            tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
            nuevaPosicion = casillas[str(casillaSiguiente)]
            tableroJuego.coords(ficha, nuevaPosicion)
            movimientos.config(text = '0 - 0')
            try:
                if ficha1[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ1, (38, 435))
            except:
                print("Error")
            try:
                if ficha2[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ2, (38, 550))
            except:
                print("Error")
            try:
                if ficha3[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ3, (148, 435))
            except:
                print("Error")
            try:
                if ficha4[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ4, (148, 550))
            except:
                print("Error")

            #Fichas Amarillas
            try:
                if ficha9[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ1, (438, 35))
            except:
                print("Error")
            try:
                if ficha10[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ2, (438, 150))
            except:
                print("Error")
            try:
                if ficha11[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ3, (550, 35))
            except:
                print("Error")
            try:
                if ficha12[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ4, (550, 150))
            except:
                print("Error")
            
            
            #Fichas Rojas
            try:
                if ficha13[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ1, (38, 35))
            except:
                print("Error")
            try:
                if ficha14[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ2, (38, 150))
            except:
                print("Error")
            try:
                if ficha15[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ3, (148, 35))
            except:
                print("Error")
            try:
                if ficha16[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ4, (148, 150))
            except:
                print("Error")
        else:
            tags = tableroJuego.gettags(ficha)
            casillaActual = tags[2]
            try:
                casillaSiguiente = int(casillaActual) + movimiento2
            except:
                casillaActual = tags[1]
                casillaSiguiente = int(casillaActual) + movimiento2
            if casillaSiguiente == 21:
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.dtag(ficha, "dentro")
                tableroJuego.addtag_withtag("ganadora", ficha)
                tableroJuego.addtag_withtag(casillaActual, ficha)
            tags = tableroJuego.gettags(ficha)
            if tags[1] == "ganadora":
                return
            if casillaSiguiente >= 13 and casillaSiguiente <= 21:
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.dtag(ficha, "fuera")
                tableroJuego.addtag_withtag("dentro", ficha)
                tableroJuego.addtag_withtag(casillaActual, ficha)
            tags = tableroJuego.gettags(ficha)
            if casillaSiguiente >= 22 and tags[1] == "dentro":
                casillaSiguiente = casillaSiguiente - movimiento1
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
                nuevaPosicion = casillas[str(casillaSiguiente)]
                tableroJuego.coords(ficha, nuevaPosicion)
                return
            if casillaSiguiente >= 100:
                casillaSiguiente = casillaSiguiente - 100
            if casillaSiguiente > 88 and casillaSiguiente < 97:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 38 and casillaSiguiente < 47:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 63 and casillaSiguiente < 72:
                casillaSiguiente = casillaSiguiente + 8
            tableroJuego.dtag(ficha, casillaActual)
            tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
            nuevaPosicion = casillas[str(casillaSiguiente)]
            tableroJuego.coords(ficha, nuevaPosicion)
            movimientos.config(text = '0 - ' + str(movimiento2))
            try:
                if ficha1[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ1, (38, 435))
            except:
                print("Error")
            try:
                if ficha2[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ2, (38, 550))
            except:
                print("Error")
            try:
                if ficha3[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ3, (148, 435))
            except:
                print("Error")
            try:
                if ficha4[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ4, (148, 550))
            except:
                print("Error")

            #Fichas Amarillas
            try:
                if ficha9[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ1, (438, 35))
            except:
                print("Error")
            try:
                if ficha10[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ2, (438, 150))
            except:
                print("Error")
            try:
                if ficha11[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ3, (550, 35))
            except:
                print("Error")
            try:
                if ficha12[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ4, (550, 150))
            except:
                print("Error")
            
            
            #Fichas Rojas
            try:
                if ficha13[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ1, (38, 35))
            except:
                print("Error")
            try:
                if ficha14[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ2, (38, 150))
            except:
                print("Error")
            try:
                if ficha15[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ3, (148, 35))
            except:
                print("Error")
            try:
                if ficha16[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ4, (148, 150))
            except:
                print("Error")
    elif jugador.cget("text") == "Jugador 3" and (ficha == FAmJ1 or ficha == FAmJ2 or ficha == FAmJ3 or ficha == FAmJ4):
        tags = tableroJuego.gettags(ficha)
        if tags[1] == "capturada":
            if movimiento1 == 5:
                tableroJuego.dtag(ficha, "capturada")
                tableroJuego.addtag_withtag("fuera", ficha)
                tableroJuego.addtag_withtag("50", ficha)
                movimientos.config(text= '0 - ' + str(movimiento2))
                nuevaPosicion = casillas["50"]
                tableroJuego.coords(ficha, nuevaPosicion)
                return
            elif movimiento2 == 5:
                tableroJuego.dtag(ficha, "capturada")
                tableroJuego.addtag_withtag("fuera", ficha)
                tableroJuego.addtag_withtag("50", ficha)
                movimientos.config(text= str(movimiento1) + ' - 0')
                nuevaPosicion = casillas["50"]
                tableroJuego.coords(ficha, nuevaPosicion)
                return
        if movimiento1 == 0:
            tags = tableroJuego.gettags(ficha)
            casillaActual = tags[2]
            try:
                casillaSiguiente = int(casillaActual) + movimiento2
            except:
                casillaActual = tags[1]
                casillaSiguiente = int(casillaActual) + movimiento2
            if casillaSiguiente == 46:
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.dtag(ficha, "dentro")
                tableroJuego.addtag_withtag("ganadora", ficha)
                tableroJuego.addtag_withtag(casillaActual, ficha)
            tags = tableroJuego.gettags(ficha)
            if tags[1] == "ganadora":
                return
            if casillaSiguiente >= 38 and casillaSiguiente <= 46:
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.dtag(ficha, "fuera")
                tableroJuego.addtag_withtag("dentro", ficha)
                tableroJuego.addtag_withtag(casillaActual, ficha)
            tags = tableroJuego.gettags(ficha)
            if casillaSiguiente >= 47 and tags[1] == "dentro":
                casillaSiguiente = casillaSiguiente - movimiento2
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
                nuevaPosicion = casillas[str(casillaSiguiente)]
                tableroJuego.coords(ficha, nuevaPosicion)
                return
            if casillaSiguiente >= 100:
                casillaSiguiente = casillaSiguiente - 100
            if casillaSiguiente > 13 and casillaSiguiente < 22:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 88 and casillaSiguiente < 97:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 63 and casillaSiguiente < 72:
                casillaSiguiente = casillaSiguiente + 8
            tableroJuego.dtag(ficha, casillaActual)
            tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
            nuevaPosicion = casillas[str(casillaSiguiente)]
            tableroJuego.coords(ficha, nuevaPosicion)
            movimientos.config(text = '0 - 0')
            try:
                if ficha1[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ1, (38, 435))
            except:
                print("Error")
            try:
                if ficha2[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ2, (38, 550))
            except:
                print("Error")
            try:
                if ficha3[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ3, (148, 435))
            except:
                print("Error")
            try:
                if ficha4[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ4, (148, 550))
            except:
                print("Error")
            

            ##Fichas Azules
            try:
                if ficha5[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ1, (438, 435))
            except:
                print("Error")
            try:
                if ficha6[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ2, (438, 550))
            except:
                print("Error")
            try:
                if ficha7[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ3, (550, 435))
            except:
                print("Error")
            try:
                if ficha8[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ4, (550, 550))
            except:
                print("Error")
            
            #Fichas Rojas
            try:
                if ficha13[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ1, (38, 35))
            except:
                print("Error")
            try:
                if ficha14[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ2, (38, 150))
            except:
                print("Error")
            try:
                if ficha15[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ3, (148, 35))
            except:
                print("Error")
            try:
                if ficha16[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ4, (148, 150))
            except:
                print("Error")
        elif movimiento2 == 0:
            tags = tableroJuego.gettags(ficha)
            casillaActual = tags[2]
            try:
                casillaSiguiente = int(casillaActual) + movimiento2
            except:
                casillaActual = tags[1]
                casillaSiguiente = int(casillaActual) + movimiento1
            if casillaSiguiente == 46:
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.dtag(ficha, "dentro")
                tableroJuego.addtag_withtag("ganadora", ficha)
                tableroJuego.addtag_withtag(casillaActual, ficha)
            tags = tableroJuego.gettags(ficha)
            if casillaSiguiente >= 38 and casillaSiguiente <= 46:
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.dtag(ficha, "fuera")
                tableroJuego.addtag_withtag("dentro", ficha)
                tableroJuego.addtag_withtag(casillaActual, ficha)
            tags = tableroJuego.gettags(ficha)
            if casillaSiguiente >= 47 and tags[1] == "dentro":
                casillaSiguiente = casillaSiguiente - movimiento1
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
                nuevaPosicion = casillas[str(casillaSiguiente)]
                tableroJuego.coords(ficha, nuevaPosicion)
                return
            if casillaSiguiente >= 100:
                casillaSiguiente = casillaSiguiente - 100
            if casillaSiguiente > 13 and casillaSiguiente < 22:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 88 and casillaSiguiente < 97:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 63 and casillaSiguiente < 72:
                casillaSiguiente = casillaSiguiente + 8
            tableroJuego.dtag(ficha, casillaActual)
            tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
            nuevaPosicion = casillas[str(casillaSiguiente)]
            tableroJuego.coords(ficha, nuevaPosicion)
            movimientos.config(text = '0 - 0')
            try:
                if ficha1[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ1, (38, 435))
            except:
                print("Error")
            try:
                if ficha2[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ2, (38, 550))
            except:
                print("Error")
            try:
                if ficha3[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ3, (148, 435))
            except:
                print("Error")
            try:
                if ficha4[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ4, (148, 550))
            except:
                print("Error")

            ##Fichas Azules
            try:
                if ficha5[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ1, (438, 435))
            except:
                print("Error")
            try:
                if ficha6[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ2, (438, 550))
            except:
                print("Error")
            try:
                if ficha7[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ3, (550, 435))
            except:
                print("Error")
            try:
                if ficha8[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ4, (550, 550))
            except:
                print("Error")
            
            #Fichas Rojas
            try:
                if ficha13[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ1, (38, 35))
            except:
                print("Error")
            try:
                if ficha14[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ2, (38, 150))
            except:
                print("Error")
            try:
                if ficha15[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ3, (148, 35))
            except:
                print("Error")
            try:
                if ficha16[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ4, (148, 150))
            except:
                print("Error")
        else:
            tags = tableroJuego.gettags(ficha)
            casillaActual = tags[2]
            try:
                casillaSiguiente = int(casillaActual) + movimiento2
            except:
                casillaActual = tags[1]
                casillaSiguiente = int(casillaActual) + movimiento2
            if casillaSiguiente == 46:
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.dtag(ficha, "dentro")
                tableroJuego.addtag_withtag("ganadora", ficha)
                tableroJuego.addtag_withtag(casillaActual, ficha)
            tags = tableroJuego.gettags(ficha)
            if casillaSiguiente >= 38 and casillaSiguiente <= 46:
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.dtag(ficha, "fuera")
                tableroJuego.addtag_withtag("dentro", ficha)
                tableroJuego.addtag_withtag(casillaActual, ficha)
            tags = tableroJuego.gettags(ficha)
            if casillaSiguiente >= 47 and tags[1] == "dentro":
                casillaSiguiente = casillaSiguiente - movimiento1
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
                nuevaPosicion = casillas[str(casillaSiguiente)]
                tableroJuego.coords(ficha, nuevaPosicion)
                return
            if casillaSiguiente >= 100:
                casillaSiguiente = casillaSiguiente - 100
            if casillaSiguiente > 13 and casillaSiguiente < 22:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 88 and casillaSiguiente < 97:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 63 and casillaSiguiente < 72:
                casillaSiguiente = casillaSiguiente + 8
            tableroJuego.dtag(ficha, casillaActual)
            tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
            nuevaPosicion = casillas[str(casillaSiguiente)]
            tableroJuego.coords(ficha, nuevaPosicion)
            movimientos.config(text = '0 - ' + str(movimiento2))

            try:
                if ficha1[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ1, (38, 435))
            except:
                print("Error")
            try:
                if ficha2[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ2, (38, 550))
            except:
                print("Error")
            try:
                if ficha3[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ3, (148, 435))
            except:
                print("Error")
            try:
                if ficha4[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ4, (148, 550))
            except:
                print("Error")

            ##Fichas Azules
            try:
                if ficha5[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ1, (438, 435))
            except:
                print("Error")
            try:
                if ficha6[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ2, (438, 550))
            except:
                print("Error")
            try:
                if ficha7[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ3, (550, 435))
            except:
                print("Error")
            try:
                if ficha8[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ4, (550, 550))
            except:
                print("Error")
            
            #Fichas Rojas
            try:
                if ficha13[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ1, (38, 35))
            except:
                print("Error")
            try:
                if ficha14[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ2, (38, 150))
            except:
                print("Error")
            try:
                if ficha15[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ3, (148, 35))
            except:
                print("Error")
            try:
                if ficha16[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FRJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FRJ4, (148, 150))
            except:
                print("Error")
    elif jugador.cget("text") == "Jugador 4" and (ficha == FRJ1 or ficha == FRJ2 or ficha == FRJ3 or ficha == FRJ4):
        tags = tableroJuego.gettags(ficha)
        if tags[1] == "capturada":
            if movimiento1 == 5:
                tableroJuego.dtag(ficha, "capturada")
                tableroJuego.addtag_withtag("fuera", ficha)
                tableroJuego.addtag_withtag("75", ficha)
                movimientos.config(text= '0 - ' + str(movimiento2))
                nuevaPosicion = casillas["75"]
                tableroJuego.coords(ficha, nuevaPosicion)
                return
            elif movimiento2 == 5:
                tableroJuego.dtag(ficha, "capturada")
                tableroJuego.addtag_withtag("fuera", ficha)
                tableroJuego.addtag_withtag("75", ficha)
                movimientos.config(text= str(movimiento1) + ' - 0')
                nuevaPosicion = casillas["75"]
                tableroJuego.coords(ficha, nuevaPosicion)
                return
        if movimiento1 == 0:
            tags = tableroJuego.gettags(ficha)
            casillaActual = tags[2]
            try:
                casillaSiguiente = int(casillaActual) + movimiento2
            except:
                casillaActual = tags[1]
                casillaSiguiente = int(casillaActual) + movimiento2
            if casillaSiguiente == 71:
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.dtag(ficha, "dentro")
                tableroJuego.addtag_withtag("ganadora", ficha)
                tableroJuego.addtag_withtag(casillaActual, ficha)
            tags = tableroJuego.gettags(ficha)
            if casillaSiguiente >= 63 and casillaSiguiente <= 71:
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.dtag(ficha, "fuera")
                tableroJuego.addtag_withtag("dentro", ficha)
                tableroJuego.addtag_withtag(casillaActual, ficha)
            tags = tableroJuego.gettags(ficha)
            if casillaSiguiente >= 72 and tags[1] == "dentro":
                casillaSiguiente = casillaSiguiente - movimiento2
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
                nuevaPosicion = casillas[str(casillaSiguiente)]
                tableroJuego.coords(ficha, nuevaPosicion)
                return
            if casillaSiguiente >= 100:
                casillaSiguiente = casillaSiguiente - 100
            if casillaSiguiente > 13 and casillaSiguiente < 22:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 38 and casillaSiguiente < 47:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 88 and casillaSiguiente < 97:
                casillaSiguiente = casillaSiguiente + 8
            tableroJuego.dtag(ficha, casillaActual)
            tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
            nuevaPosicion = casillas[str(casillaSiguiente)]
            tableroJuego.coords(ficha, nuevaPosicion)
            movimientos.config(text = '0 - 0')
            try:
                if ficha1[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ1, (38, 435))
            except:
                print("Error")
            try:
                if ficha2[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ2, (38, 550))
            except:
                print("Error")
            try:
                if ficha3[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ3, (148, 435))
            except:
                print("Error")
            try:
                if ficha4[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ4, (148, 550))
            except:
                print("Error")

            ##Fichas Azules
            try:
                if ficha5[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ1, (438, 435))
            except:
                print("Error")
            try:
                if ficha6[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ2, (438, 550))
            except:
                print("Error")
            try:
                if ficha7[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ3, (550, 435))
            except:
                print("Error")
            try:
                if ficha8[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ4, (550, 550))
            except:
                print("Error")
            
            #Fichas Amarillas
            try:
                if ficha9[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ1, (438, 35))
            except:
                print("Error")
            try:
                if ficha10[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ2, (438, 150))
            except:
                print("Error")
            try:
                if ficha11[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ3, (550, 35))
            except:
                print("Error")
            try:
                if ficha12[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ4, (550, 150))
            except:
                print("Error")
            
        elif movimiento2 == 0:
            tags = tableroJuego.gettags(ficha)
            casillaActual = tags[2]
            try:
                casillaSiguiente = int(casillaActual) + movimiento2
            except:
                casillaActual = tags[1]
                casillaSiguiente = int(casillaActual) + movimiento2
            if casillaSiguiente == 71:
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.dtag(ficha, "dentro")
                tableroJuego.addtag_withtag("ganadora", ficha)
                tableroJuego.addtag_withtag(casillaActual, ficha)
            tags = tableroJuego.gettags(ficha)
            if casillaSiguiente >= 63 and casillaSiguiente <= 71:
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.dtag(ficha, "fuera")
                tableroJuego.addtag_withtag("dentro", ficha)
                tableroJuego.addtag_withtag(casillaActual, ficha)
            tags = tableroJuego.gettags(ficha)
            if casillaSiguiente >= 72 and tags[1] == "dentro":
                casillaSiguiente = casillaSiguiente - movimiento1
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
                nuevaPosicion = casillas[str(casillaSiguiente)]
                tableroJuego.coords(ficha, nuevaPosicion)
                return
            if casillaSiguiente >= 100:
                casillaSiguiente = casillaSiguiente - 100
            if casillaSiguiente > 13 and casillaSiguiente < 22:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 38 and casillaSiguiente < 47:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 88 and casillaSiguiente < 97:
                casillaSiguiente = casillaSiguiente + 8
            tableroJuego.dtag(ficha, casillaActual)
            tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
            nuevaPosicion = casillas[str(casillaSiguiente)]
            tableroJuego.coords(ficha, nuevaPosicion)
            movimientos.config(text = '0 - 0')
            try:
                if ficha1[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ1, (38, 435))
            except:
                print("Error")
            try:
                if ficha2[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ2, (38, 550))
            except:
                print("Error")
            try:
                if ficha3[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ3, (148, 435))
            except:
                print("Error")
            try:
                if ficha4[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ4, (148, 550))
            except:
                print("Error")

            ##Fichas Azules
            try:
                if ficha5[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ1, (438, 435))
            except:
                print("Error")
            try:
                if ficha6[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ2, (438, 550))
            except:
                print("Error")
            try:
                if ficha7[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ3, (550, 435))
            except:
                print("Error")
            try:
                if ficha8[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ4, (550, 550))
            except:
                print("Error")
            
            #Fichas Amarillas
            try:
                if ficha9[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ1, (438, 35))
            except:
                print("Error")
            try:
                if ficha10[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ2, (438, 150))
            except:
                print("Error")
            try:
                if ficha11[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ3, (550, 35))
            except:
                print("Error")
            try:
                if ficha12[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ4, (550, 150))
            except:
                print("Error")
            
        else:
            tags = tableroJuego.gettags(ficha)
            casillaActual = tags[2]
            try:
                casillaSiguiente = int(casillaActual) + movimiento2
            except:
                casillaActual = tags[1]
                casillaSiguiente = int(casillaActual) + movimiento2
            if casillaSiguiente == 71:
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.dtag(ficha, "dentro")
                tableroJuego.addtag_withtag("ganadora", ficha)
                tableroJuego.addtag_withtag(casillaActual, ficha)
            tags = tableroJuego.gettags(ficha)
            if casillaSiguiente >= 63 and casillaSiguiente <= 71:
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.dtag(ficha, "fuera")
                tableroJuego.addtag_withtag("dentro", ficha)
                tableroJuego.addtag_withtag(casillaActual, ficha)
            tags = tableroJuego.gettags(ficha)
            if casillaSiguiente >= 72 and tags[1] == "dentro":
                casillaSiguiente = casillaSiguiente - movimiento1
                tableroJuego.dtag(ficha, casillaActual)
                tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
                nuevaPosicion = casillas[str(casillaSiguiente)]
                tableroJuego.coords(ficha, nuevaPosicion)
                return
            if casillaSiguiente >= 100:
                casillaSiguiente = casillaSiguiente - 100
            if casillaSiguiente > 13 and casillaSiguiente < 22:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 38 and casillaSiguiente < 47:
                casillaSiguiente = casillaSiguiente + 8
            elif casillaSiguiente > 88 and casillaSiguiente < 97:
                casillaSiguiente = casillaSiguiente + 8
            tableroJuego.dtag(ficha, casillaActual)
            tableroJuego.addtag_withtag(str(casillaSiguiente), ficha)
            nuevaPosicion = casillas[str(casillaSiguiente)]
            tableroJuego.coords(ficha, nuevaPosicion)
            movimientos.config(text = '0 - ' + str(movimiento2))
            try:
                if ficha1[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ1, (38, 435))
            except:
                print("Error")
            try:
                if ficha2[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ2, (38, 550))
            except:
                print("Error")
            try:
                if ficha3[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ3, (148, 435))
            except:
                print("Error")
            try:
                if ficha4[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FVJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FVJ4, (148, 550))
            except:
                print("Error")

            ##Fichas Azules
            try:
                if ficha5[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ1, (438, 435))
            except:
                print("Error")
            try:
                if ficha6[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ2, (438, 550))
            except:
                print("Error")
            try:
                if ficha7[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ3, (550, 435))
            except:
                print("Error")
            try:
                if ficha8[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAJ4, (550, 550))
            except:
                print("Error")
            
            #Fichas Amarillas
            try:
                if ficha9[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ1, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ1, (438, 35))
            except:
                print("Error")
            try:
                if ficha10[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ2, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ2, (438, 150))
            except:
                print("Error")
            try:
                if ficha11[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ3, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ3, (550, 35))
            except:
                print("Error")
            try:
                if ficha12[2] == str(casillaSiguiente):
                    tableroJuego.dtag(FAmJ4, str(casillaSiguiente))
                    tableroJuego.dtag(ficha, "fuera")
                    tableroJuego.addtag_withtag("capturada", ficha)
                    tableroJuego.coords(FAmJ4, (550, 150))
            except:
                print("Error")
            

def UI(ventana):
    ventana.geometry("1280x720")
    ventana.resizable(width = False, height = False)
    ventana.title("Parchis")
    centra(ventana, 1280, 720)

    global tablero
    tablero = PhotoImage(file = "Tablero.png")

    dado1 = PhotoImage(file = 'Dado1.png')

    global roja, azul, amarilla, verde
    roja = PhotoImage(file = 'Roja.png')
    azul = PhotoImage(file = 'Azul.png')
    amarilla = PhotoImage(file = 'Amarilla.png')
    verde = PhotoImage(file = 'Verde.png')

    global tableroJuego
    tableroJuego = Canvas(ventana, highlightthickness=0, width=608, height=608)
    tableroJuego.place(x=40, y=40)
    tableroJuego.create_image(0, 0, anchor="nw", image=tablero)


    #Jugador 1
    global FVJ1, FVJ2, FVJ3, FVJ4
    FVJ1 = tableroJuego.create_image(38,435,anchor = "nw", tags="verde", image=verde)
    tableroJuego.addtag_withtag("capturada", FVJ1)
    tableroJuego.tag_bind(FVJ1, "<Button-1>", lambda event: moverFicha(FVJ1, movimientos))
    FVJ2 = tableroJuego.create_image(38,550,anchor = "nw", tags="verde", image=verde)
    tableroJuego.addtag_withtag("capturada", FVJ2)
    tableroJuego.tag_bind(FVJ2, "<Button-1>", lambda event: moverFicha(FVJ2, movimientos))
    FVJ3 = tableroJuego.create_image(148,435,anchor = "nw", tags="verde", image=verde)
    tableroJuego.addtag_withtag("capturada", FVJ3)
    tableroJuego.tag_bind(FVJ3, "<Button-1>", lambda event: moverFicha(FVJ3, movimientos))
    FVJ4 = tableroJuego.create_image(148,550,anchor = "nw", tags="verde", image=verde)
    tableroJuego.addtag_withtag("capturada", FVJ4)
    tableroJuego.tag_bind(FVJ4, "<Button-1>", lambda event: moverFicha(FVJ4, movimientos))

    #Jugador 2
    global FAJ1, FAJ2, FAJ3, FAJ4
    FAJ1 = tableroJuego.create_image(438,435,anchor = "nw", tags="azul", image=azul)
    tableroJuego.addtag_withtag("capturada", FAJ1)
    tableroJuego.tag_bind(FAJ1, "<Button-1>", lambda event: moverFicha(FAJ1, movimientos))
    FAJ2 = tableroJuego.create_image(438,550,anchor = "nw", tags="azul", image=azul)
    tableroJuego.addtag_withtag("capturada", FAJ2)
    tableroJuego.tag_bind(FAJ2, "<Button-1>", lambda event: moverFicha(FAJ2, movimientos))
    FAJ3 = tableroJuego.create_image(550,435,anchor = "nw", tags="azul", image=azul)
    tableroJuego.addtag_withtag("capturada", FAJ3)
    tableroJuego.tag_bind(FAJ3, "<Button-1>", lambda event: moverFicha(FAJ3, movimientos))
    FAJ4 = tableroJuego.create_image(550,550,anchor = "nw", tags="azul", image=azul)
    tableroJuego.addtag_withtag("capturada", FAJ4)
    tableroJuego.tag_bind(FAJ4, "<Button-1>", lambda event: moverFicha(FAJ4, movimientos))

    #Jugador 3
    global FAmJ1, FAmJ2, FAmJ3, FAmJ4
    FAmJ1 = tableroJuego.create_image(438,35,anchor = "nw", tags="amarillo", image=amarilla)
    tableroJuego.addtag_withtag("capturada", FAmJ1)
    tableroJuego.tag_bind(FAmJ1, "<Button-1>", lambda event: moverFicha(FAmJ1, movimientos))
    FAmJ2 = tableroJuego.create_image(438,150,anchor = "nw", tags="amarillo", image=amarilla)
    tableroJuego.addtag_withtag("capturada", FAmJ2)
    tableroJuego.tag_bind(FAmJ2, "<Button-1>", lambda event: moverFicha(FAmJ2, movimientos))
    FAmJ3 = tableroJuego.create_image(550,35,anchor = "nw", tags="amarillo", image=amarilla)
    tableroJuego.addtag_withtag("capturada", FAmJ3)
    tableroJuego.tag_bind(FAmJ3, "<Button-1>", lambda event: moverFicha(FAmJ3, movimientos))
    FAmJ4 = tableroJuego.create_image(550,150,anchor = "nw", tags="amarillo", image=amarilla)
    tableroJuego.addtag_withtag("capturada", FAmJ4)
    tableroJuego.tag_bind(FAmJ4, "<Button-1>", lambda event: moverFicha(FAmJ4, movimientos))

    #Jugador 4
    global FRJ1, FRJ2, FRJ3, FRJ4
    FRJ1 = tableroJuego.create_image(38,35,anchor = "nw", tags="rojo", image=roja)
    tableroJuego.addtag_withtag("capturada", FRJ1)
    tableroJuego.tag_bind(FRJ1, "<Button-1>", lambda event: moverFicha(FRJ1, movimientos))
    FRJ2 = tableroJuego.create_image(38,150,anchor = "nw", tags="rojo", image=roja)
    tableroJuego.addtag_withtag("capturada", FRJ2)
    tableroJuego.tag_bind(FRJ2, "<Button-1>", lambda event: moverFicha(FRJ2, movimientos))
    FRJ3 = tableroJuego.create_image(148,35,anchor = "nw", tags="rojo", image=roja)
    tableroJuego.addtag_withtag("capturada", FRJ3)
    tableroJuego.tag_bind(FRJ3, "<Button-1>", lambda event: moverFicha(FRJ3, movimientos))
    FRJ4 = tableroJuego.create_image(148,150,anchor = "nw", tags="rojo", image=roja)
    tableroJuego.addtag_withtag("capturada", FRJ4)
    tableroJuego.tag_bind(FRJ4, "<Button-1>", lambda event: moverFicha(FRJ4, movimientos))

    #Dados
    dados = Canvas(ventana, highlightthickness=0, width=370, height=175)
    dados.place(x=800,y=100)
    primerDado = dados.create_image(0, 0, anchor="nw", image=dado1)
    segundoDado = dados.create_image(175, 0, anchor="nw", image=dado1)

    #Jugador actual
    global jugador
    jugador = Label(text = 'Jugador 1', font = ('Calibri Light Bold', 30))
    jugador.place(x = 890, y = 45)

    #Movimientos
    movimientos = Label(text = '0 - 0', font = ('Calibri Light Bold', 30))
    movimientos.place(x = 920, y = 375)

    #Fin de Turno
    global finalTurno
    finalTurno = Button(text = 'Fin Turno', width = 9, bg = 'gainsboro', activebackground = 'darkcyan', state="disabled", command = lambda: finTurno())
    finalTurno.place(x = 930, y = 500)

    #Lanzar Dados
    global lanzar
    lanzar = Button(text = 'Lanzar', width = 9, bg = 'gainsboro', activebackground = 'darkcyan', command = lambda: lanzarDados(dados, primerDado, segundoDado, movimientos))
    lanzar.place(x = 930, y = 300)

ventana = Tk()
aplicación = UI(ventana)
ventana.mainloop()