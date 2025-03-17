#para se criar uma função usamos a palavra def 

def imprimirNomeCurso():
    print("Curso de python")

imprimirNomeCurso()

#Parametro de função quando a funcao é chamada sao passados valores para essas variaveis

def calcularAreadoTriangulo(base,altura):
    area = (base * altura) / 2
    print(f"Area do triangulo = ", area)

calcularAreadoTriangulo(10,20)

base = float(input("valor 1: "))
altura = float(input("valor 2: "))

def cal(base, altura):
    area = (base * altura) / 2


