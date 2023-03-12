from tkinter import *
import math
from collections import deque
root = Tk()
root.title("Calculadora")
display = Entry(root)
display.grid(row=1, columnspan=8, sticky=W+E)
i = 0
def get_number(n):
    global i
    display.insert(i, n)
    i += 1

def get_operacion(operator):
    global i
    operator_length = len(operator)
    display.insert(i, operator)
    i += operator_length

def clear_display():
    display.delete(0, END)

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()
        display.insert(0, 'error')

def resultado():
    ecuacion=display.get()
    a=enlistar(ecuacion)
    b=infix_to_postfix(a)
    c=evaluate_postfix(b)
    display.delete(0,END)
    display.insert(0,c)
    i=0

def prioridad(C):
    if C in ["+", "-"]:
        return 1
    elif C in ["*", "/"]:
        return 2
    elif C in funciones:
        return 4
    elif C in ["^"]:
        return 3
    elif C in ["(", ")"]:
        return 0

def infix_to_postfix(expr):
    p = expr
    p.append(")")
    p.insert(0, "(")
    stack = []
    posfix = []
    global operadores
    global funciones
    for i in range(len(p)):
        if p[i] == "(":
            stack.append(p[i])
        elif p[i] in operadores or p[i] in funciones:
            contador = len(stack) - 1
            if (prioridad(p[i])) > (prioridad(stack[contador] or prioridad(p[i]) ==0)):
                stack.append(p[i])
            else:
                posfix.append(stack.pop())
                stack.append(p[i])
        elif p[i] == ")":
            contador = len(stack) - 1
            while stack[contador] != "(":
                posfix.append(stack.pop())
                contador -= 1
            stack.pop()
        else:
            posfix.append(p[i])
    return posfix


def evaluate_postfix(posfix):
    vector = posfix
    vector.append(")")
    i = 0
    stack = []
    global funciones
    while vector[i] != ")":
        if vector[i] in operadores:
            B = float(stack.pop())
            A = float(stack.pop())
            if vector[i] == "*":
                C = A * B
            elif vector[i] == "/":
                C = A / B
            elif vector[i] == "+":
                C = A + B
            elif vector[i] == "-":
                C = A - B
            elif vector[i] == "^":
                C = A ** B
            stack.append(C)
        elif vector[i] in funciones:
            A = float(stack.pop())
            try:
                if vector[i] == "sin":
                    C = math.sin(math.radians(A))
                elif vector[i] == "cos":
                    C = math.cos(math.radians(A))
                elif vector[i] == "tan":
                    C = math.tan(math.radians(A))
                elif vector[i] == "asin":
                    C = math.degrees(math.asin(A))
                elif vector[i] == "acos":
                    C = math.degrees(math.acos(A))
                elif vector[i] == "atan":
                    C = math.degrees(math.atan(A))
                elif vector[i] == "log":
                    C = math.log10(A)
                elif vector[i] == "ln":
                    C = math.log(A, math.e)
                elif vector[i] == "alog":
                    C = 10 ** A
                elif vector[i] == "aln":
                    C = math.e ** A
                C = round(C, 4)
                stack.append(C)
            except:
                return "Math Error"
        else:
            stack.append(vector[i])
        i += 1
    resultado = stack.pop()
    return resultado

def enlistar(op):
    op = list(op)
    op.append('b')
    op2 = []
    stack = deque()
    for i in op:
        if i not in ['+', '-', '/', '*', '(', ')', 'b', '^']:
            stack.append(i)
        elif i in ['+', '-', '/', '*', '(', ')', 'b', '^']:
            contador = len(stack) - 1
            b = ''
            while contador >= 0 and stack[contador] not in ['+', '-', '/', '*']:
                b = b + stack.popleft()
                contador -= 1
            if b != '':
                op2.append(b)
            if i != 'b':
                op2.append(i)
    return op2

operadores = ["+", "-", "*", "/", "^"]
funciones = ["sin", "cos", "tan", "asin", "acos", "atan", "log", "ln", "alog", "aln"]
Button(root, text="1",width=5, height=4,command=lambda:get_number(1)).grid(row=2,column=0,sticky=W+E)
Button(root, text="2",width=5, height=4,command=lambda:get_number(2)).grid(row=2,column=1,sticky=W+E)
Button(root, text="3",width=5, height=4,command=lambda:get_number(3)).grid(row=2,column=2,sticky=W+E)

Button(root, text="4",width=5, height=4,command=lambda:get_number(4)).grid(row=3,column=0,sticky=W+E)
Button(root, text="5",width=5, height=4,command=lambda:get_number(5)).grid(row=3,column=1,sticky=W+E)
Button(root, text="6",width=5, height=4,command=lambda:get_number(6)).grid(row=3,column=2,sticky=W+E)

Button(root, text="7",width=5, height=4,command=lambda:get_number(7)).grid(row=4,column=0,sticky=W+E)
Button(root, text="8",width=5, height=4,command=lambda:get_number(8)).grid(row=4,column=1,sticky=W+E)
Button(root, text="9",width=5, height=4,command=lambda:get_number(9)).grid(row=4,column=2,sticky=W+E)

Button(root, text="AC",width=5, height=4,command=lambda:clear_display()).grid(row=5,column=0,sticky=W+E)
Button(root, text="0",width=5, height=4,command=lambda:get_number(0)).grid(row=5,column=1,sticky=W+E)

Button(root, text="+",width=5, height=4,command=lambda:get_operacion("+")).grid(row=2,column=3,sticky=W+E)
Button(root, text="-",width=5, height=4,command=lambda:get_operacion("-")).grid(row=3,column=3,sticky=W+E)
Button(root, text="",width=5, height=4,command=lambda:get_operacion("")).grid(row=4,column=3,sticky=W+E)
Button(root, text="/",width=5, height=4,command=lambda:get_operacion("/")).grid(row=5,column=2,sticky=W+E)

Button(root, text="←",width=5, height=4,command=lambda:undo()).grid(row=2,column=4,sticky=W+E,columnspan=2)
Button(root, text="exp",width=5, height=4,command=lambda:get_operacion("^")).grid(row=3,column=4,sticky=W+E)
Button(root, text="(",width=5, height=4,command=lambda:get_operacion("(")).grid(row=4,column=4,sticky=W+E)
Button(root, text=")",width=5, height=4,command=lambda:get_operacion(")")).grid(row=4,column=5,sticky=W+E)
Button(root, text="=",width=5, height=4,command=lambda:resultado()).grid(row=5,column=3,sticky=W+E,columnspan=2)

Button(root, text="sen",width=5, height=4,command=lambda:get_operacion("sin(")).grid(row=5,column=5,sticky=W+E)
Button(root, text="cos",width=5, height=4,command=lambda:get_operacion("cos(")).grid(row=2,column=6,sticky=W+E)
Button(root, text="tan",width=5, height=4,command=lambda:get_operacion("tan(")).grid(row=5,column=7,sticky=W+E)
Button(root, text="log",width=5, height=4,command=lambda:get_operacion("log(")).grid(row=3,column=5,sticky=W+E)

Button(root, text="asen",width=5, height=4,command=lambda:get_operacion("asin(")).grid(row=3,column=6,sticky=W+E)
Button(root, text="acos",width=5, height=4,command=lambda:get_operacion("acos(")).grid(row=4,column=6,sticky=W+E)
Button(root, text="atan",width=5, height=4,command=lambda:get_operacion("atan(")).grid(row=5,column=6,sticky=W+E)

root.mainloop()