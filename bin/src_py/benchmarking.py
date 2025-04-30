
from metodoso_ordenamiento import MetodosOredenamiento
import random
import time
class Benchmarkin:

    #public
    def __init__(self):
        print ('Benchmarkin instanciado')

        self.mO = MetodosOredenamiento()
        #mO.bumbble_sort

        arreglo = self.build_arreglo(10000)

        tarea = lambda: self.mO.bumbble_sort(arreglo)
        # tarea = () ->

        milisegundo = self.contar_con_current_time_milles(tarea)
        tiemponano = self.contar_con_current_time(tarea)

        print (f" tiempo en milisegundos: {milisegundo}\n tiempo nanosegundos: {tiemponano}")


        tareaburbujamejorado = lambda: self.mO.sort_burbuja_mejorado_optimizado (arreglo)
        tiemponano1 = self.contar_con_current_time(tareaburbujamejorado)
        print (f"tiempo en nanoseguntos burbuja mejorado: {tiemponano1}")

        tareaseleccion = lambda: self.mO.sort_seleccion (arreglo)
        tiemponano2 = self.contar_con_current_time(tareaseleccion)
        print(f"tiempo en nanosegundos: {tiemponano2}")


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
    
    
   