##Definir as variaveis
combustivel = 110
tripulantes = []

##definir funçoes

def viajar():
    ##aqui vamos gastar combustivel
    global combustivel ##modificar uma variavel externa
    if(combustivel>=30):
         combustivel = combustivel - 30
         print("a nave viajou")
    else:
        print("voce esta sem combustivel suficinte.Abasteça!")

def abastecer():
    global combustivel
    combustivel = 110
    print("Tanque cheio! ⛽")

def status_nave():
    print("\n----- STATUS DA NAVE -----")
    print(f"Temos {combustivel} de combustivel")
    print(f"Os tripulantes são: {tripulantes}")


def RegistrarTripulante():
    novoTripulante = input("Qual o nome do novo tripulante?:")
    tripulantes.append(novoTripulante)
    print("Tripulante inserido com sucesso! 🚀🚀")

status_nave()
RegistrarTripulante()
status_nave()

##criar menu

while True:
    print("\nBem vindo ao menu interativo da nave.Por favor,selecione uma opção:")
    print("\n1- Mostrar status da nave | 2-Viajar | 3-abastecer | 4-novo tripulante | 5-sair")

    opcao = input ("Escolha: ")

    if (opcao == 1):
        status_nave()
    elif(opcao == "2"):
        viajar()
    elif(opcao == "3"):
        abastecer()
    elif(opcao == "4"):
        RegistrarTripulante()
    elif(opcao == "5"):
        print("Viagem encerrada! ")
        break




# status_nave()
# viajar()
# viajar()
# status_nave()
# viajar()
# viajar()
# abastecer()
# viajar()
# status_nave()