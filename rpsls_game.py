from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

#0 = Piedra
#1 = Papel
#2 = Tijera
#3 = Lagarto
#4 = Spock
transition_table = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
tirada_anterior = None
tirada_actual = None
puntuacion_humano = 0
puntuacion_maquina = 0

def results(opcion_humano, opcion_maquina):
    #Si eligen lo mismo es empate
    if(opcion_humano == opcion_maquina):
        return None
    elif (opcion_humano == "piedra" and (opcion_maquina == "tijera" or opcion_maquina == "lagarto")):
        return True 
    elif(opcion_humano == "papel" and (opcion_maquina == "piedra" or opcion_maquina == "spock")):
        return True
    elif(opcion_humano == "tijera" and (opcion_maquina == "papel" or opcion_maquina == "lagarto")):
        return True
    elif(opcion_humano == "lagarto" and (opcion_maquina == "spock" or opcion_maquina == "papel")):
        return True
    elif(opcion_humano == "spock" and (opcion_maquina == "tijera" or opcion_maquina == "piedra")):
        return True
    else:
        return False
    
def tryWinMachine(possible_option):
    opc = random.randint(1,2)
    if (possible_option == "piedra"):
        if (opc == 1):
            return "papel"
        else:
            return "spock"
    if (possible_option == "papel"):
        if (opc == 1):
            return "tijera"
        else:
            return "lagarto"
    if (possible_option == "tijera"):
        if (opc == 1):
            return "piedra"
        else:
            return "spock"
    if (possible_option == "lagarto"):
        if (opc == 1):
            return "tijera"
        else:
            return "piedra"
    if (possible_option == "spock"):
        if (opc == 1):
            return "papel"
        else:
            return "lagarto"


def get_max_indices(ls,value):
    return [i for i in range(len(ls)) if ls[i] == value]

def get_choice(tirada = None, index = None):
    if (tirada == "piedra" or index == 0):
        return 0, "piedra" 
    elif(tirada == "papel" or index == 1):
        return 1, "papel"
    elif(tirada == "tijera" or index == 2):
        return 2, "tijera"
    elif(tirada == "lagarto" or index == 3):
        return 3, "lagarto"
    else:
        return 4, "spock"

def play(opcion_humano):
    global transition_table
    global tirada_anterior
    global tirada_actual
    global puntuacion_humano
    global puntuacion_maquina

    ban = False

    tirada_actual = opcion_humano
    tirada_actual_index = get_choice(tirada=tirada_actual)[0]

    if (tirada_anterior == None):
        tirada_anterior = tirada_actual
        ban = True

    #Nos devuelve la fila de la matriz que le corresponde
    #a la tirada anterior
    tirada_anterior_index = get_choice(tirada=tirada_anterior)[0]
    #Obtenemos el valor mas grande dentro de esa fila
    max_value = max(transition_table[tirada_anterior_index])
    #Si el valor maximo se repite obtenemos un arreglo con las posiciones del valor mas grande
    index_max_values = get_max_indices(transition_table[tirada_anterior_index], max_value)
    #Como puede haber varias opciones con la misma probabilidad
    #Se escoje el indice de una al azar 
    machine_choice_index = index_max_values[random.randint(0,len(index_max_values)-1)]
    machine_choice_name = get_choice(index=machine_choice_index)[1]
    #En base a la prediccion retornamos un valor que le gane
    machine_choice_name = tryWinMachine(machine_choice_name)

    #Configuramos la imagen de la opcion de el usuario 
    img = Image.open(f"{opcion_humano}.png")
    img = img.resize((200, 200))
    img = ImageTk.PhotoImage(img)
    
    img_human.configure(image=img)
    img_human.image=img

    #Configuramos la imagen de la opcion de la maquina
    img = Image.open(f"{machine_choice_name}.png")
    img = img.resize((200, 200))
    img = ImageTk.PhotoImage(img)
 
    img_robot.configure(image=img)
    img_robot.image=img

    result_ban = results(opcion_humano, machine_choice_name)
    if result_ban == None:
        msg_resultado.set("EMPATE")
    elif result_ban:
        puntuacion_humano = puntuacion_humano + 1
        msg_human.set(f"HUMANO: {puntuacion_humano}")
        msg_resultado.set("GANASTE")
    else:
        puntuacion_maquina = puntuacion_maquina + 1
        msg_maquina.set(f"MAQUINA: {puntuacion_maquina}")
        msg_resultado.set("PERDISTE")
    
    #Guardamos dentro del renglon de tirada anterior lo elegido por el usuario para tener en cuenta su probabilidad
    if (ban == False):
        transition_table[tirada_anterior_index][tirada_actual_index] = transition_table[tirada_anterior_index][tirada_actual_index] + 1 

    tirada_anterior = tirada_actual



root = Tk()
root.geometry("900x600")
root.configure(bg = "gray")
root.title("PIEDRA PAPEL O TIJERA")

#declaramos los label que contendran el conteo de ganados
Label(root, text = "RESULTADO", font = ("Derive Unicode", 25), bg = 'white smoke').pack()
msg_human = StringVar()
msg_human.set("HUMANO: 0")
lbl_human = Label(root, textvariable=msg_human, font = ("Derive Unicode", 25), bg = 'white smoke').place(x=50,y=10)

msg_maquina = StringVar()
msg_maquina.set("MAQUINA: 0")
lbl_maquina = Label(root, textvariable=msg_maquina, font = ("Derive Unicode", 25), bg = 'white smoke').place(x=650,y=10)

#Declaramos el lbl que indicara si gano o perdio el usario al momento de estar jugando
msg_resultado = StringVar()
lbl_resultado = Label(root, textvariable=msg_resultado, font = ("Derive Unicode", 25), bg = 'gray').place(x=362,y=120)

#Declaramos el lbl que contendra la imagen seleccionada por el usuario
img_human = ttk.Label(root, text="", background="gray")
img_human.place(x=50,y=80)
#Declaramos el lbl que contendra la imagen seleccionada por la maquina
img_robot = ttk.Label(root, text="", background="gray")
img_robot.place(x=650,y=80)

Button(root, text = "PIEDRA" , font = ('Derive Unicode', 25), width=10, command=lambda:play("piedra")).place(x=350, y=220)
Button(root,text = 'PAPEL',font = ('Derive Unicode', 25), width=10, command=lambda:play("papel")).place(x=350,y=290)
Button(root, text = 'TIJERA', font=('Derive Unicode', 25), width=10, command=lambda:play("tijera")).place(x=350 , y =360)
Button(root, text = "SPOCK" , font = ('Derive Unicode', 25), width=10, command=lambda:play("spock")).place(x=350, y=430)
Button(root,text = 'LAGARTO',font = ('Derive Unicode', 25), width=10, command=lambda:play("lagarto")).place(x=350,y=500)
root.mainloop()