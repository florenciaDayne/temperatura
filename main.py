from typing import List

class AnalizadorTemperaturas:
    def __init__(self):
        self.dias_semana = ["lunes", "martes", "miercoles", "jueves","viernes","sabado","domingo"]
        self.temperatura: List[float] = []

    def obtener_temperaturas(self):
        print("Ingrese las temperaturas de los 7 días:\n")
        for dia in self.dias_semana:
            while True:
                try:
                    temp = float(input(f"{dia} - temperatura (°C): "))
                    self.temperatura.append(temp)
                    break
                except ValueError:
                    print("Entrada no válida. Ingresa un número real.")

    def calcular_promedio(self):
        return sum(self.temperatura) / len(self.temperatura)

    def encontrar_max_min(self):
        max_temp = max(self.temperatura)
        min_temp = min(self.temperatura)
        dia_max = self.dias_semana[self.temperatura.index(max_temp)]
        dia_min = self.dias_semana[self.temperatura.index(min_temp)]
        return max_temp, dia_max, min_temp, dia_min

    def mostrar_temperaturas_superiores_al_promedio(self, promedio):
        print("\nDías con temperatura por encima del promedio")
        for i, temp in enumerate(self.temperatura):
            if temp > promedio:
                print(f"{self.dias_semana[i]}: {temp}°C")

    def mostrar_alertas(self):
        for i, temp in enumerate(self.temperatura):
            if temp > 40 or temp < 0:
                print(f"¡Alerta! Temperatura extrema el {self.dias_semana[i]}: {temp}°C")

    def mostrar_resultados(self):
        promedio = self.calcular_promedio()
        max_temp, dia_max, min_temp, dia_min = self.encontrar_max_min()

        print("\n--- Resultados ---")
        print(f"Temperatura máxima: {max_temp}°C ({dia_max})")
        print(f"Temperatura mínima: {min_temp}°C ({dia_min})")
        print(f"Promedio semanal: {promedio:.2f}°C")

        self.mostrar_temperaturas_superiores_al_promedio(promedio)
        self.mostrar_alertas()


# Función principal
def main():
    analizador = AnalizadorTemperaturas()  
    analizador.obtener_temperaturas()
    analizador.mostrar_resultados()  


if __name__ ==  "__main__":
    main()