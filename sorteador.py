import random


def sortear_numero(inicio: int = 0, fim: int = 1000) -> int:
    """Retorna um número inteiro aleatório entre inicio e fim (inclusive)."""
    return random.randint(inicio, fim)


if __name__ == "__main__":
    numero = sortear_numero()
    print(f"Número sorteado: {numero}")
