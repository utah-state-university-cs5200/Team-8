import json

def encoder(message_data):
    return json.dumps(message_data).encode()

def decoder(message_string):
    return json.loads(message_string.decode())
