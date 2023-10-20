import paho.mqtt.client as mqtt

# Definir los detalles del broker MQTT
broker_address = "ffab79b43fa54fe9bfbba352bebdd51b.s1.eu.hivemq.cloud"
port = 8883  # Puerto seguro MQTT estándar
username = "MemoArguello"  # Reemplaza con tu nombre de usuario
password = "Hamburguesa98"  # Reemplaza con tu contraseña

# Callback cuando se recibe un mensaje en el tema suscrito
def on_message(client, userdata, message):
    print(f"Temperatura recibida: {message.payload.decode()}")

# Crear un cliente MQTT
client = mqtt.Client()

# Establecer el callback de mensaje
client.on_message = on_message 

# Establecer la seguridad para el puerto seguro MQTT (TLS)
client.tls_set()  # Esto activa el uso de TLS

client.username_pw_set(username, password)  

# Conectar al broker
client.connect(broker_address, port, 60)

# Suscribirse al tema del sensor de temperatura
client.subscribe("sensor/temperatura")

# Mantener la conexión activa
client.loop_forever()
