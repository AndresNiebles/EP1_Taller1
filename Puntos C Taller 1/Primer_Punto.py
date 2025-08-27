import matplotlib.pyplot as plt
import numpy as np

# Parámetros del PT100
R0 = 100  # Resistencia a 0°C en ohmios
alpha = 0.00385  # Coeficiente de temperatura

# Rango de temperatura (de -200 a 200 °C)
temperaturas = np.linspace(-200, 200, 400)  # 400 puntos
resistencias = R0 * (1 + alpha * temperaturas)  # Fórmula R(T) = R0 * (1 + αT)

# Crear la gráfica
plt.figure(figsize=(8, 6))
plt.plot(temperaturas, resistencias, color="blue", linewidth=2)
plt.title("Comportamiento de un sensor PT100", fontsize=14)
plt.xlabel("Temperatura (°C)", fontsize=12)
plt.ylabel("Resistencia (Ω)", fontsize=12)
plt.grid(True)

# Agregar puntos clave con anotaciones
plt.scatter([0, 100, 200], [R0, R0 * (1 + alpha * 100), R0 * (1 + alpha * 200)], color="red")
plt.text(0, R0, f"{R0:.2f}Ω", ha='left', va='bottom', fontsize=10, color="red")
plt.text(100, R0 * (1 + alpha * 100), f"{R0 * (1 + alpha * 100):.2f}Ω", ha='left', va='bottom', fontsize=10, color="red")
plt.text(200, R0 * (1 + alpha * 200), f"{R0 * (1 + alpha * 200):.2f}Ω", ha='left', va='bottom', fontsize=10, color="red")

# Mostrar la gráfica
plt.show()
