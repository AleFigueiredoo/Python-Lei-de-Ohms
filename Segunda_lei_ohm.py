def calculo_corrente():
    r = float(input("Digite o valor da resistência em Ohms: "))
    v = float(input("Digite o valor da tensão: "))
    return round(v / r,3)

def calculo_tensao():
    r = float(input("Digite o valor da resistência em Ohms: "))
    i = float(input("Digite o valor da Corrente: "))
    return round(r * i)

def calculo_resistencia():
    v = float(input("Digite o valor da tensão: "))
    i = float(input("Digite o valor da Corrente: "))
    return round(v / i,3)

def calculo_potencia():
    v = float(input("Digite o valor da tensão: "))
    i = float(input("Digite o valor da Corrente: "))
    return round(v * i,3)

def entrada():
    letra = input("Digite:\n\"R\" para resistência   "
              "\n\"I\" para corrente  "
              "\n\"V\" para tensão "
              "\n\"P\" para potência  "
              "\n\"S\" para sair - ").upper()
    return letra

def selecao(letra):
    while letra != "S":
        if letra =="I":
           i = calculo_corrente()
           print("O valor da corrente é", i, "A.")
           return

        if letra =="V":
            v = calculo_tensao()
            print("O valor da tensão é", v, "V")
            return

        if letra == "R":
            r = calculo_resistencia()
            print("O valor da resitência é ", r, "ohms")
            return

        if letra == "P":
            p = calculo_potencia()
            print("O valor da potência é ", p, "W")
            return
    return "S"

def main():
    letra = entrada()
    while letra != "S":
        calculo = selecao(letra)
        print()
        letra = entrada()
    print("Fim do calculo !")

main()

