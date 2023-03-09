# Recebe um número do usuário
num = int(input("Digite um número: "))

fib1 = 0
fib2 = 1

# Verifica se o número informado é 0 ou 1 
if num == 0:
    print("O número 0 pertence à sequência de Fibonacci.")
elif num == 1:
    print("O número 1 pertence à sequência de Fibonacci.")
else:
    while fib2 <= num:
        fib3 = fib1 + fib2
        if fib3 == num:
            print(f"O número {num} pertence à sequência de Fibonacci.")
            break
        fib1 = fib2
        fib2 = fib3
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")
