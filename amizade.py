class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.amigos = []
    
    def enviar_pedido_amizade(self, usuario):
        if usuario not in self.amigos:
            usuario.receber_pedido_amizade(self)
            print(f"Pedido de amizade enviado para {usuario.nome}.")
        else:
            print(f"{usuario.nome} já é seu amigo.")
    
    def receber_pedido_amizade(self, usuario):
        if usuario not in self.amigos:
            self.amigos.append(usuario)
            print(f"Pedido de amizade aceito de {usuario.nome}.")
        else:
            print(f"Você já é amigo de {usuario.nome}.")
    
    def listar_amigos(self):
        if self.amigos:
            print("Lista de Amigos:")
            for amigo in self.amigos:
                print(amigo.nome)
        else:
            print("Você não tem amigos ainda.")
            

# Exemplo de uso
usuario1 = Usuario("Ester")
usuario2 = Usuario("Beli")
usuario3 = Usuario("Jesus")
usuario4 = Usuario("Souza")

usuario1.enviar_pedido_amizade(usuario2)
usuario2.enviar_pedido_amizade(usuario1)
usuario1.enviar_pedido_amizade(usuario3)
usuario3.enviar_pedido_amizade(usuario1)
usuario1.enviar_pedido_amizade(usuario4)
usuario3.enviar_pedido_amizade(usuario2)
usuario3.enviar_pedido_amizade(usuario4)
usuario2.enviar_pedido_amizade(usuario3)
usuario2.enviar_pedido_amizade(usuario4)
usuario4.enviar_pedido_amizade(usuario1)
usuario4.enviar_pedido_amizade(usuario2)
usuario4.enviar_pedido_amizade(usuario3)

usuario1.listar_amigos()
usuario2.listar_amigos()
usuario3.listar_amigos()
