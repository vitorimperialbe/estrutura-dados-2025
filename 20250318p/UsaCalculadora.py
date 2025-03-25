import Calculadora

if __name__=="__main__":
    valorInicial=float(input("Entre o valorInicial:"))
    calc = Calculadora.Calculadora(valorInicial)
    operacao=0
    while operacao!=5:

        operacao=int(input("Entre o operador:\n1 para somar\n2 para subtrair\n3 para multiplicar\n4 para dividir\n5 para sair\n"))
        if operacao == 5:
            print("Valor final: ")
            print(calc.valor)
            break

        valorOperador = float(input("Informe o valor a ser utilizado na operação:"))
        if operacao == 1:
            calc.somar(valorOperador)
        elif operacao == 2:
            calc.subtrair(valorOperador)
        elif operacao == 3:
            calc.multiplicar(valorOperador)
        elif operacao == 4:
            calc.dividir(valorOperador)
        else:
            print("Valor da operação inválido")

