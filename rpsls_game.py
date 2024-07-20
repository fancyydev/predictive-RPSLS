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
previous_game_turn = None
current_game_turn = None
human_score = 0
machine_score = 0

def results(human_option, machine_option):
    #Si eligen lo mismo es empate
    if(human_option == machine_option):
        return None
    elif (human_option == "piedra" and (machine_option == "tijera" or machine_option == "lagarto")):
        return True 
    elif(human_option == "papel" and (machine_option == "piedra" or machine_option == "spock")):
        return True
    elif(human_option == "tijera" and (machine_option == "papel" or machine_option == "lagarto")):
        return True
    elif(human_option == "lagarto" and (machine_option == "spock" or machine_option == "papel")):
        return True
    elif(human_option == "spock" and (machine_option == "tijera" or machine_option == "piedra")):
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

def get_choice(option = None, index = None):
    if (option == "piedra" or index == 0):
        return 0, "piedra" 
    elif(option == "papel" or index == 1):
        return 1, "papel"
    elif(option == "tijera" or index == 2):
        return 2, "tijera"
    elif(option == "lagarto" or index == 3):
        return 3, "lagarto"
    else:
        return 4, "spock"

def play(human_option):
    global transition_table
    global previous_game_turn
    global current_game_turn
    global human_score
    global machine_score

    ban = False

    current_game_turn = human_option
    current_game_turn_index = get_choice(option=current_game_turn)[0]

    if (previous_game_turn == None):
        previous_game_turn = current_game_turn
        ban = True

    #Nos devuelve la fila de la matriz que le corresponde
    #a la option anterior
    previous_game_turn_index = get_choice(option=previous_game_turn)[0]
    #Obtenemos el valor mas grande dentro de esa fila
    max_value = max(transition_table[previous_game_turn_index])
    #Si el valor maximo se repite obtenemos un arreglo con las posiciones del valor mas grande
    index_max_values = get_max_indices(transition_table[previous_game_turn_index], max_value)
    #Como puede haber varias opciones con la misma probabilidad
    #Se escoje el indice de una al azar 
    machine_choice_index = index_max_values[random.randint(0,len(index_max_values)-1)]
    machine_choice_name = get_choice(index=machine_choice_index)[1]
    #En base a la prediccion retornamos un valor que le gane
    machine_choice_name = tryWinMachine(machine_choice_name)

    #Configuramos la imagen de la opcion de el usuario 
    img = Image.open(f"{human_option}.png")
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

    result_ban = results(human_option, machine_choice_name)
    if result_ban == None:
        msg_result.set("EMPATE")
    elif result_ban:
        human_score = human_score + 1
        msg_human.set(f"HUMANO: {human_score}")
        msg_result.set("GANASTE")
    else:
        machine_score = machine_score + 1
        msg_machine.set(f"MAQUINA: {machine_score}")
        msg_result.set("PERDISTE")
    
    #Guardamos dentro del renglon de option anterior lo elegido por el usuario para tener en cuenta su probabilidad
    if (ban == False):
        transition_table[previous_game_turn_index][current_game_turn_index] = transition_table[previous_game_turn_index][current_game_turn_index] + 1 

    previous_game_turn = current_game_turn



root = Tk()
root.geometry("900x600")
root.configure(bg = "gray")
root.title("PIEDRA PAPEL O TIJERA")

#declaramos los label que contendran el conteo de ganados
Label(root, text = "RESULTADO", font = ("Derive Unicode", 25), bg = 'white smoke').pack()
msg_human = StringVar()
msg_human.set("HUMANO: 0")
lbl_human = Label(root, textvariable=msg_human, font = ("Derive Unicode", 25), bg = 'white smoke').place(x=50,y=10)

msg_machine = StringVar()
msg_machine.set("MAQUINA: 0")
lbl_machine = Label(root, textvariable=msg_machine, font = ("Derive Unicode", 25), bg = 'white smoke').place(x=650,y=10)

#Declaramos el lbl que indicara si gano o perdio el usario al momento de estar jugando
msg_result = StringVar()
lbl_result = Label(root, textvariable=msg_result, font = ("Derive Unicode", 25), bg = 'gray').place(x=362,y=120)

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