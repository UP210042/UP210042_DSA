infix='5*(6+2)-12/4'                                #prioridad (1): +-, (2): */, (3): ^ (4): ()
posfix='5 6 2 + * 12 4/-'
value=[]                                               # Q=(-5-*-(-6-+-2-)---12-/--4---)
                                                        #  0-1-2-3-4-5-6-7-8-9-10-11-12                                                     
p=posfix.split()
# posfix= 1x1x1x1x/+/+/+/+/
p= ['5','6','2','+','*','12','4','/','-']
def determinar_op_ope (p):
    if p[0] in ['+','-','*','/','^','()']:
        print("operador")             
    else:
        print("operando") 
def op_o_ope (p):
    if p[0] in ['+','-']:
        return 4
    elif p[0] in ['*','/']:
        return 3
    elif p[0] in ['^']:
        return 2     
    elif p[0] in ['()']:
        return 1

# if p==0:
#     return 0              

infix="A+(B*C-(D/E^F)*G)*H"
infix=infix.split()
# op='+','-','*','/','^'
# while op>=op:
infix.pop()
#stack=pila
print(infix)
print(infix[-1])
infix.insert(0,"(")
print(infix)
# value=input(infix)    ->Imprime el resultado en base al infix
# print(value)