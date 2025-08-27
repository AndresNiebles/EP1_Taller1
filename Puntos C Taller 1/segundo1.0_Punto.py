import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# -------------------------------
# Ingreso de coeficientes
# -------------------------------
print("Función de transferencia: G(s) = (b0*s + b1) / (a0*s^2 + a1*s + a2)")
b0 = float(input("Ingrese el coeficiente b0 (multiplica s): "))
b1 = float(input("Ingrese el coeficiente b1 (término independiente): "))
a0 = float(input("Ingrese el coeficiente a0 (s^2): "))
a1 = float(input("Ingrese el coeficiente a1 (s): "))
a2 = float(input("Ingrese el coeficiente a2 (constante): "))

# -------------------------------
# Determinar tipo de sistema
# -------------------------------
# Forma general: a0*s^2 + a1*s + a2
# Comparación con s^2 + 2ζωn s + ωn^2
# ωn = sqrt(a2/a0), ζ = a1 / (2*sqrt(a0*a2))
wn = np.sqrt(a2 / a0)
zeta = a1 / (2 * np.sqrt(a0 * a2))

if zeta < 1:
    tipo = "Subamortiguado"
elif np.isclose(zeta, 1, atol=1e-3):
    tipo = "Críticamente amortiguado"
else:
    tipo = "Sobreamortiguado"

print(f"\nFrecuencia natural (ωn): {wn:.4f}")
print(f"Factor de amortiguamiento (ζ): {zeta:.4f}")
print(f"Tipo de sistema: {tipo}")

# -------------------------------
# Crear función de transferencias
# -------------------------------
num = [b0, b1]
den = [a0, a1, a2]

sistema = signal.TransferFunction(num, den)

# -------------------------------
# Respuesta al escalón
# -------------------------------
t = np.linspace(0, 10, 1000)  # 10 segundos
t, y = signal.step(sistema, T=t)

# -------------------------------
# Graficar
# -------------------------------
plt.figure(figsize=(8, 6))
plt.plot(t, y, label=f'{tipo} (ζ={zeta:.2f}, ωn={wn:.2f})', color="blue")
plt.axhline(1, color='gray', linestyle='--', label='Valor final (1)')
plt.title("Respuesta al escalón de un sistema de 2° orden", fontsize=14)
plt.xlabel("Tiempo (s)")
plt.ylabel("Salida")
plt.grid(True)
plt.legend()
plt.show()
