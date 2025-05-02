import benchmarking as bm
#from benchmarking import Benchmarking
from metodoso_ordenamiento import MetodosOredenamiento
# archivo principal o main
if __name__=="__main__":

    print ("funciona")
    bench = bm.Benchmarking()
    metodosO = MetodosOredenamiento()

    ##tam = 10000
    tamanios = [5000, 10000, 20000]
    resultados = []

    for tam in tamanios:
        arreglo_base = bench.build_arreglo(tam)   

        key = "burbuja",
        value = metodosO.bumbble_sort

    

        metodos_dic = {
            "burbuja": metodosO.bumbble_sort,
            "burbuja mejorado": metodosO.sort_burbuja_mejorado_optimizado,
            "seleccion": metodosO.sort_seleccion,
            "shell": metodosO.ordenShell
        }

        resultados = []
    

        for nombre, fun_metodo in metodos_dic.items():
            tiempo_resultado = bench.medir_tiempo (fun_metodo, arreglo_base)
            tupla_resultado = (tam, nombre, tiempo_resultado)
            resultados.append(tupla_resultado)
    
        for tam, nombre, tiempo in resultados:
            print (f'Tamaño:{tam}, nombre {nombre}, Tiempo: {tiempo:.6f} segundo')

    




    