#Clase Deque(Combinacion de Stack y Queve)
class Deque:
    def __init__(self,lista :iter = list()) -> None:
        self.lista = list(lista)  

    def pop(self):
        if len(self.lista)>0:
            return self.lista.pop()
        return None
        
    
    def popleft(self):
        if len(self.lista)>0:
            return self.lista.pop(0)
        return None
    
    def peek(self):
        if len(self.lista)>0:
            return self.lista[-1]
        return None
    
    def peekleft(self):
        if len(self.lista)>0:
            return self.lista[0]
        return None
    
    def append(self, valor):
        self.lista.append(valor)

    def appendleft(self, valor):
        self.lista.insert(0,valor)

    def show(self):
        print(self.lista)
    
    def len(self):
        return len(self.lista)

  
deque = Deque(range(1,5))
deque.append(10)
deque.append(30)
deque.show()
print(deque.len())
deque.popleft()
deque.pop()
deque.show()