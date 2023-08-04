# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas 
# de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.​
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;​
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 
# e quatro notas de 1.

def caixa(saque):
    notas_disp = [100, 50, 10, 5 , 1]
    qtd_notas = [0, 0, 0, 0, 0]

    if (saque < 10 or saque > 600):
        print("Valor inválido, o valor mínimo é 10 reais e o valor máximo é 600 reais")
        return 0
    
    for i in range(len(notas_disp)):
        qtd_notas[i] = saque // notas_disp[i]
        saque %= notas_disp[i]
    
    print("-=" * 20)
    print("Quantidade de notas: ")
    for i in range(len(notas_disp)):
        if (qtd_notas[i] > 0):
          print(f"{qtd_notas[i]} de notas de {notas_disp[i]} dolares")
        

# Main
saque = int(input("Valor que deseja sacar: "))
caixa(saque)
