# Programa para cadastro e avaliação de alunos

# Função principal
def cadastro_e_avaliacao():
    # Solicita o nome do aluno
    nome = input("Digite o nome do aluno: ")

    # Solicita o ano de nascimento do aluno e calcula a idade
    ano_nascimento = int(input("Digite o ano de nascimento do aluno: "))
    idade = 2024 - ano_nascimento  # Calcula a idade com base no ano atual

    # Solicita as notas e pesos das provas
    nota1 = float(input("Digite a nota 1 (0 a 10): "))
    nota2 = float(input("Digite a nota 2 (0 a 10): "))
    nota3 = float(input("Digite a nota 3 (0 a 10): "))

    # Pesos das provas
    peso1 = 1
    peso2 = 2
    peso3 = 3

    # Calcula a média ponderada
    media_final = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

    # Determina o status do aluno baseado na média final
    if media_final >= 7.0:
        status = "Aprovado"
    elif 5.0 <= media_final <= 6.9:
        status = "Recuperação"
    else:
        status = "Reprovado"

    # Exibe as informações do aluno
    print("\n--- Resultado ---")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média Final: {media_final:.2f}")
    print(f"Status: {status}")

# Executa o programa
cadastro_e_avaliacao()
