import math
import random

# Funções
def verificaPrimo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def gerador():
    num1 = random.randint(100, 500)
    num2 = random.randint(100, 500)

    while not verificaPrimo(num1):
        num1 += 1
    while not verificaPrimo(num2) or num1 == num2:
        num2 += 1

    return num1, num2

def coprimos(e, t):
    return math.gcd(e, t) == 1

def euclides_estendido(a, b):
    if a == 0:
        return 0, 1, b

    x1, y1, mdc = euclides_estendido(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return x, y, mdc

def encontrar_d(e, totiente_n):
    x, y, gcd = euclides_estendido(e, totiente_n)
    if gcd != 1:
        raise Exception('e e totiente_n não são coprimos')
    
    d = x % totiente_n
    return d

def encriptar(mensagem, e, n):
    mensagem_cifrada = []
    for i in mensagem:
        m = ord(i)
        c = pow(m, e, n)
        mensagem_cifrada.append(c)
    return mensagem_cifrada

def decriptar(mensagem_cifrada, d, n):
    mensagem_original = ""
    for i in mensagem_cifrada:
        m = pow(i, d, n)
        mensagem_original += chr(m)
    return mensagem_original

# Geração de chaves e inicio do algoritmo de fato
p, q = gerador()
print(f"p: {p}\nq: {q}")

n = p * q
print(f"n: {n}")

totiente_n = (p - 1) * (q - 1)
print(f"totiente_n: {totiente_n}")

e = random.randint(2, totiente_n - 1)
while not coprimos(e, totiente_n):
    e = random.randint(2, totiente_n - 1)
print(f"Chave pública 'e' = {e}")

d = encontrar_d(e, totiente_n)
print(f"Chave privada 'd' = {d}")

print(f"\nChave Pública (n, e): ({n}, {e})")
print(f"Chave Privada (n, d): ({n}, {d})")

# O menu tá aq
while True:
    print("\n1. Gerar novas chaves")
    print("2. Encriptar uma mensagem")
    print("3. Decriptar uma mensagem")
    print("4. Sair\n")
    
    try:
        opcao = int(input("Escolha sua ação: "))
    except ValueError:
        print("Opção inválida. Por favor, digite um número.")
        continue
    
    if opcao == 4:
        print("Fim do programa!")
        break
    
    if opcao == 1:

        p, q = gerador()
        print(f"Novos primos gerados: p={p}, q={q}")
        n = p * q
        totiente_n = (p - 1) * (q - 1)
        e = random.randint(2, totiente_n - 1)
        while not coprimos(e, totiente_n):
            e = random.randint(2, totiente_n - 1)
        d = encontrar_d(e, totiente_n)
        
        print(f"Chave Pública (n, e): ({n}, {e})")
        print(f"Chave Privada (n, d): ({n}, {d})")

    elif opcao == 2:
        texto = input("Digite a mensagem: ")
        texto_encriptado_lista = encriptar(texto, e, n)
        print(f"Texto encriptado: {texto_encriptado_lista}")

    elif opcao == 3:
        texto_encriptado_str = input("Digite o texto encriptado (deixe no seguinte formato: [num1, num2]): ")
        lista_encriptada = [int(i.strip()) for i in texto_encriptado_str.strip('[]').split(',')]
        texto_decriptado = decriptar(lista_encriptada, d, n)
        print(f"Texto decriptado: {texto_decriptado}")    
    else:
        print("Opção inválida. Escolha entre 1 e 4.")
