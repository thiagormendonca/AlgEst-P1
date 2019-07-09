def preced(op1, op2):
    operadores = ["^", "*/", "+-"]
    op1i = 0
    op2i = 0
    for item in operadores:
        if op1 in item:
            op1i = operadores.index(item)
        if op2 in item:
            op2i = operadores.index(item)
    if op1i < op2i:
        return True
    else:
        return False


def in_to_pos(exp):
    operadores = ""
    pos = ""
    while exp != "":
        if exp[0] not in "+-*/^":
            if exp[0] == "(":
                exp = exp[1:]
                continue
            elif exp[0] == ")":
                pos = pos + operadores
                operadores = ""
            else:
                pos = pos + exp[0]
        else:
            while operadores != "" and preced(operadores[0], exp[0]):
                pos = pos + operadores[0]
                operadores = operadores[1:]
            operadores = exp[0] + operadores
        exp = exp[1:]
    while operadores != "":
        pos = pos + operadores[0]
        operadores = operadores[1:]
    return pos

print(in_to_pos("(A*B+2*C^3)/2*A"))