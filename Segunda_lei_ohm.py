def calculo_corrente():
    r, v = input("Entre com valor da resistência e tensão separado por virgula.\n").split(",")
    resultado = round(float(v)/float(r),3)
    return resultado

def calculo_tensao():
    r, i = input("Entre com valor da resistência e corrente separado por virgula.\n").split(",")
    resultado = round(float(r) * float(i))
    return resultado

def calculo_resistencia():
    v, i = input("Entre com valor da tensão e corrente separado por virgula.\n").split(",")
    resultado = round(float(v) / float(i),3)
    return resultado

def calculo_potencia():
    v, i = input("Entre com valor da tensão e corrente separado por virgula.\n").split(",")
    resultado = round(float(v) * float(i),3)
    return resultado

def entrada():
    print(f"** Escolha a opção que deseja calcular. **\n"
          f"'R' para resistência\n"
          f"'I' para corrente\n"
          f"'V' para tensão\n"
          f"'P' para potência\n"
          f"'E' para sair")
    letra = input(f"Selecione a opção!\n").upper()
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
    return

def main():
    letra = entrada()
    while letra != "E" and letra != "N":
        calculo = selecao(letra)
        continua = input(f"Deseja novo Calculo? (S/N)\n").upper()
        if continua == "S":
            letra = entrada()
        else:
            letra = continua
    print("Fim do calculo !")

main()

