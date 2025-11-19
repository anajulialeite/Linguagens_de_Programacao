# -*- coding: utf-8 -*-

# Exercicio 2
import hashlib

# senha previamente armazenada (hash da palavra "python123")
senha_correta_hash = hashlib.sha256("python123".encode()).hexdigest()

senha_digitada = input("Digite sua senha: ")
senha_hash = hashlib.sha256(senha_digitada.encode()).hexdigest()

if senha_hash == senha_correta_hash:
    print("Acesso permitido ✅")
else:
    print("Acesso negado ❌")
