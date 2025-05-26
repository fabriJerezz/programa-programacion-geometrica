from gpkit import Variable, Model


def main():
    # Problema en forma estandar:

    h = Variable("altura", "m")  # Altura
    w = Variable("ancho", "m")  # Ancho
    d = Variable("profundo", "m")  # Profundo

    z = h**-1 * w**-1 * d**-1

    # TODO: Aca nos tenemos que decidir cuales van a ser los limites inferiores
    # y superiores del ratio de aspecto
    alpha = Variable("alpha", 1.0)
    beta = Variable("beta", 1.0)
    gamma = Variable("gamma", 1.0)
    delta = Variable("delta", 1.0)

    A_pared = Variable("A_pared", 10, "m^2")
    A_piso = Variable("A_piso", 5, "m^2")

    restricciones = [
        2 * A_pared**-1 * h * w + 2 * A_pared**-1 * h * d <= 1,
        A_piso**-1 * w * d <= 1,
        alpha * h**-1 * w <= 1,
        beta**-1 * h * w**-1 <= 1,
        gamma * w * d**-1 <= 1,
        delta**-1 * w**-1 * d <= 1,
    ]

    modelo = Model(z, restricciones)
    solucion = modelo.solve(verbosity=2)
    print(solucion.table())


if __name__ == "__main__":
    main()
