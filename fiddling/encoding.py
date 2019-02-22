import json

def encoder(message_tuple):
    return json.dumps(message_tuple)

def decoder(message_string):
    return json.loads(message_string)
