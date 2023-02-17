posfix= [5, 6, 2, '+', '*', 12, 4, '/', '-']   #---->P
stack=[]
posfix.append(')')
c=0
print(posfix)
while posfix[c] != ")":
    if type(posfix[c])== int:
        stack.append(posfix[c])
    elif type(posfix[c])==str:
        b=stack.pop()
        a=stack.pop()
        if posfix[c] == '+':
            z=a+b
        elif posfix[c] =='-':
            z=a-b
        elif posfix[c] == '*':
            z=a*b
        elif posfix[c] == '/':        
            z=a/b
        elif posfix[c] == '^':
            z=a^b    
        stack.append(z)
    c+=1
print(stack)          