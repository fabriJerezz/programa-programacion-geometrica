from gpkit import Model, Variable


def main():
    # Problema en forma estandar:
    h = Variable("h", "m", "Altura")
    w = Variable("w", "m", "Ancho")
    d = Variable("d", "m", "Profundo")

    # TODO: Aca nos tenemos que decidir cuales van a ser los limites inferiores
    # y superiores del ratio de aspecto
    alpha = Variable(
        "\\alpha", 0.7, "-", "Límite inferior de la razón de aspecto de la pared"
    )

    beta = Variable(
        "\\beta", 1.0, "-", "Límite superior de la razón de aspecto de la pared"
    )

    gamma = Variable(
        "\\gamma", 1.0, "-", "Límite inferior de la razón de aspecto del piso"
    )
    delta = Variable(
        "\\delta", 3.0, "-", "Límite superior de la razón de aspecto del piso"
    )

    A_pared = Variable("A_pared", 20, "m^2", "Limite superior del area de la pared")

    A_piso = Variable("A_piso", 16, "m^2", "Limite superior del area del piso")

    z = (1 / h) * (1 / w) * (1 / d)
    restricciones = [
        (2 / A_pared) * h * w + (2 / A_pared) * h * d <= 1,
        (1 / A_piso) * w * d <= 1,
        alpha / h * w <= 1,
        (1 / beta) * h * w**-1 <= 1,
        gamma * w * d**-1 <= 1,
        (1 / delta) * w**-1 * d <= 1,
    ]

    modelo = Model(z, restricciones)
    solucion = modelo.solve(verbosity=2)
    print(solucion.table())


if __name__ == "__main__":
    main()
