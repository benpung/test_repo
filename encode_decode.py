'''
This is to encode and decode values using base64
'''
import base64


def encode_string(i):
    '''
    encode a string using base64
    '''
    print('encode input value: ' + i)
    encoded_value = base64.b64encode(b,i)
    print('base64 encoded value in bytes: ' + encoded_value)


def decode_string(i):
    '''
    decode a string using base64
    '''
    print('decode input value: ' + i)
    encoded_value = base64.b64decode(i).decode('utf-8')
    print('base64 decoded value in utf-8: ' + encoded_value)

print('starting encode/decode utility')
print('enter E to encode or D to decode:')
i_mode = input()

if i_mode == 'E':
    print('enter string to encode:')
    i_encode = input()
    encode_string(i_encode)
elif i_mode == 'D':
    print('enter string to decode:')
    i_decode = input()
    decode_string(i_decode)
else:
    print('invalid input.  enter E or D.')
    exit
