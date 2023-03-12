class Node:
    def __init__ (self, dato):
        self.data = dato
        self.next = None

    def getData (self):
        return self.data

    def setData (self, data):
        self.data = data

nodo1 = Node("Axelito")
# print(nodo1.data)
# print(nodo1.getData())
# print(nodo1.next)

nodo1.setData("Niñito")
# print(nodo1.getData())
# print(nodo1.data)

nodo2 = Node("Bonito")
nodo1.next = nodo2

nodo3 = Node("Axelito")
nodo2.next = nodo3

print("---->")
print(nodo1.data)
print(nodo1.next.data) #.next.data ---> se ubica en la siguiente direccion y te muestra con 'data' el elemento que tienes en esa misma
print(nodo1.next.next.data)
