"""
listas
"""

lista1=[10,5,3]
lista2=[1.5,2.66,1.70,89.2]
lista3=["Lunes","Martes","Miercoles"]
lista4=["Juan",45,1.92]

print(type(lista1)) #Muestra el tipo de datos
print(len(lista1)) #Muestra el tamaño de la lista 


print(lista1[0])

suma=0
x=0

while x<len(lista1):
    suma= suma + lista1[x]
    x=x+1
print("La suma es: {}".format(suma)) 
print(lista1)
print(lista1[0])
lista1.append(100) #Agrega un elemento a la lista 
print(lista1)
print(lista1[3])


lista5=[] #Crea una lista vacia 
for x in range(5):
    valor=int(input("Ingresa un valor:")) 
    lista5.append(valor)
    #Agrega valores a la lista mediente un for y la entrada de texto de "valor" para agregarlo en "lista5.append(valor)"
print(lista5)    

#Eliminar elementos de listas 
print(lista1)    
lista1.pop()
print(lista1)    

print("-----Pares o Inpares-----")

numero=int(input("Cuantos numeros se ingresaran?"))
lista6=[]
pares=""
inpares=""
for x in range(numero):
    ing=int(input("Ingresa un valor:"))
    lista6.append(ing)

print(lista6)
z = 0
while z<=numero:
    if lista6[z] % 2 == 0:
        pares = pares + str(lista6[z]) + " "
        z=z+1
    else:
        inpares = inpares + str(lista6[z]) + " "
        z=z+1
        
print(pares)        
print(inpares)        
print("-------------")

lista1.sort()#Ordena la lista 
print(lista1)
lista1.reverse()
print(lista1)

lista1.remove(10)
print(lista1) #?

lista1.clear()
print(lista1) #?