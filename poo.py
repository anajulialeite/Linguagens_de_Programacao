# criação
class Personagem:
    def __init__(self, nome, vida):
        self.__nome = nome
        self.__vida = vida
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    def atacar(self, personagem):
        personagem.vida -= 10
        print(f'{self.nome} atacou {personagem.nome} e {personagem.nome} perdeu 10 pontos de vida e agora esta com {personagem.vida}')

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def atacar(self, personagem):
        personagem.vida -= 20
        print(f'{self.nome} atacou {personagem.nome} e {personagem.nome} perdeu 20 pontos de vida e agora esta com {personagem.vida}')

    def cura(self, personagem):
        personagem.vida += 30
        print(f'{self.nome} curou {personagem.nome} e {personagem.nome} ganhou 30 pontos de vida e agora esta com {personagem.vida}')

# criando os objetos
personagem1 = Personagem('Guerreiro', 100)
print(f'Personagem {personagem1.nome} | Vida: {personagem1.vida}')
mago = Mago('Gandof', 100)
print(f'Personagem {mago.nome} | Vida: {mago.vida}')

personagem1.atacar(mago)
mago.cura(mago)
print(f'Personagem {personagem1.nome} | Vida: {personagem1.vida}')
print(f'Personagem {mago.nome} | Vida: {mago.vida}')
