# Programa que usa estruturas de repetição, operadores aritméticos e arrays

# Função principal
def sistema():
    # Lista para armazenar os números inseridos
    numeros = []

    # Estrutura de repetição: solicita números até o usuário digitar -1
    while True:
        numero = int(input("Digite um número (ou -1 para sair): "))
        if numero == -1:
            break  # Sai do loop se o usuário digitar -1
        numeros.append(numero)  # Adiciona o número à lista

    # Realizando operações aritméticas com os números armazenados
    soma = sum(numeros)  # Soma de todos os números
    subtracao = numeros[0] - sum(numeros[1:]) if len(numeros) > 1 else numeros[0]  # Subtração
    multiplicacao = 1
    for num in numeros:
        multiplicacao *= num  # Multiplicação de todos os números

    divisao = numeros[0] / numeros[1] if len(numeros) > 1 else "Indefinido"  # Divisão (se houver 2 números ou mais)
    divisao_inteira = numeros[0] // numeros[1] if len(numeros) > 1 else "Indefinido"  # Divisão inteira
    resto_divisao = numeros[0] % numeros[1] if len(numeros) > 1 else "Indefinido"  # Resto da divisão
    exponenciacao = numeros[0] ** 2  # Exponenciação (quadrado do primeiro número)

    # Exibindo os resultados
    print("\n--- Resultados ---")
    print(f"Números armazenados: {numeros}")
    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao}")
    print(f"Divisão Inteira: {divisao_inteira}")
    print(f"Resto da Divisão: {resto_divisao}")
    print(f"Exponenciação (primeiro número ao quadrado): {exponenciacao}")

# Executa o programa
sistema()
