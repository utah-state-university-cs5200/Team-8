import pickle


def decode(recv_obj):
    return pickle.loads(recv_obj)
