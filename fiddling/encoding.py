import json

def encoder(message_tuple):
    return json.dumps(message_tuple).encode()

def decoder(message_string):
    return json.loads(message_string.decode())
