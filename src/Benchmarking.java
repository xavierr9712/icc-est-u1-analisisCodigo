import java.util.Random;

public class Benchmarking {

    private MetodosOrdenamiento mOrdenamiento;

    public Benchmarking (){

        long currentMillis = System.currentTimeMillis();
        long currentNano = System.nanoTime();

        System.out.println();
        System.out.println("Resultado benchmarking: ");
        System.out.println(currentMillis);
        System.out.println(currentNano);

        mOrdenamiento = new MetodosOrdenamiento();

        int [ ] arreglo = genrrarArregloAleatorio(1000);

        Runnable tarea = ()-> mOrdenamiento.burbujaTradicional(arreglo);

        
        double tiempoDuracionMillis= medirConCurrentTimeMiles(tarea);
        double tiempoDuracionNano= medirConNanoTime(tarea);

        System.out.println();
        System.out.println("Tiempo en millis: " + tiempoDuracionMillis);
        System.out.println("Tiempo en nano: " + tiempoDuracionNano);

    }

    private int [ ] genrrarArregloAleatorio (int tamano ){
        // 0 al 99.999
        int [] arreglo = new int [tamano];
        Random random = new Random();
        
        for ( int i = 0; i < tamano; i++) {
            arreglo [i] = random.nextInt(100000);

        }

        return arreglo;

    }
    public double medirConCurrentTimeMiles(Runnable tarea){
        long  inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        double tiempoSegundos = (fin - inicio) / 1000.0;
        return tiempoSegundos;
    }
    public double medirConNanoTime (Runnable tarea){
        long  inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        double tiempoSegundos = (fin - inicio) / 1000_000_000.0;
        return tiempoSegundos;
    }
}
