'''
This is to encode and decode values using base64
'''
import base64


def encode_string(i):
    '''
    encode a string using base64
    '''
    print('encode input value: ' + i)
    encoded_value = base64.b64encode(i.encode())
    print('base64 encoded value in bytes: ' + str(encoded_value))


def decode_string(i):
    '''
    decode a string using base64
    '''
    print('decode input value: ' + i)
    decoded_value = base64.b64decode(i).decode('utf-8')
    print('base64 decoded value in utf-8: ' + str(decoded_value))

print('starting encode/decode utility')
print('enter e to encode or d to decode:')
i_mode = input()

if i_mode == 'e':
    print('enter string to encode:')
    i_encode = input()
    encode_string(i_encode)
elif i_mode == 'd':
    print('enter string to decode:')
    i_decode = input()
    decode_string(i_decode)
else:
    print('invalid input.  enter e or d.  exiting.')
