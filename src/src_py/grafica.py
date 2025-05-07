import matplotlib.pyplot as plt


x = [1,2,3,4,5]
y= [2,4,6,8,10]

# Crear un grafic en lineas 
plt.plot ( x, y, label = "linea" , color= "blue")

# Agregar parametros
plt.title ("Grafico de Ejemplo con Matplotlib")
plt.xlabel ("eje de la x")
plt.ylabel ("eje de la y")

# agregar leyenda
plt.legend()

# Mostrar mi ventana
plt.show()