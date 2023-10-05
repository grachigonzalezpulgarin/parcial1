""" 
___________     Parcial 1    ___________________
    INTEGRANTES:
        Grachi Gonzalez Pulgarin
 """
#importamos statistics Este módulo proporciona funciones para calcular estadísticas matemáticas de datos numéricos
#importamos random numeros aleatorios
#primer parametro para el metodo instacia self
import random
import statistics

class ListOperations: #class se le llama a los submenus
    def __init__(self, data):  #todo lo que se trata de operaciones
        self.data = data #POO se llama cada vez que se instancia una clase y sirve para iniciar el objeto que creamos 

    def generar_list_random(self): #el self hace referencia al nombre del objeto en el que se encuentra escrito, lo podemos reemplazar por el ombre de clase 
        self.data = [random.randint(1, 100) for _ in range(10)]
        print("Lista aleatoria generada.")

    def list_manual(self):
        try:
            input_list = input("Ingrese la lista separada por comas: ")
            self.data = [int(item.strip()) for item in input_list.split(',')]#Cada número se convierte en un entero y se almacena en la lista `self.data`
            print("Lista ingresada manualmente.")
        except ValueError as e: #saca una advertencia de un error
            print(f"Error al ingresar la lista: {e}")

    def list_previamente(self):#lista predeterminada
        self.data = [5, 2, 9, 1, 7, 8, 3, 6, 4, 10]
        print("Lista previamente cargada.")

    def crea_list_range(self):#cria lista de rangos
        try:
            start = int(input("Ingrese el valor inicial del rango: "))#numero incial
            end = int(input("Ingrese el valor final del rango: "))#numero final
            self.data = list(range(start, end + 1))#crea una lista con un rango con los numeros introducidos y el final se le suma 1 ya que el ultimo no se cuenta
            print("Lista creada desde rango.")
        except ValueError as e: #arroja un error
            print(f"Error al crear la lista desde el rango: {e}")

    def print_list(self):
        print("Lista actual:", self.data)#se almacena los datos y se reemplaza 

    def bubble_sort(self):#cuando es con burbuja lo ordena de menor a mayor 
        try:#itera sobre la lista, comparando elementos adyacentes y realizando intercambios si es necesario para asegurarse de que la lista esté ordenada de menor a mayor al final del proceso
            n = len(self.data)# calcule la longitud de los datos almacenados en el atributo self.datay la almacena en la variable n.
            for i in range(n - 1):#Controle la cantidad de pasos necesarios para asegurarse de que todos los elementos estén en su posición final
                for j in range(0, n - i - 1):#Este compara cada elemento con su siguiente y realiza un intercambio si el elemento actual es mayor que el siguiente.
                    if self.data[j] > self.data[j + 1]:#se compara con el sigueinte
                        self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]#Si el elemento actual es mayor que el siguiente
            print("Lista ordenada con burbuja:", self.data)
        except Exception as e:
            print(f"Error al ordenar con burbuja: {e}")

    def quick_sort(self):#busqueda rapida
        try:
            self.data = self._quick_sort(self.data)
            print("Lista ordenada con rápido:", self.data)
        except Exception as e:
            print(f"Error al ordenar con rápido: {e}")

    def _quick_sort(self, arr):#almacena varios elementos rapidos y que se va a ordenar
        if len(arr) <= 1: #si la longitud de la lista es menor o igual a 1 significa que la lista ya está ordenada.
            return arr
        else:
            pivot = arr[0] #selecciona el pivote de la lista
            less = [x for x in arr[1:] if x <= pivot] #elementos menores
            greater = [x for x in arr[1:] if x > pivot] #mayores
            return self._quick_sort(less) + [pivot] + self._quick_sort(greater)

    def compare_sorted(self):#compara la lista creada con la que se acaba de crear
        sorted_list = sorted(self.data)
        if self.data == sorted_list:
            print("La lista ya está ordenada.")
        else:
            print("La lista no está ordenada.")

    def linear_search(self, target):
        for i, element in enumerate(self.data):#busca la posicion en la que esta self.data
            if element == target: 
                print(f"{target} encontrado en la posición {i}.")
                return
        print(f"{target} no encontrado en la lista.")

    def binary_search(self, target): #busca en binario el objeto en la variable self
        try:
            self.data.sort() #ordena en orden ascendente
            low, high = 0, len(self.data) - 1 #izq y der de la sublista actual
            while low <= high:
                mid = (low + high) // 2 #calcula el indice medio
                if self.data[mid] == target: #compara la posicion del objeto
                    print(f"{target} encontrado en la posición {mid}.") #si se encuentra se imprime
                    return
                elif self.data[mid] < target:
                    low = mid + 1 # Si el elemento en la posición menor que el objetivo, se actualiza low para buscar en la mitad derecha
                else:
                    high = mid - 1 # Si es mayor, se actualiza high para buscar en la mitad izquierda.
            print(f"{target} no encontrado en la lista.")
        except Exception as e:
            print(f"Error al realizar la búsqueda binaria: {e}")

    def sum_elements(self):
        total = sum(self.data)
        print(f"La suma de los elementos es: {total}")

    def calculate_average(self):
        avg = statistics.mean(self.data)
        print(f"El promedio de la lista es: {avg}")

    def calculate_median(self): #agregarmos funcion para la libreria
        median = statistics.median(self.data)
        print(f"La mediana de la lista es: {median}")

    def calculate_variance(self): #agregamos la funcion varianza
        variance = statistics.variance(self.data)
        print(f"La varianza de la lista es: {variance}")

    def find_min_max(self): #para encontrar maximo y minimo de la lista
        if not self.data:
            print("La lista está vacía.")
            return
        min_val = min(self.data)
        max_val = max(self.data)
        print(f"El valor mínimo de la lista es: {min_val}")
        print(f"El valor máximo de la lista es: {max_val}")

    def show_length(self): # muestra la longitud de la lista
        length = len(self.data)
        print(f"La longitud de la lista es: {length}")

    def compare_with_other_list(self, other_list): #comparar con otras listas
        if self.data == other_list:
            print("Las listas son iguales.")
        else:
            print("Las listas son diferentes.")

def main():
    list_operations = ListOperations([]) #menu principal
    while True:
        print("\n--- Menú Principal ---")
        print("1. Generar lista aleatoria")
        print("2. Ingresar lista manualmente")
        print("3. Usar lista previamente cargada")
        print("4. Crear lista desde rango")
        print("5. Ir al Submenú")
        print("6.Ayuda")
        print("7. Salir")
        

        choice = input("Ingrese su elección: ")

        if choice == "1":
            list_operations.generar_list_random()
        elif choice == "2":
            list_operations.list_manual()
        elif choice == "3":
            list_operations.list_previamente()
        elif choice == "4":
            list_operations.crea_list_range()
        elif choice == "5":
            sub_menu(list_operations)
        elif choice == "6":
            print("La busqueda lineal recorre la lista de principio a fin hasta encontrar el elemento.")
            print("La busqueda binaria requiere que la lista este ordenada y encuentra el elemento dividiendo la lista en mitades.")
            print("El ordenamiento oir burbuja compara pares de elementos adyacentes y los intercammbia si esta en orden incorrecto.")
            print("El ordenamiento rapido utliza un elemento 'pivote' para dividir la lista y ordenarla de manera mas eficiente.")
        elif choice == "7":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

def sub_menu(list_operations):# submenu
    while True:
        print("\n--- Submenú ---")
        print("1. Imprimir lista")
        print("2. Ordenar con burbuja")
        print("3. Ordenar con rápido")
        print("4. Comparar con sorted")
        print("5. Buscar elemento (lineal)")
        print("6. Buscar elemento (binario)")
        print("7. Sumar elementos")
        print("8. Calcular promedio")
        print("9. Calcular mediana")
        print("10. Calcular varianza")
        print("11. Encontrar mínimo y máximo")
        print("12. Mostrar longitud de la lista")
        print("13. Comparar con otra lista")
        print("14. Volver al menú principal")

        sub_choice = input("Ingrese su elección: ")

        if sub_choice == "1":
            list_operations.print_list()
        elif sub_choice == "2":
            list_operations.bubble_sort()
        elif sub_choice == "3":
            list_operations.quick_sort()
        elif sub_choice == "4":
            list_operations.compare_sorted()
        elif sub_choice == "5":
            target = int(input("Ingrese el elemento a buscar: "))
            list_operations.linear_search(target)
        elif sub_choice == "6":
            target = int(input("Ingrese el elemento a buscar: "))
            list_operations.binary_search(target)
        elif sub_choice == "7":
            list_operations.sum_elements()
        elif sub_choice == "8":
            list_operations.calculate_average()
        elif sub_choice == "9":
            list_operations.calculate_median()
        elif sub_choice == "10":
            list_operations.calculate_variance()
        elif sub_choice == "11":
            list_operations.find_min_max()
        elif sub_choice == "12":
            list_operations.show_length()
        elif sub_choice == "13":
            other_list = enter_manual_list()
            list_operations.compare_with_other_list(other_list)
        elif sub_choice == "14":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
