def infix_to_postfix(Q):
    # Paso 1: Agregar paréntesis al inicio y final de la expresión Q
    Q = ['('] + Q + [')']
    # Paso 2: Inicializar P y STACK
    P = []
    stack = []
    # Paso 3-6: Recorrer Q de izquierda a derecha
    for token in Q:
        if token.isnumeric() or token.isalpha():
            # Paso 3: Si es un operando, agregarlo a P
            P.append(token)
        elif token == '(':
            # Paso 4: Si es un paréntesis de apertura, agregarlo a STACK
            stack.append(token)
        elif token in ['+', '-', '*', '/', '^']:
            # Paso 5: Si es un operador, verificar precedencia
            while stack[-1] in ['+', '-', '*', '/', '^'] and \
                  (precedencia(token) <= precedencia(stack[-1])):
                P.append(stack.pop())
            # Agregar el operador a STACK
            stack.append(token)
        elif token == ')':
            # Paso 6: Si es un paréntesis de cierre, desapilar hasta el paréntesis de apertura
            while stack[-1] != '(':
                P.append(stack.pop())
            # Eliminar el paréntesis de apertura de STACK
            stack.pop()
    # Paso 7: Imprimir la expresión postfix
    print(' '.join(P))

# Función para determinar la precedencia de un operador
def precedencia(op):
    if op in ['+', '-']:
        return 1
    elif op in ['*', '/']:
        return 2
    elif op == '^':
        return 3
    else:
        return 0
