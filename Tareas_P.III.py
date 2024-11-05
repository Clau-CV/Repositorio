import numpy as np
import matplotlib.pyplot as plt

from T_203 import abs_X

# 1. Genera un arreglo 1D, llamado freq, de 4 elementos de números aleatorios enteros en el intervalo [1, 8]
freq = [1, 4, 6, 8] # np.random.randint(1, 8, size = [4])

# 2. Genera un arreglo 1D, llamado amplitud, de 4 elementos de números aleatorios con distribución uniforme
# en el intervalo [3, 6]
amplitud = [3.1, 3.8, 4.4, 5.2] # np.random.uniform(3, 6, size= 4)

# 3. Use el metodo arange para generar un arreglo, llamado t, de 2000 números en el intervalo [0, 1]
t = np.arange(0, 1, 1/2000)

# 4. Genere 4 ondas sinusoidales con cada frecuencia y amplitud.
# Hint: recuerde que la ecuación de la onda sinusoidal es y(t) = A*sin(2*piB*t) donde A es la amplitud y B es la
# frecuencia. Para usar pi en numpy, use np.pi
# Sugerencia: para visualizar las ondas sinusoidales puede usar las líneas de código
t = np.linspace(0, 1, 1000) # Definir tiempo entre 0 y 1s con 1000 puntos
amplitudes = [1, 2, 0.5, 1.5]
frequencies = [1, 3, 5, 7]
plt.figure(figsize=(10, 6)) # Graficar
for i in range(4):
    A = amplitudes[i]
    B = frequencies[i]
    y = A * np.sin(2 * np.pi * B * t)  # Generación onda sinusoidal
    plt.plot(t, y, label=f'Amplitud: {A}, Frecuencia: {B} Hz')  # Graficamos cada onda con una etiqueta
plt.show()

# 5. Cree un arreglo llamado x, que sea la suma de las 4 ondas sinusoidales
x = np.zeros_like(t)
for i in range(4):
    x += amplitudes[i] * np.sin(2 * np.pi * frequencies[i] * t) #Sumar ondas
plt.plot(t, x)
plt.show() #Visualizar

# Numpy también permite aplicar operadores tales como la transormada de fourier a un arreglo de datos con
# el paquete np.fft, en particular la función np.fft.fft(x) aplica la transformada discreta de fourier al arreglo x
X = np.fft.fft(x)

# 6. Cree un arreglo, llamado frequence, de los enteros en el intervalo [0, 1999]
frequence = range(2000)

# 7. Calcular el valor absoluto a todos los elementos del arreglo X
absX = np.abs(x)

# 8. De los primeros 10 elementos del arreglo del ejercicio anterior, determine los 4 elementos máximos y en
# qué índices se localizan
print(absX[:10])

# Para mostrar la frecuencia y la amplitud en el dominio de Fourier use las siguientes líneas de código
plt.stem(frequence[:10], absX[:10])
plt.show()
