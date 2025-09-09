# -*- coding: utf-8 -*-

# Exercicio 5
class Animal:
    def falar(self):
        print("O animal faz um som.")

class Cachorro(Animal):
    def falar(self):
        print("Au Au 🐶")

a = Animal()
a.falar()

c = Cachorro()
c.falar()

