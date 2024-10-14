# Classe Produto
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    # Método para atualizar o estoque
    def atualizar_estoque(self, quantidade_vendida):
        self.quantidade -= quantidade_vendida

    # Método para calcular o valor total das vendas de um produto
    def calcular_valor_vendas(self, quantidade_vendida):
        return quantidade_vendida * self.preco

# Função para salvar informações dos produtos em um arquivo
def salvar_produto(produto):
    with open("produtos.txt", "a") as arquivo:
        arquivo.write(f"{produto.nome},{produto.preco},{produto.quantidade}\n")

# Função para carregar os produtos do arquivo
def carregar_produtos():
    produtos = []
    try:
        with open("produtos.txt", "r") as arquivo:
            for linha in arquivo:
                nome, preco, quantidade = linha.strip().split(",")
                produtos.append(Produto(nome, float(preco), int(quantidade)))
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado.")
    return produtos

# Função para registrar uma venda e atualizar o arquivo
def registrar_venda(nome_produto, quantidade_vendida):
    produtos = carregar_produtos()
    for produto in produtos:
        if produto.nome == nome_produto:
            produto.atualizar_estoque(quantidade_vendida)
            valor_venda = produto.calcular_valor_vendas(quantidade_vendida)
            salvar_venda(nome_produto, quantidade_vendida, valor_venda)
            salvar_produtos(produtos)
            return valor_venda
    print("Produto não encontrado.")
    return 0

# Função para salvar a venda em um arquivo
def salvar_venda(nome_produto, quantidade_vendida, valor_venda):
    with open("vendas.txt", "a") as arquivo:
        arquivo.write(f"{nome_produto},{quantidade_vendida},{valor_venda}\n")

# Função para salvar o estado atualizado dos produtos
def salvar_produtos(produtos):
    with open("produtos.txt", "w") as arquivo:
        for produto in produtos:
            arquivo.write(f"{produto.nome},{produto.preco},{produto.quantidade}\n")

# Função para calcular e exibir o total de vendas e gerar relatórios
def gerar_relatorio():
    total_vendas = 0
    produto_mais_vendido = None
    produto_maior_receita = None
    vendas_por_produto = {}
    receita_por_produto = {}

    try:
        with open("vendas.txt", "r") as arquivo:
            for linha in arquivo:
                nome_produto, quantidade_vendida, valor_venda = linha.strip().split(",")
                quantidade_vendida = int(quantidade_vendida)
                valor_venda = float(valor_venda)
                total_vendas += valor_venda

                # Atualiza vendas e receita por produto
                if nome_produto in vendas_por_produto:
                    vendas_por_produto[nome_produto] += quantidade_vendida
                    receita_por_produto[nome_produto] += valor_venda
                else:
                    vendas_por_produto[nome_produto] = quantidade_vendida
                    receita_por_produto[nome_produto] = valor_venda

        # Identifica o produto mais vendido e com maior receita
        if vendas_por_produto:
            produto_mais_vendido = max(vendas_por_produto, key=vendas_por_produto.get)
            produto_maior_receita = max(receita_por_produto, key=receita_por_produto.get)

        # Exibe o relatório
        print(f"Total de vendas: R$ {total_vendas:.2f}")
        print(f"Produto mais vendido: {produto_mais_vendido}")
        print(f"Produto com maior receita: {produto_maior_receita}")
    except FileNotFoundError:
        print("Arquivo de vendas não encontrado.")

# Exemplo simples de como usar o sistema
if __name__ == "__main__":
    # Exemplo de cadastro de produtos
    p1 = Produto("Camisa", 50.0, 100)
    p2 = Produto("Calça", 80.0, 50)
    
    # Salvando os produtos
    salvar_produto(p1)
    salvar_produto(p2)

    # Registrando uma venda
    valor_venda = registrar_venda("Camisa", 10)
    print(f"Venda registrada: R$ {valor_venda:.2f}")

    # Gerando o relatório de vendas
    gerar_relatorio()
