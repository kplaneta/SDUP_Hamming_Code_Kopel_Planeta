# This file performs encoding and decoding of Hamming (15,11) code.

import math


def insert_error(data, position):
    if position > 0:
        if data[position - 1] == 0:
            data[position - 1] = 1
        else:
            data[position - 1] = 0


def hamming_encode(data):
    # Get data bits
    d = list(data)
    d = [int(i) for i in d]

    # Calculate hamming bits
    p = [0, 0, 0, 0]
    p[0] = (d[0] + d[1] + d[3] + d[4] + d[6] + d[8] + d[10]) % 2
    p[1] = (d[0] + d[2] + d[3] + d[5] + d[6] + d[9] + d[10]) % 2
    p[2] = (d[1] + d[2] + d[3] + d[7] + d[8] + d[9] + d[10]) % 2
    p[3] = (d[4] + d[5] + d[6] + d[7] + d[8] + d[9] + d[10]) % 2

    encoded = [p[0], p[1], d[0], p[2], d[1], d[2], d[3], p[3], d[4], d[5], d[6], d[7], d[8], d[9], d[10]]

    return encoded


def hamming_decode(data):
    # Get data bits
    d = list(data)
    d = [int(i) for i in d]
    data_corrected = list(data)
    data_corrected = [int(i) for i in data_corrected]

    p = [d[0], d[1], d[3], d[7]]

    d.pop(7)
    d.pop(3)
    d.pop(1)
    d.pop(0)

    p[0] = (p[0] + d[0] + d[1] + d[3] + d[4] + d[6] + d[8] + d[10]) % 2
    p[1] = (p[1] + d[0] + d[2] + d[3] + d[5] + d[6] + d[9] + d[10]) % 2
    p[2] = (p[2] + d[1] + d[2] + d[3] + d[7] + d[8] + d[9] + d[10]) % 2
    p[3] = (p[3] + d[4] + d[5] + d[6] + d[7] + d[8] + d[9] + d[10]) % 2

    p_int = 0
    for i in range(len(p)):
        p_int += p[i] * math.pow(2, i)

    p_int = int(p_int)

    if p_int != 0:
        if data_corrected[p_int - 1] == 0:
            data_corrected[p_int - 1] = 1
        else:
            data_corrected[p_int - 1] = 0

    data_corrected.pop(7)
    data_corrected.pop(3)
    data_corrected.pop(1)
    data_corrected.pop(0)

    print("Error on position: ", p_int)
    return data_corrected


if __name__ == "__main__":

    encode_data = "11010111111" #11010111001
    print("Encode data:  ", [int(i) for i in list(encode_data)])
    encoded_data = hamming_encode(encode_data)
    print("Encoded data: ", encoded_data)
    decode_data = encoded_data
    insert_error(decode_data, 7)
    print("Decode data:  ", decode_data)
    # decode_data = [str(i) for i in decode_data]
    # print(''.join(decode_data))
    decoded_data = hamming_decode(decode_data)
    print("Decoded data: ", decoded_data)

    if [int(i) for i in list(encode_data)] == decoded_data:
        print("OK !")
