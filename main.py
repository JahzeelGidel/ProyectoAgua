from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import StringProperty
import random

UMBRAL_DIF = 2.0  # Diferencia de presión para marcar filtro lleno

class FiltroWidget(BoxLayout):
    presion_antes = StringProperty("0.0 kPa")
    presion_despues = StringProperty("0.0 kPa")
    estado_texto = StringProperty("Esperando datos...")
    color_estado = StringProperty("#000000")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.actualizar, 1)  # Actualiza cada 1 segundo

    def actualizar(self, dt):
        p_antes = round(random.uniform(1.0, 5.0), 2)
        p_despues = round(random.uniform(0.5, 4.5), 2)
        diferencia = p_antes - p_despues

        self.presion_antes = f"{p_antes} kPa"
        self.presion_despues = f"{p_despues} kPa"

        if diferencia > UMBRAL_DIF:
            self.estado_texto = "⚠️ FILTRO LLENO ⚠️"
            self.color_estado = "#B30000"
        else:
            self.estado_texto = "✅ FILTRO LIMPIO ✅"
            self.color_estado = "#006600"

    def liberar_agua(self):
        # Simula limpieza reduciendo la diferencia de presión
        p_antes = random.uniform(1.5, 4.0)
        p_despues = p_antes - random.uniform(0.3, 1.0)
        self.presion_antes = f"{round(p_antes,2)} kPa"
        self.presion_despues = f"{round(p_despues,2)} kPa"
        self.estado_texto = "✅ FILTRO LIMPIO ✅"
        self.color_estado = "#006600"

class GotaApp(App):
    def build(self):
        self.title = "Gota de esperanza"
        return FiltroWidget()

if __name__ == "__main__":
    GotaApp().run()
