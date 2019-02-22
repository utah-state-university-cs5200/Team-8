import struct
import json
'''
submitting clue message
  int, int, str, str <=> message_type_id, player_id, clue string, associated word
declare contact message
    int, int, int, str <=> message_type_id, player_id, clue_id, associated word
'''

class DumbyClass():
    def __init__(self):
        self.a='fart'
        self.b=4
        self.c={'a':2,'b':'largesse'}

def decoder(message_byte_string):
    message_type = struct.unpack_from('i', message_byte_string, 0)
    output_message = [message_type[0]]
    print(output_message)
    message_format = msg_format_dict[output_message[0]]
    print(output_message)

def encoder(message_tuple):
    format_tuple = msg_format_dict[message_tuple[0]]
    format_string = ''
    print( [type(ele) for ele in message_tuple])
    message_list =[]
    for index in range(len(format_tuple)):
        element = format_tuple[index]
        if 's' in element:
            format_string += element%len(message_tuple[index])
            message_list.append(len(message_tuple[index]))
            message_list.append(message_tuple[index])
            continue
        format_string += element
        message_list.append(message_tuple[index])
    encoding = struct.pack(format_string, *message_tuple)
    return encoding

def jencoder(message_tuple):
    return json.dumps(message_tuple)

def jdecoder(message_string):
    return json.loads(message_string)

msg_format = 'ii'+'6s'+'4s'
msg_format_dict = {
    1:('i','i', 'i' ,'%ds', 'i', '%ds'),
    2:('i','i', 'i', 'i', '%ds')
}



# encoded = struct.pack(msg_format, 1, 1, b'flatus', b'fart')
# # encoded = struct.pack(msg_format,( 1, 1, 'flatus', 'fart'))
# print(encoded)
# decoded = struct.unpack(msg_format, encoded)
# print(decoded)

if __name__ == '__main__':
    result1 = jencoder((1,1,'bean noises', 'fart'))
    print(jdecoder(result1))
    result2 = jencoder((2,3,1, 'fart noises'))
    print(jdecoder(result2))
    test_obj = DumbyClass()
    result3 = jencoder(test_obj)
    print(result3)
    print(jdecoder(result3))
