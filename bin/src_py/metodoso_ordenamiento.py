class MetodosOredenamiento:

    def bumbble_sort (self, array):
        arreglo = array.copy()
        n = len (arreglo)
        for i in range (n):
            for j in range (i+1, n):
                if arreglo[i]>arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo [j], arreglo[i]
        return arreglo    
         
    def sort_burbuja_mejorado_optimizado(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
        return arreglo  

    def sort_seleccion(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n - 1):
            menor = i  
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[menor]:
                    menor = j
            if menor != i:
                arreglo[menor], arreglo[i] = arreglo[i], arreglo[menor]
        return arreglo  

    def ordenShell(self, lista):  
        arreglo = lista.copy()
        n = len(arreglo)
        inc = 1
        while inc <= n // 3:  
            inc = inc * 3 + 1
        while inc > 0:
            for i in range(inc, n):  
                j = i
                temp = arreglo[i]
                while j >= inc and arreglo[j - inc] > temp:  
                    arreglo[j] = arreglo[j - inc]
                    j = j - inc
                arreglo[j] = temp
            inc = inc // 3
        return arreglo


        

                   




    
    


