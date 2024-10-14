# Classe base chamada Produto
class Produto:
    def __init__(self, nome, preco, quantidade):
        # Atributos básicos do produto
        self.nome = nome  # Nome do produto
        self.preco = preco  # Preço do produto
        self.quantidade = quantidade  # Quantidade em estoque
    
    def calcular_preco_total(self):
        # Método para calcular o preço total com base na quantidade
        return self.preco * self.quantidade
    
    def aplicar_desconto(self, desconto):
        # Método para aplicar um desconto no preço do produto
        self.preco -= (self.preco * desconto / 100)

# Subclasse ProdutoComDesconto que herda da classe Produto
class ProdutoComDesconto(Produto):
    def __init__(self, nome, preco, quantidade, desconto):
        # Chama o construtor da classe base
        super().__init__(nome, preco, quantidade)
        self.desconto = desconto  # Atributo para o desconto específico
    
    def aplicar_desconto_especifico(self):
        # Aplica o desconto específico deste tipo de produto
        self.aplicar_desconto(self.desconto)
    
    def exibir_informacoes(self):
        # Exibe o preço original e o preço com desconto
        preco_original = self.preco / (1 - self.desconto / 100)
        print(f"Produto: {self.nome}")
        print(f"Preço original: R${preco_original:.2f}")
        print(f"Preço com desconto: R${self.preco:.2f}\n")

# Subclasse ProdutoImportado que herda da classe Produto
class ProdutoImportado(Produto):
    def __init__(self, nome, preco, quantidade, imposto_importacao):
        # Chama o construtor da classe base
        super().__init__(nome, preco, quantidade)
        self.imposto_importacao = imposto_importacao  # Atributo para o imposto
    
    def calcular_preco_com_imposto(self):
        # Calcula o preço considerando o imposto de importação
        return self.preco + (self.preco * self.imposto_importacao / 100)
    
    def exibir_informacoes(self):
        # Exibe o preço original, o imposto e o preço final
        preco_final = self.calcular_preco_com_imposto()
        print(f"Produto: {self.nome}")
        print(f"Preço original: R${self.preco:.2f}")
        print(f"Imposto de importação: {self.imposto_importacao}%")
        print(f"Preço final com imposto: R${preco_final:.2f}\n")

# Criando uma lista de produtos para testar as classes
produtos = [
    ProdutoComDesconto("Camiseta", 50.0, 10, 20),
    ProdutoImportado("Relógio", 200.0, 5, 15)
]

# Usando list comprehension para filtrar produtos acima de um certo preço
produtos_acima_de_100 = [p for p in produtos if p.preco > 100]

# Exibindo informações dos produtos
for produto in produtos:
    produto.exibir_informacoes()

# Exibindo produtos com preço acima de 100
print("Produtos acima de R$100,00:")
for produto in produtos_acima_de_100:
    print(f"{produto.nome} - R${produto.preco:.2f}")
