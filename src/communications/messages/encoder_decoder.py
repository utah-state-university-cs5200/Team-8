import json


class DecodeError(Exception):
    pass


class EncodeError(Exception):
    pass


def encoding(subject):
    try:
        return json.dumps(subject).encode()
    except Exception as e:
        raise EncodeError(e)


def decoding(message_string):
    try:
        return json.loads(message_string.decode())
    except Exception as e:
        raise DecodeError(e)
