
import Calculadora

if __name__=="__main__":
    valorInicial=float(input("Entre o valorInicial:"))
    calc = Calculadora.Calculadora(valorInicial)
    operador=float(input("Entre o operador:"))
    calc.somar(operador)
    print(calc.valor)
    operador = float(input("Digite um novo valor para soma"))
    calc.somar(operador)
    print(calc.valor)
