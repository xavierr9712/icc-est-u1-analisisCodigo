class MetodosOredenamiento:

    def bumbble_sort (self, array):
        arreglo = array.copy()
        n = len (arreglo)
        for i in range (n):
            for j in range (i+1, n):
                if arreglo[i]>arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo [j], arreglo[i]
        return arreglo
    
    def sort_burbuja_mejorado_optimizado (self, array):
        arreglo = array.copy()
        n = len (arreglo)
        for i in range(n-1):       
            for j in range(n-1-i): 
                if arreglo[j] > arreglo[j+1]:
                    arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

    def  sort_seleccion (self, array):
        arreglo = array.copy()
        n = len ( arreglo)
        for i in range(len(arreglo) - 1):        
            for j in range(i + 1, len(arreglo)): 
                if arreglo[j] < arreglo[menor]:
                    menor = j
        if menor != i:
            arreglo[menor], arreglo[i] = arreglo[i], arreglo[menor]

        

                   




    
    


