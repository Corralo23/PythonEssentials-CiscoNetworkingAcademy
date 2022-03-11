#Zero é o valor padrão para todos os parâmetros acima. Não há necessidade de efetuar quaisquer verificações de validação.
#A própria classe deve fornecer as seguintes facilidades:
#objetos da classe devem ser "imprimíveis", ou seja, devem ser capazes de se converter implicitamente em strings da seguinte forma: "hh:mm:ss", com zeros iniciais adicionados quando qualquer um dos valores for inferior a 10;
#a classe deve ser equipada com métodos sem parâmetros chamados next_second() e previous_second(), incrementando o tempo armazenado dentro dos objetos em +1/-1 segundo, respetivamente.
#Use as seguintes dicas:
#todas as propriedades do objeto devem ser privadas;
#considere escrever uma função separada (não um método!) para formatar a string de tempo.
#Complete o template que lhe fornecemos no editor. Execute o seu código e verifique se o output tem o mesmo aspeto que o nosso.
def two_digits(val):
    s = str(val)
    if len(s) == 1:
        s = '0' + s
    return s


class Timer:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds


    def __str__(self):
        return two_digits(self.__hours) + ':' + \
               two_digits(self.__minutes) + ':' + \
               two_digits(self.__seconds)


    def next_seconds(self):
        self.__seconds += 1
        if self.__seconds > 59:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes > 59:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours < 0:
                    self.__hours = 23


    def prev_seconds(self):
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours < 0:
                    self.__hours = 23



timer = Timer(23, 59, 59)
print(timer)
timer.next_seconds()
print(timer)
timer.prev_seconds()
print(timer)
