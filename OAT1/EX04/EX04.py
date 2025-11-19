# -*- coding: utf-8 -*-

# Exercicio 4
class Aluno:
    def __init__(self, nome, nota):
        self.__nome = nome
        self.nota = nota  # usa o setter

    @property
    def nome(self):
        return self.__nome

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, valor):
        if 0 <= valor <= 10:
            self.__nota = valor
        else:
            raise ValueError("Nota deve estar entre 0 e 10")

aluno1 = Aluno("Ana", 9)
print(aluno1.nome, aluno1.nota)

# Teste inválido:
# aluno1.nota = 11  # Vai gerar erro

