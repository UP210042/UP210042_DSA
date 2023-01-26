import random
intentos=0
numero=random.randint(1,1000) 
while intentos<numero:
    print(
    """
    +================================+
    | Welcome to my game, muggle!    |
    | Enter an integer number        |
    | and guess what number I've     |
    | picked for you.                |
    | So, what is the secret number? |
    +================================+
    """)
    estimacion=input()
    estimacion=int(estimacion)
    intentos=+1
    if estimacion<numero:
        print("you're far away!")
    if estimacion>numero:
        print("you're near!")    
    if estimacion==numero:
        break

if estimacion==numero:  
    intentos=str(intentos)    
    print("Diste con el numero! en solo: " + intentos + "intentos")