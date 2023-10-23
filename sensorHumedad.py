import paho.mqtt.client as mqtt
import random
import time

# Definir los detalles del broker MQTT
broker_address = "ffab79b43fa54fe9bfbba352bebdd51b.s1.eu.hivemq.cloud"
port = 8883  # Puerto seguro MQTT estándar
username = "MemoArguello"  # Reemplaza con tu nombre de usuario
password = "Hamburguesa98"  # Reemplaza con tu contraseña
topic = "sensor/temperatura"

# Callback cuando se establece la conexión con el broker
def on_connect(client, userdata, flags, rc):
    print("Conectado con el código de resultado: " + str(rc))

def on_message(client, userdata, message):
    global enviar_temperatura
    payload = message.payload.decode()
    

# Crear un cliente MQTT
client = mqtt.Client()

# Establecer el callback de conexión
client.on_connect = on_connect
client.on_message = on_message

# Configurar la seguridad para el puerto seguro MQTT (TLS)
client.tls_set()

client.username_pw_set(username, password)

# Conectar al broker
client.connect(broker_address, port, 60)

client.subscribe(topic)

# Mantener la conexión activa
client.loop_start()

# Simular un sensor de humedad que envía datos al broker
while True:
    humidity = round(random.uniform(30, 70), 2)  # Humedad aleatoria entre 30% y 70%
    client.publish("sensor/humedad", f"{humidity} %")
    print(f"Humedad enviada: {humidity} %")
    time.sleep(5)  # Esperar 5 segundos antes de enviar la próxima actualización
