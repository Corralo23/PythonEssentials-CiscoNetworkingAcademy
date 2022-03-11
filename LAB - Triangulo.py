#Vamos agora incorporar a classe Point (ver Lab 3.4.1.14) dentro de outra classe. Além disto, vamos colocar três pontos numa classe, o que nos permitirá definir um triângulo. Como podemos fazer isto?

#A nova classe será chamada Triangle e esta é a lista das nossas expetativas:

#o construtor aceita três argumentos - todos eles são objetos da classe Point ;
#os pontos são armazenados dentro do objeto como uma lista privada;
#a classe fornece um método sem parâmetros chamado perimeter(), que calcula o perímetro do triângulo descrito pelos três pontos; o perímetro é uma soma de todos os comprimentos das pernas (mencionamo-lo para registo, embora estejamos certos de que o conhece perfeitamente.)
#Complete o template que fornecemos no editor. Execute o seu código e verifique se o perímetro avaliado é igual ao nosso.
import math

class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.__x = x
        self.__y = y


    def getx(self):
        return self.__x


    def gety(self):
        return self.__y


    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))


    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]


    def perimeter(self):
        per = 0
        for i in range(3):
            per += self.__vertices[i].distance_from_point(self.__vertices[(i + 1) % 3])
        return per


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
