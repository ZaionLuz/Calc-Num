# ==========================================
# MÉTODO DA FALSA POSIÇÃO
# ==========================================

# Função
def f(x):
    return x**3 - 4*x - 9

def falsa_posicao(a, b, erro=0.00001):
    """
    Método da Falsa Posição:
    Usa uma reta entre dois pontos do intervalo.
    """

    iteracao = 0

    # Verifica se há raiz no intervalo
    if f(a) * f(b) >= 0:
        print("Não há raiz no intervalo.")
        return None

    while True:
        # Fórmula
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))

        iteracao += 1
        print(f"Iteração {iteracao}: x = {x}")

        # Critério de parada
        if abs(f(x)) < erro:
            return x

        # Atualiza intervalo
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x


# Teste
raiz = falsa_posicao(2, 3)
print("Raiz aproximada:", raiz)