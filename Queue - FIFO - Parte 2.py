#A sua tarefa é alargar ligeiramente as capacidades da classe Queue . Queremos que ele tenha um método sem parâmetros
#que devolva True se a queue estiver vazia e False caso contrário.

#Complete o código que fornecemos no editor. Execute-o para verificar se ele produz um resultado semelhante ao nosso.
class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []


    def put(self, elem):
        self.queue.insert(0, elem)


    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError


class SuperQueue(Queue):
    def isempty(self):
        return len(self.queue) == 0


que = SuperQueue()
que.put(1)
que.put('dog')
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print('Queue empty')
