from gpkit import Variable, Model

def main():
    # Problema en forma estandar:

    h = Variable("h", "m", "Altura")
    w = Variable("w", "m", "Ancho")
    d = Variable("d", "m", "Profundo")

    # TODO: Aca nos tenemos que decidir cuales van a ser los limites inferiores
    # y superiores del ratio de aspecto
    alpha = Variable("\\alpha", 0.5, "-")
    beta = Variable("\\beta", 2.0, "-")
    gamma = Variable("\\delta", 0.5, "-")
    delta = Variable("\\gamma", 2.0, "-")

    A_pared = Variable("A_pared", 10, "m^2", "Limite superior del area de la pared")
    A_piso = Variable("A_piso", 5, "m^2", "Limite superior del area del piso")

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
