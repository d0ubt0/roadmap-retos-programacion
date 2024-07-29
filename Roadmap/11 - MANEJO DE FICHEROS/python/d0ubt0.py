import os

file_name = 'd0ubt0.txt'

with open(file_name,'w+') as file:
    file.write('Sebastian\n')
    file.write('20\n')
    file.write('Python')
    file.seek(0)
    print(file.read())

    
os.remove(file_name)

print('\n-----------------------------------------------------\n')
#Ejercicio
class Product:
    def __init__(self,name:str,quantity:int,price:int) -> None:
        self.name  = name
        self.quantity = quantity
        self.price = price

    def __str__(self) -> str:
        return  f'{self.name}-{self.quantity}-{self.price}'
        
class SalesManagement:
    def __init__(self,file_name:str) -> None:
        self.file_name = file_name
        with open(self.file_name,'w') as file:
            pass
        self.run_console_interface()

    def add(self,product: Product):
        with open(self.file_name,'a') as file:
            file.write(f'{product}\n')
        print('----Producto agregado----')

    def _verify_number(self):
        user_input = input('Ingrese la nueva cantidad del producto: ')
        while not(user_input.isdigit()):
            print('Input invalido')
            user_input = input('Ingrese la nueva cantidad del producto: ')
        return user_input


    def remove(self,product_name:str):
        index = self._search_product(product_name)
        if index != None:
            with open(self.file_name,'r') as file:
                lines = file.readlines()
                del lines[index]

            with open(self.file_name,'w') as file:
                lines = file.writelines(lines)
                print('----Producto eliminado----')

    def update(self,product_name:str):
        index = self._search_product(product_name)
        if index != None:
            with open(self.file_name,'r') as file:
                lines = file.readlines()
    
            print(f'----Actualizar datos----\nDatos Actuales: {lines[index].strip()}')
            new_quantity = self._verify_number()
            new_price = self._verify_number()
            lines[index] = f'{product_name}-{new_quantity}-{new_price}\n'

            with open(self.file_name,'w') as file:
                lines = file.writelines(lines)
                print('----Producto Actualizado----')

    def see(self,product_name :str):
        index = self._search_product(product_name)
        if index != None:
            with open(self.file_name,'r') as file:
                current_line = 0
                for line in file:
                    if index == current_line:
                        print(line.strip())
                        break
                    current_line +=1

    def product_sale(self,product_name:str):
        index = self._search_product(product_name)
        if index != None:
            with open(self.file_name,'r') as file:
                current_line = 0
                for line in file:
                    if index == current_line:
                        line = line.strip().split('-')
                        return (int(line[1])*int(line[2]))
                    current_line +=1


    def total_sale(self):
        total = 0
        with open(self.file_name,'r') as file:
            for line in file:
                line = line.strip().split('-')
                total += (int(line[1])*int(line[2]))
        return total

    def _search_product(self,product_name:str):
        with open(self.file_name,'r') as file:
            lines = file.readlines()
            for i,line in enumerate(lines):
                data = line.split('-')
                if data[0] == product_name:
                    return i 
        print('----Producto no encontrado----')   
        return None     
    
    def run_console_interface(self):
        while True:
            print("\n--- Gestión de Ventas ---")
            print("1. Agregar Producto")
            print("2. Eliminar Producto")
            print("3. Actualizar Producto")
            print("4. Ver Producto")
            print("5. Ver Venta de Producto")
            print("6. Ver Venta Total")
            print("7. Salir")

            choice = input("Ingrese su opción: ")

            if choice == '1':
                name = input("Ingrese el nombre del producto: ")
                quantity = int(self._verify_number())
                price = int(self._verify_number())
                product = Product(name, quantity, price)
                self.add(product)

            elif choice == '2':
                name = input("Ingrese el nombre del producto a eliminar: ")
                self.remove(name)

            elif choice == '3':
                name = input("Ingrese el nombre del producto a actualizar: ")
                self.update(name)

            elif choice == '4':
                name = input("Ingrese el nombre del producto a ver: ")
                self.see(name)

            elif choice == '5':
                name = input("Ingrese el nombre del producto para ver la venta: ")
                sale = self.product_sale(name)
                if sale is not None:
                    print(f"La venta del producto {name} es: {sale}")

            elif choice == '6':
                total = self.total_sale()
                print(f"La venta total es: {total}")

            elif choice == '7':
                print("Saliendo...")
                os.remove(self.file_name)
                break

            else:
                print("Opción no válida. Inténtelo de nuevo.")
            
        
sales = SalesManagement('sales.txt')
        