# Questão 1
indice = 13
soma = 0
k = 0

while (k < indice):
    k = k + 1
    soma = soma + k
    print(soma)

# Questão 2
def pertence_ao_fibonacci(n):
    numeros = [0, 1]
    for i in range(2, n):
        numeros.append(numeros[i-1] + numeros[i-2])
        if numeros[i] == n:
            return True
        
    return False

print(str(pertence_ao_fibonacci(35)))
print(str(pertence_ao_fibonacci(13)))
print(str(pertence_ao_fibonacci(1)))


    
