import json

def encoding(subject):
    return json.dumps(subject).encode()

def decoding(message_string):
    return json.loads(message_string.decode())
