class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def convidar_encontro(self, pessoa):
        resposta = input(f"Olá {pessoa.nome}! {self.nome} gostaria de te convidar para um encontro. Você aceita? (s/n): ")
        if resposta.lower() == "s":
            print("Ótimo! O encontro está marcado.")
        else:
            print("Tudo bem, quem sabe em outra oportunidade.")
            

# Exemplo de uso
pessoa1 = Pessoa("Ester")
pessoa2 = Pessoa("Pessoinha")

pessoa1.convidar_encontro(pessoa2)
