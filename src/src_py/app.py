import matplotlib.pyplot as plt
import benchmarking as bm
#from benchmarking import Benchmarking
from metodoso_ordenamiento import MetodosOredenamiento
# archivo principal o main
if __name__=="__main__":

    print ("funciona")
    bench = bm.Benchmarking()
    metodosO = MetodosOredenamiento()

    ##tam = 10000
    tamanios = [500, 1000, 2000]
    metodos_dic = {
            "burbuja": metodosO.bumbble_sort,
            "burbuja mejorado": metodosO.sort_burbuja_mejorado_optimizado,
            "seleccion": metodosO.sort_seleccion,
            "shell": metodosO.ordenShell
        }
    resultados = []

    for tam in tamanios:
        arreglo_base = bench.build_arreglo(tam)   

        key = "burbuja",
        value = metodosO.bumbble_sort

        for nombre, fun_metodo in metodos_dic.items():
            tiempo_resultado = bench.medir_tiempo (fun_metodo, arreglo_base)
            tupla_resultado = (tam, nombre, tiempo_resultado)
            resultados.append(tupla_resultado)
    
        for tam, nombre, tiempo in resultados:
            print (f'Tamaño:{tam}, nombre {nombre}, Tiempo: {tiempo:.6f} segundo')

    # Preparar datos para ser graficados 
    # 1. crear un diccionario o mapa paara almaceanr resultados por metodo 
    tiempos_by_metodo = {
        "burbuja": [],
        "burbuja mejorado":[],
        "seleccion": [],
        "shell": [],
        }
    for tam, nombre, tiempo in resultados:
        tiempos_by_metodo[nombre].append(tiempo)
    plt.figure (figsize =(10, 6))

    # graficar los tiempos de ejecucion para cada metodo 
    for nombre, tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempos, label= nombre, marker="o")

    # agregar parametros 
    plt.figure ("Xavier Ortega")
    plt.title ("Comparacion de tiempos de ejecucion de algoritmos de ordenamiento")
    plt.xlabel ("tamaño de los arreglos")
    plt.ylabel ("tiempo de ejecucion")
    
    plt.legend()

    plt.show()
