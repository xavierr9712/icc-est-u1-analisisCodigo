
from metodoso_ordenamiento import MetodosOredenamiento
import random
import time
class Benchmarking:

    def __init__(self):
        print("Benchmarkin instanciado")

    def medir_tiempo(self, funcion, arreglo):
        inicio = time.perf_counter()
        funcion (arreglo)
        fin = time.perf_counter()
        return (fin - inicio)


    #public
    def metod(self):
        print ('Benchmarkin instanciado')

        # self.mO = MetodosOredenamiento()
        # #mO.bumbble_sort

        # arreglo = self.build_arreglo(10000)

        # tarea = lambda: self.mO.bumbble_sort(arreglo)
        # # tarea = () ->

        # milisegundo = self.contar_con_current_time_milles(tarea)
        # tiemponano = self.contar_con_current_time(tarea)

        # print (f" tiempo en milisegundos: {milisegundo}\n tiempo nanosegundos: {tiemponano}")


        # tarea_burbuja_mejorado = lambda: self.mO.sort_burbuja_mejorado_optimizado (arreglo)
        # tiemponano1 = self.contar_con_current_time(tarea_burbuja_mejorado)
        # print (f" tiempo en nanoseguntos burbuja mejorado: {tiemponano1}")

        # tarea_seleccion = lambda: self.mO.sort_seleccion (arreglo)
        # tiemponano2 = self.contar_con_current_time(tarea_seleccion)
        # print(f" tiempo en nanosegundos metodo seleccion: {tiemponano2}")

        # tarea_shell = lambda: self.mO.ordenShell(arreglo)  
        # tiemponano3 = self.contar_con_current_time(tarea_shell)
        # print(f" tiempo en nanosegundos metodo shell: {tiemponano3}")


    def build_arreglo(self, tamano):
        arreglo = []
        for i in range (tamano):
            numero = random.randint (0, 99999)
            arreglo.append(numero)
        return arreglo
    # importar time : clase archivo 
    # milisegundos en segundos con # x = time.time()
    # nanoseguhndo con # x = time.time_ns()
    # ejecutar es tarea()

    def contar_con_current_time_milles(self, tarea):
        inicio = time.time()
        tarea()
        fin = time.time()
        return(fin-inicio)/1000

        
    def contar_con_current_time(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return(fin-inicio)/1000_000_000
    
    
    
   