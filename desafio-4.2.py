# Classe para representar um Livro
class Livro:
    def __init__(self, id_livro, titulo, autor, categoria):
        # Atributos do livro
        self.id_livro = id_livro  # Identificação única do livro
        self.titulo = titulo  # Título do livro
        self.autor = autor  # Autor do livro
        self.categoria = categoria  # Categoria do livro

# Classe para representar um Autor
class Autor:
    def __init__(self, id_autor, nome):
        # Atributos do autor
        self.id_autor = id_autor  # Identificação única do autor
        self.nome = nome  # Nome do autor

# Classe para representar um Usuário
class Usuario:
    def __init__(self, id_usuario, nome):
        # Atributos do usuário
        self.id_usuario = id_usuario  # Identificação única do usuário
        self.nome = nome  # Nome do usuário

# Classe para representar um Empréstimo de livro
class Emprestimo:
    def __init__(self, id_emprestimo, livro, usuario, data_emprestimo, data_devolucao=None):
        # Atributos do empréstimo
        self.id_emprestimo = id_emprestimo  # Identificação única do empréstimo
        self.livro = livro  # Referência ao livro emprestado
        self.usuario = usuario  # Referência ao usuário que pegou o livro
        self.data_emprestimo = data_emprestimo  # Data do empréstimo
        self.data_devolucao = data_devolucao  # Data da devolução (pode ser None se ainda não devolvido)

# Criando alguns autores
autor1 = Autor(1, "Machado de Assis")
autor2 = Autor(2, "J.K. Rowling")

# Criando alguns livros
livro1 = Livro(1, "Dom Casmurro", autor1, "Romance")
livro2 = Livro(2, "Harry Potter e a Pedra Filosofal", autor2, "Fantasia")

# Criando alguns usuários
usuario1 = Usuario(1, "Maria")
usuario2 = Usuario(2, "João")

# Criando um empréstimo
emprestimo1 = Emprestimo(1, livro1, usuario1, "2023-10-10")

# Exibindo detalhes de um empréstimo
print(f"Empréstimo ID: {emprestimo1.id_emprestimo}")
print(f"Livro emprestado: {emprestimo1.livro.titulo}")
print(f"Usuário: {emprestimo1.usuario.nome}")
print(f"Data do empréstimo: {emprestimo1.data_emprestimo}")
