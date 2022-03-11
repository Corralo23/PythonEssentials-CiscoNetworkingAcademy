#Uma queue (fila de espera) é um modelo de dados caraterizado pelo termo FIFO: First In - Fist Out. Nota:
#uma queue regular (fila) que conhece das lojas ou correios funciona exatamente da mesma maneira - um cliente que chegou primeiro
#também é servido primeiro.
#A sua tarefa é implementar a classe Queue com duas operações básicas:
#put(element), que coloca um elemento no final da queue;
#get(), que toma um elemento da frente da queue e o devolve como resultado (a queue não pode estar vazia para o executar com êxito.)
#Siga as dicas:

#utilize uma lista como seu aramazenamento (tal como fizemos na stack)
#put() deve anexar elementos ao início da lista, enquanto get() deve remover os elementos do final da lista;
#defina uma nova exceção chamada QueueError (escolha uma exceção para derivá-la) e levante-a quando get() tenta operar numa lista vazia.

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


que = Queue()
que.put(1)
que.put('dog')
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print('Queue error')
