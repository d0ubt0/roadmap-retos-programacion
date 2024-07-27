class Deque:
    def __init__(self,lista :iter = list()) -> None:
        self.lista = list(lista)
        self.posicion = 0

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

    def back(self):
        if self.posicion != 0:
            self.posicion -=1
        else:
            print('No podemos retroceder mas')
    
    def next(self):
        if self.posicion != len(self.lista) -1:
            self.posicion +=1
        else:
            print('No podemos avanzar mas')
    
    def show_list(self):
        print(self.lista)

    def data_position(self):
        return  self.lista[self.posicion]

class PaginaWeb:
    def  __init__(self,paginas:iter  = ['Menu']) -> None:
        self.paginas = Deque(paginas)
        self.ui()

    def ui(self):
        print('\n\nPagina WEB')
        while True:
            print(f'\nActualmente estamos en {self.paginas.data_position()}')
            print('\nQue quieres hacer:')
            print('Pagina Siguiente: [Siguiente]')
            print('Pagina Anterior: [Anterior]')
            print('Salir del Programa: [Salir]')
            print('O puedes crear otra pagina escribiendo su nombre')

            user_input = input('Escribe el comando: ').lower()

            match user_input:
                case 'siguiente':
                    self.paginas.next()
                case 'anterior':
                    self.paginas.back()
                case 'salir':
                    break
                case _:
                    self.paginas.append(user_input)

class Impresora:
    def __init__(self,documentos:iter = None) -> None:
        if documentos == None:
            self.documentos = Deque()
        else:
            self.documentos = Deque(documentos)

        self.ui()
    
    def ui(self):
        print('\n\nImpresora')
        while True:
            print('\nQue quieres hacer:')
            print('Imprimir: [Imprimir]')
            print('Salir: [Salir]')
            print('O puedes colocar otra hoja escribiendo su nombre')

            user_input = input('Escribe el comando: ').lower()

            match user_input:
                case 'imprimir':
                    output_popleft = self.documentos.popleft()
                    if  output_popleft:
                        print(f'Pagina {output_popleft} impresa')
                    else:
                        print('\nNo hay paginas para imprimir')
                case 'salir':
                    print('\n\nSALIENDO DEL PROGRAMA\n\n')
                    break
                case _:
                    self.documentos.append(user_input)
                    print(f'Pagina {user_input} agregada a la cola')



                

        
pagina1 = PaginaWeb(range(1,4))
impresora = Impresora()
