from gpkit import Variable, Model
from gpkit.nomials import Monomial, Posynomial, PosynomialInequality

h = Variable("h", "m")
w = Variable("w", "m")
d = Variable("d", "m")
a_pared = 2 * (h * w + h * d) # type: ignore
assert isinstance(a_pared, Posynomial)
a_piso = w * d
assert isinstance(a_piso, Monomial)

alpha = 2
beta = 2
gamma = 3
delta = 3
assert isinstance(delta, Monomial)
# alpha = Variable("alpha")
# beta = Variable("beta")
# gamma = Variable("gamma")

objective = h**-1 * w**-1 * d**-1

constraints = [
        (2 / a_pared) * h * w + (2 / a_pared) * h * d <= 1, # type: ignore
        (1 / a_piso) * w * d <= 1, # type: ignore
        alpha * h**-1 * w <= 1,
        (1 / beta) * h * w**-1 <= 1,
        gamma * w * d**-1 <= 1,
        (1 / delta) * w**-1*d <=1
    ]
    
m = Model(objective, constraints)

sol = m.solve(verbosity=0)

print(sol.table())