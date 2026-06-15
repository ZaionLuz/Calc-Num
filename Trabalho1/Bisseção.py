# ==========================================
# MÉTODO DA BISSEÇÃO
# ==========================================

# Função
def f(x):
    return x**3 - 9*x + 3

def bissecao(a, b, erro=0.0001):
    """
    Método da Bisseção:
    Divide o intervalo ao meio até encontrar a raiz.
    """

    iteracao = 0

    # Verifica se existe raiz
    if f(a) * f(b) >= 0:
        print("Não há raiz no intervalo.")
        return None

    while (b - a) / 2 > erro:
        c = (a + b) / 2  # ponto médio

        iteracao += 1
        print(f"Iteração {iteracao}: c = {c}")

        # Se encontrou a raiz exata
        if f(c) == 0:
            return c

        # Atualiza intervalo
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


# Teste
raiz = bissecao(-5, -3)
print("Raiz aproximada:", raiz)