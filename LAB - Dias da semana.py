#O construtor de classe aceita um argumento - uma string. A string representa o nome do dia da semana e os únicos valores aceitáveis devem vir do seguinte conjunto:
#Mon Thu Wed Thu Fri Sat Sun
#Invocar o construtor com um argumento de fora deste conjunto deveria levantar a exceção WeekDayError (defina-a você mesmo; não se preocupe, em breve falaremos sobre a natureza objetiva das exceções). A classe deve fornecer as seguintes facilidades:
#os objetos da classe devem ser "imprimíveis", ou seja, devem ser capazes de se converter implicitamente em strings da mesma forma que os argumentos do construtor;
#a classe deve ser equipada com métodos de um parâmetro chamado add_days(n) e subtract_days(n), sendo n um número inteiro e atualizando o dia da semana armazenado dentro do objeto de forma a refletir a mudança de data pelo número de dias indicado, para a frente ou para trás.
#todas as propriedades do objeto devem ser privadas;
#Complete o modelo que fornecemos no editor e execute o seu código e verifique se o seu output tem o mesmo aspeto que o nosso.
class WeekDayEror(Exception):
    pass


class Weeker:
    __names = ['Mon', 'Thu', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


    def __init__(self, day):
        try:
            self.__current = Weeker.__names.index(day)
        except ValueError:
            raise WeekDayEror


    def __str__(self):
        return Weeker.__names[self.__current]


    def add_days(self, n):
        self.__current = (self.__current + n) % 7


    def subtract_days(self, n):
        self.__current = (self.__current - n) % 7


try:
    Weekday = Weeker('Mon')
    print(Weekday)
    Weekday.add_days(15)
    print(Weekday)
    Weekday.subtract_days(23)
    print(Weekday)
    Weekday = Weeker('Monday')
except WeekDayEror:
    print("Sorry, E can't serve your request")