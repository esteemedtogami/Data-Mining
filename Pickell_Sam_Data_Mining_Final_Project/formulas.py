import math


def sig(x):
    #  Implementation the log function as shown in the provided Wikipedia page
    return 1/(1+math.exp(-x))


def inv_sig(x):
    #  Derivative of the log function as shown in the provided Wikipedia page
    log_fun = 1/(1+math.exp(-x))
    return log_fun * (1 - log_fun)


def err(o, t):
    #  squared error function, o is the actual output value and t is the target output, as shown in the
    #  provided Wikipedia page
    return math.pow((t - o), 2)


def inv_err(o, t):
    #  derivative of squared error function with respect to o, as shown in the provided Wikipedia page
    return o - t


