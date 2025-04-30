import java.util.Arrays;

public class MetodosOrdenamiento {

    // Método de burbuja tradicional con errores
    // Error encontrado: el retur devuelve un error vacio-return new int[] {};
    // solucion: el codigo deve devolver-return arreglo 
    public int[] burbujaTradicional(int[] arregloOriginal) {
        int[] arreglo = Arrays.copyOf(arregloOriginal, arregloOriginal.length);

        int n = arreglo.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (arreglo[i] > arreglo[j]) {
                    // Intercambio de elementos
                    int temp = arreglo[i];
                    arreglo[i] = arreglo[j];
                    arreglo[j] = temp;
                }
            }
        }
        return arreglo;
    }

    // Método de burbuja tradicional con errores
    // Error encontrado:
     // Método de burbuja tradicional con errores
    // Error encontrado: La condición del if estaba ordenando el arreglo de forma descendente (< en lugar de >).
    // solucion: Se cambió la condición del if a (arreglo[i] > arreglo[j]) para ordenar ascendentemente.

    public int[] burbujaTradicionalSegundo(int[] arregloOriginal) {
        int[] arreglo = Arrays.copyOf(arregloOriginal, arregloOriginal.length);

        int n = arreglo.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (arreglo[i] > arreglo[j]) {
                    // Intercambio de elementos
                    // Estas 3 lineas NO DEBEN ser modificadas
                    int temp = arreglo[i];
                    arreglo[i] = arreglo[j];
                    arreglo[j] = temp;
                }
            }
        }

        return arreglo;

    }

    // Método de burbuja tradicional con errores
    // Error encontrado:El bucle interno recorría todo el arreglo en 
    // cada iteración del bucle externo- for (int j = 0; j < n ; j++) {
    // solucion:ajustó el límite del bucle interno a (n - i - 1) para 
    // evitar comparaciones innecesarias y el error de índice.
    public int[] burbujaTradicionalTercero(int[] arregloOriginal) {

        int[] arreglo = Arrays.copyOf(arregloOriginal, arregloOriginal.length);

        int n = arreglo.length;
        for (int i = 0; i < n -1; i++) {
            for (int j = 0; j < n - i -1 ; j++) {
                if (arreglo[j] > arreglo[j + 1]) {
                    // Intercambio de elementos
                    int temp = arreglo[j];
                    arreglo[j] = arreglo[j + 1];
                    arreglo[j + 1] = temp;
                }
            }
        }
        return arreglo;
    }

    // Método de selección con errores
    // Error encontrado: El método no devolvía ningún valor.
    // solucion: Se agregó la sentencia 'return arreglo;' al final del método.

    public int[] seleccionPrimero(int[] arregloOriginal) {

        int[] arreglo = Arrays.copyOf(arregloOriginal, arregloOriginal.length);

        for (int i = 0; i < arreglo.length - 1; i++) {
            int indiceMinimo = i;
            for (int j = i + 1; j < arreglo.length; j++) {
                if (arreglo[j] < arreglo[indiceMinimo]) {
                    indiceMinimo = j;
                }
            }
            int smallerNumber = arreglo[indiceMinimo];
            arreglo[indiceMinimo] = arreglo[i];
            arreglo[i] = smallerNumber;
        }
        return arreglo;

    }

    // Método de selección con errores
    // Error encontrado: el bucle esta mermando: j-- 
    // Solucion :bucle j++.
    public int[] seleccionSegundo(int[] arregloOriginal) {

        int[] arreglo = Arrays.copyOf(arregloOriginal, arregloOriginal.length);

        for (int i = 0; i < arreglo.length; i++) {
            int indiceMinimo = i;

            for (int j = i + 1; j < arreglo.length; j++) {
                if (arreglo[j] < arreglo[indiceMinimo]) {
                    indiceMinimo = j;
                }
            }

            int smallerNumber = arreglo[indiceMinimo];
            arreglo[indiceMinimo] = arreglo[i];
            arreglo[i] = smallerNumber;
        }
        return arreglo;
    }

    // Método de selección con errores
    // Error encontrado: el error esta en arreglo[indiceMinimo] = arreglo[i]; 
    // Solucion: se corrigio arreglo[i] = arreglo[indiceMinimo];.
    
    public int[] seleccionTercero(int[] arregloOriginal) {

        int[] arreglo = Arrays.copyOf(arregloOriginal, arregloOriginal.length);

        for (int i = 0; i < arreglo.length - 1; i++) {
            int indiceMinimo = i;

            for (int j = i + 1; j < arreglo.length; j++) {
                if (arreglo[j] < arreglo[indiceMinimo]) {
                    indiceMinimo = j;
                }
            }

            int smallerNumber = arreglo[i];
            arreglo[i] = arreglo[indiceMinimo];
            arreglo[indiceMinimo] = smallerNumber;
        }
        return arreglo;
    }

    // Método de inserción con errores
    // Error encontrado:
    // En while era i > 0 no se comparara correctamente el primer elemento 
    // y el  while estaba ordenando de forma descendente (arreglo[i] < key).
    // Solucion: correguimos while a i >= 0 y correguimos while a arreglo[i] > key para ordenar ascendentemente.
    public int[] insercionPrimero(int[] arregloOriginal) {

        int[] arreglo = Arrays.copyOf(arregloOriginal, arregloOriginal.length);
        for (int j = 1; j < arreglo.length; j++) {
            int key = arreglo[j];
            int i = j - 1;

            while (i >= 0 && arreglo[i] > key) {
                arreglo[i + 1] = arreglo[i];
                i--;
            }
            arreglo[i + 1] = key;
        }
        return arreglo;
    }

    // Método de inserción con errores
    // Error encontrado: Error en   for (; j >= 0 && arreglo[j] > actual; j--)
    // deberia ser while y deberea ser i envez de j y arreglo en [i] > actual
    // y luego agregar i -- despues el error tambien esta en  arreglo[j + 1] = arreglo[j] 
    // porque debe ser i 
    // Solucion: Se puso el bucle interno a un bucle while poniendolo correctamente
    // para el algoritmo de inserción ascendente.
    //  while ( i >= 0 && arreglo[i] > actual) {
    //  arreglo[i + 1] = arreglo[i];
    //  i--;
    public int[] insercionSegundo(int[] arregloOriginal) {

        int[] arreglo = Arrays.copyOf(arregloOriginal, arregloOriginal.length);
        for (int j = 1; j < arreglo.length; j++) {
            int actual = arreglo[j];

            int i = j - 1;
            while ( i >= 0 && arreglo[i] > actual) {
                arreglo[i + 1] = arreglo[i];
                i--;
            }
            arreglo[i + 1] = actual;
        }
        return arreglo;
    }

    // Método de inserción con errores
    // Error encontrado: En el bucle while falta el = en i > y arreglo[i] < key la condicion es >.
    // en el bucle whilw  tambein hay error en i++;
    // el metodo retorna al arreglo. no esto return new int[] { 15, 34, 1, 2, 5, 6, 7, 10 };
    // y tambien hay error en int i = j;
    // Solucion: se cambia  int i = j; por int i = j - 1; tambien 
    // se cambia la condicion arreglo[i] > key 
    // para oredenar ascendentemente.
    // el incremento se cambia a i -- y  return new int[] { 15, 34, 1, 2, 5, 6, 7, 10 }; por return arreglo; 
    public int[] insercionTercero(int[] arregloOriginal) {

        int[] arreglo = Arrays.copyOf(arregloOriginal, arregloOriginal.length);
        for (int j = 1; j < arreglo.length; j++) {
            int key = arreglo[j];
            
            int i = j-1;

            while (i >= 0 && arreglo[i] > key) {
                arreglo[i + 1] = arreglo[i];
                i--;
            }
            arreglo[i + 1] = key;
        }
        return arreglo;
    }

}
