import csv
import random

class Chatbot:
    def __init__(self):
        self.historial = []

    def saludar(self):
        return "Soy un chatbot. ¿En qué puedo ayudarte?"

    def contar_chiste(self):
        chistes = [
            "¿Cuál es el último animal que subió al arca de Noé? El del-fin.",
            "Sí los zombies se deshacen con el paso del tiempo ¿zombiodegradables?",
            "¿Qué le dice un techo a otro? Techo de menos.",
            "¿Cómo se llama hacer dieta en chino? Kita Kilito.",
            "¿Cómo se despiden los químicos? Ácido un placer.",
            "¿Cómo se dice no en Sudáfrica? Mopongo.",
        ]
        return random.choice(chistes)

    def responder_pregunta(self, pregunta):
        return "Lo siento, no entendí tu pregunta."
    
    def guardar_conversacion(self, usuario, tipo, mensaje):
        with open(f'{usuario}_historial.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([f"{tipo} - {mensaje}"])