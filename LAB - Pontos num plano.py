#É assim que imaginamos a classe:
#é chamada Point;
#o seu construtor aceita dois argumentos (x e y respetivamente), ambos a zero, por defeito;
#todas as propriedades devem ser privadas;
#a classe contém dois métodos sem parâmetros chamados getx() e gety(), que devolvem cada uma das duas coordenadas (as coordenadas são armazenadas de forma privada, pelo que não podem ser acedidas diretamente do interior do objeto);
#a classe fornece um método chamado distance_from_xy(x,y), que calcula e devolve a distância entre o ponto armazenado dentro do objeto e o outro ponto dado como um par de floats;
#a classe fornece um método chamado distance_from_point(point), que calcula a distância (como o método anterior), mas a localização do outro ponto é dada como outro Ponto objeto de classe;
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
        return self.distance_from_xy(point.gety(), point.gety())


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))