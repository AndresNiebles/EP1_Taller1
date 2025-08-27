import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Entrada de datos
# -------------------------------
V = float(input("Ingrese el voltaje en voltios (V): "))
R = float(input("Ingrese la resistencia en ohmios (Ω): "))
C_micro = float(input("Ingrese la capacitancia en microfaradios (μF): "))

# Conversión de microfaradios a faradios
C = C_micro * 1e-6

# Constante de tiempo tau
tau = R * C
print(f"\nConstante de tiempo (τ) = {tau:.6f} segundos")

# -------------------------------
# Cálculo del tiempo y voltajes
# -------------------------------
t = np.linspace(0, 5 * tau, 1000)  # Simulamos 5 constantes de tiempo

# Ecuación de carga y descarga
Vc_carga = V * (1 - np.exp(-t / tau))
Vc_descarga = V * np.exp(-t / tau)

# -------------------------------
# Graficar
# -------------------------------
plt.figure(figsize=(8, 6))
plt.plot(t, Vc_carga, label='Carga del capacitor', color='blue')
plt.plot(t, Vc_descarga, label='Descarga del capacitor', color='red', linestyle='--')
plt.axhline(V, color='gray', linestyle=':', label=f'Voltaje máximo ({V} V)')
plt.title('Carga y Descarga de un Circuito RC', fontsize=14)
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje en el capacitor (V)')
plt.grid(True)
plt.legend()
plt.show()
