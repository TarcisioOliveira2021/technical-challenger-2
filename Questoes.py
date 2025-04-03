# Questão 1
indice = 13
soma = 0
k = 0

while (k < indice):
    k = k + 1
    soma = soma + k
    print(soma)

# Questão 2
def pertence_ao_fibonacci(n:int) -> bool:
    numeros = [0, 1]
    for i in range(2, n):
        numeros.append(numeros[i-1] + numeros[i-2])
    if n in numeros:
        return True
    else:
        return False

print(str(pertence_ao_fibonacci(35)))
print(str(pertence_ao_fibonacci(13)))
print(str(pertence_ao_fibonacci(1)))


# Questão 3
valores_faturados = [
	{
		"dia": 1,
		"valor": 22174.1664
	},
	{
		"dia": 2,
		"valor": 24537.6698
	},
	{
		"dia": 3,
		"valor": 26139.6134
	},
	{
		"dia": 4,
		"valor": 0.0
	},
	{
		"dia": 5,
		"valor": 0.0
	},
	{
		"dia": 6,
		"valor": 26742.6612
	},
	{
		"dia": 7,
		"valor": 0.0
	},
	{
		"dia": 8,
		"valor": 42889.2258
	},
	{
		"dia": 9,
		"valor": 46251.174
	},
	{
		"dia": 10,
		"valor": 11191.4722
	},
	{
		"dia": 11,
		"valor": 0.0
	},
	{
		"dia": 12,
		"valor": 0.0
	},
	{
		"dia": 13,
		"valor": 3847.4823
	},
	{
		"dia": 14,
		"valor": 373.7838
	},
	{
		"dia": 15,
		"valor": 2659.7563
	},
	{
		"dia": 16,
		"valor": 48924.2448
	},
	{
		"dia": 17,
		"valor": 18419.2614
	},
	{
		"dia": 18,
		"valor": 0.0
	},
	{
		"dia": 19,
		"valor": 0.0
	},
	{
		"dia": 20,
		"valor": 35240.1826
	},
	{
		"dia": 21,
		"valor": 43829.1667
	},
	{
		"dia": 22,
		"valor": 18235.6852
	},
	{
		"dia": 23,
		"valor": 4355.0662
	},
	{
		"dia": 24,
		"valor": 13327.1025
	},
	{
		"dia": 25,
		"valor": 0.0
	},
	{
		"dia": 26,
		"valor": 0.0
	},
	{
		"dia": 27,
		"valor": 25681.8318
	},
	{
		"dia": 28,
		"valor": 1718.1221
	},
	{
		"dia": 29,
		"valor": 13220.495
	},
	{
		"dia": 30,
		"valor": 8414.61
	}
]

def encontrar_menor_faturamento(valores:list) -> str:
    valor = 0
    for i in valores:
        if int(i["valor"]) < valor:
            valor = int(i["valor"])
    
    print(f"O menor valor de faturamento foi: R$ {valor:.2f}")
def encontrar_maior_faturamento(valores:list) -> str:
    valor = 0
    for i in valores:
        if int(i["valor"]) > valor:
            valor = int(i["valor"])
    
    print(f"O maior valor de faturamento foi: R$ {valor:.2f}")
def calcular_media_mensal(valores:list) -> int:
    valor_media_mensal = 0
    qtd_dias_faturados = int(valores[-1]["dia"])

    for i in valores:
        if int(i["valor"]) > 0:
            valor_media_mensal += int(i["valor"])


    return valor_media_mensal / qtd_dias_faturados
def encontrar_dias_com_faturamento_acima_da_media_mensal(valores:list) -> None:
    valor_media_mensal = calcular_media_mensal(valores)
    dias_acima_media = []
    for i in valores:
        if int(i["valor"]) > valor_media_mensal:
            dias_acima_media.append(i["dia"])
    
    print(f"O valor médio mensal foi: R$ {valor_media_mensal:.2f}")
    print("Os dias com faturamento acima da média mensal foram: " + str(dias_acima_media))

encontrar_menor_faturamento(valores_faturados)
encontrar_maior_faturamento(valores_faturados)
encontrar_dias_com_faturamento_acima_da_media_mensal(valores_faturados)


# Questão 4
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}
total = sum(faturamento.values())
def exibir_percentual_representacao(faturamento:dict, total:float) -> None:
    for estado, valor in faturamento.items():
        percentual = (valor / total) * 100
        print(f"{estado}: {percentual:.2f}%")

exibir_percentual_representacao(faturamento, total)

# Questão 5
texto = "Dois patos na lagoa"
texto_invertido = ""

for caractere in texto:
    texto_invertido = caractere + texto_invertido

print("String original:", texto)
print("String invertida:", texto_invertido)


