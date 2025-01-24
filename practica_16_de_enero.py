#Medir distancia entre dos puntos (3,4) (7,1) =5
import math
coor1=[]
coor2=[]

x =int(input("Primer coordenada primer punto: "))
coor1.append(x)
x =int(input("Primer coordenada segundo punto: "))
coor1.append(x)
x =int(input("Segunda coordenada primer punto: "))
coor2.append(x)
x =int(input("Segunda coordenada segundo punto: "))
coor2.append(x)

resultado = math.sqrt((((coor2[0]-coor1[0])**2)+((coor2[1]-coor1[1])**2)))

print("El resultado es: ", resultado)