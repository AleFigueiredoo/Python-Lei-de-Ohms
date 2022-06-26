def calculo_corrente():
    r = float(input("Digite o valor da resistência em Ohms: "))
    v = float(input("Digite o valor da tensão: "))
    print("O valor da corrente é", round(v / r,3), "A")
    return

def calculo_tensao():
    r = float(input("Digite o valor da resistência em Ohms: "))
    i = float(input("Digite o valor da Corrente: "))
    print("O valor da tensão é", round(r * i), "V")
    return

def calculo_resistencia():
    v = float(input("Digite o valor da tensão: "))
    i = float(input("Digite o valor da Corrente: "))
    print("O valor da resitência é ", round(v / i,3), "ohms")
    return

def calculo_potencia():
    v = float(input("Digite o valor da tensão: "))
    i = float(input("Digite o valor da Corrente: "))
    print("O valor da potência é ", round(v * i,3), "W")
    return

letra = input("Digite:\n\"R\" para resistência   "
              "\n\"I\" para corrente  "
              "\n\"V\" para tensão "
              "\n\"P\" para potência  "
              "\n\"S\" para sair - ").upper()
print()
    
while letra != "S":
    if letra =="I":
       i = calculo_corrente()

    if letra =="V":
        v = calculo_tensao()

    if letra == "R":
        r = calculo_resistencia()

    if letra == "P":
        p = calculo_potencia()

    if letra != "S":
        letra = input("Digite o que quer calcular ou \"S\" para sair: ").upper()

print("Fim do calculo !")
