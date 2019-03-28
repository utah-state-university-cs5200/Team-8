import json

from src.communications.messages.message_factory import MessageFactory


class DecodeError(Exception):
    pass


class EncodeError(Exception):
    pass


def encode(message):
    try:
        return decoding(message.getAttributes())
    except Exception as e:
        raise EncodeError(e)


def decode(message_string):
    try:
        unpacked_dict = decoding(message_string)
        return MessageFactory.build(**unpacked_dict)
    except Exception as e:
        raise DecodeError(e)


def encoding(subject):
    return json.dumps(subject).encode()


def decoding(message_string):
    return json.loads(message_string.decode())
