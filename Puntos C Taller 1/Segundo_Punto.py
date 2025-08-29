import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


# Entrada de coeficientes
print("Función de transferencia: G(s) = K * ω_n^2 / (s^2 + 2ζω_n s + ω_n^2)")
K = float(input("Ingrese la ganancia K: "))
wn = float(input("Ingrese la frecuencia natural (ω_n): "))
zeta = float(input("Ingrese el coeficiente de amortiguamiento (ζ): "))


# Clasificación del sistema
if zeta < 1:
    tipo = "Subamortiguado"
elif np.isclose(zeta, 1, atol=1e-3):
    tipo = "Críticamente amortiguado"
else:
    tipo = "Sobreamortiguado"

print(f"Tipo de sistema: {tipo}")

# Función de transferencia
num = [K * wn**2] 
den = [1, 2*zeta*wn, wn**2]

# Crear sistema
sistema = signal.TransferFunction(num, den)


# Respuesta al escalón
t = np.linspace(0, 10, 1000)  # 10 segundos
t, y = signal.step(sistema, T=t)


# Gráfica
plt.figure(figsize=(8, 6))
plt.plot(t, y, label=f'{tipo} (ζ={zeta}, ωn={wn}, K={K})', color="blue")
plt.axhline(K, color='gray', linestyle='--', label=f'Valor final ({K})')
plt.title("Respuesta al escalón unitario de un sistema de 2° orden", fontsize=14)
plt.xlabel("Tiempo (s)")
plt.ylabel("Salida")
plt.grid(True)
plt.legend()
plt.show()
