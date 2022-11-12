def f1(t, b):
    return b * np.exp(-beta * t)

def f2(t, b, beta):
    return b * np.exp(-beta * t)

def f3(t, a, alpha):
    return (a * np.exp(-alpha * t)) + (b * np.exp(-beta * t))