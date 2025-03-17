import random

def sorteio_alunos():
    alunos = [
        "jose", "vini", "alanda",
        "apollo", "malu", "maru"
    ]

    escolher = random.choice(alunos)
    print(f"o aluno escolhido foi: {escolher}")

sorteio_alunos()