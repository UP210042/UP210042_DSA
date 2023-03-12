import tkinter as tk
import math

def infix_to_postfix(expr):
    op_prioridad = {'+':1, '-':1, '*':2, '/':2, '^':3, 'sin':4, 'cos':4, 'tan':4, 'log':4, 'asin':4, 'acos':4, 'atan':4, '(':0}
    stack = []
    posfix = []
    for token in expr:
        if token in ['+', '-', '*', '/', '^', 'sin', 'cos', 'tan', 'log', 'asin', 'acos', 'atan']:
            while stack and op_prioridad[token] <= op_prioridad[stack[-1]]:
                posfix.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                posfix.append(stack.pop())
            stack.pop()
        else:
            posfix.append(float(token))
    while stack:
        posfix.append(stack.pop())
    return posfix

def evaluate_postfix(posfix):
    stack = []
    for token in posfix:
        if token == '+':
            stack.append(stack.pop()+stack.pop())
        elif token == '-':
            b=stack.pop()
            a=stack.pop()
            stack.append(a-b)
        elif token == '*':
            stack.append(stack.pop()*stack.pop())
        elif token == '/':
            b=stack.pop()
            a=stack.pop()
            stack.append(a/b)
        elif token == '^':
            b=stack.pop()
            a=stack.pop()
            stack.append(a**b)
        elif token == 'sin':
            stack.append(math.sin(stack.pop()))
        elif token == 'cos':
            stack.append(math.cos(stack.pop()))
        elif token == 'tan':
            stack.append(math.tan(stack.pop()))
        elif token == 'log':
            stack.append(math.log(stack.pop(),10))
        elif token == 'asin':
            stack.append(math.asin(stack.pop()))
        elif token == 'acos':
            stack.append(math.acos(stack.pop()))
        elif token == 'atan':
            stack.append(math.atan(stack.pop()))
        else:
            stack.append(token)
    return stack[0]

def evaluate_expression(expression):
    tokens = expression.split()
    posfix = infix_to_postfix(tokens)
    resultado = evaluate_postfix(posfix)
    return resultado

def btn_click(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(num))

def btn_clear():
    entry.delete(0, tk.END)

def btn_equals():
    expression = entry.get()
    resultado = evaluate_expression(expression)
    entry.delete(0, tk.END)
    entry.insert(0, resultado)

root = tk.Tk()
root.title("Calculadora")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: btn_click(1))

root.mainloop()