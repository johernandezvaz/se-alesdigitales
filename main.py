import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import math

# Caracteristicas de nuestra señal

freq = 123.47 # Do Octava 5
amplitude = 0.3
duration = 1.0 # Medida en segundos
sample_rate = 44100 # Muestras por segundo

# Arreglo de tiempo

t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)

# Señal "analógica"
signal = amplitude  * np.sin(2 * math.pi * freq * t)



def main():
    # Crear imagén
    plt.plot(t, signal)
    plt.show()


    # Generar el sonido
    sd.play(signal, sample_rate)
    sd.wait()



if __name__ == "__main__":
    main()
