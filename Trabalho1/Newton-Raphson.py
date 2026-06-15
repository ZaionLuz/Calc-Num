# ==========================================
# MÉTODO DE NEWTON-RAPHSON
# ==========================================

# Função
def f(x):
    return x**3 - 2*x - 5

# Derivada
def df(x):
    return 3*x**2 - 2

def newton(x0, erro=0.001):
    """
    Método de Newton:
    Usa derivada para encontrar a raiz rapidamente.
    """

    iteracao = 0

    while True:
        # Fórmula de Newton
        x1 = x0 - f(x0) / df(x0)

        iteracao += 1
        print(f"Iteração {iteracao}: x = {x1}")

        # Critério de parada
        if abs(x1 - x0) < erro:
            return x1

        x0 = x1


# Teste
raiz = newton(2)
print("Raiz aproximada:", raiz)