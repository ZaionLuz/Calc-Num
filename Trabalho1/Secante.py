# ==========================================
# MÉTODO DA SECANTE
# ==========================================

# Função f(x)
def f(x):
    return x**4 - x - 10

def secante(x0, x1, erro=0.001):
    """
    Método da Secante:
    Usa dois pontos iniciais para aproximar a raiz.
    Não precisa de derivada.
    """

    iteracao = 0

    # Enquanto o erro for maior que o desejado
    while abs(x1 - x0) > erro:
        # Fórmula da secante
        x = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))

        # Atualiza os valores
        x0 = x1
        x1 = x

        iteracao += 1
        print(f"Iteração {iteracao}: x = {x1}")

    return x1


# Teste
raiz = secante(1, 2)
print("Raiz aproximada:", raiz)