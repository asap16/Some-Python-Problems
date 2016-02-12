def TwosComplement(s1):
    exchange_num = NumConversion(s1)
    dec_1 = BinaryToDec(exchange_num)
    twos_comp_dec = dec_1 + 1
    result_twos_comp = DecToBinary(twos_comp_dec)
    return result_twos_comp


def NumConversion(s1):
    is_reversed = ''
    for i in range(len(s1)):
        if s1[i] == '0':
            is_reversed += '1'
        elif s1[i] == '1':
            is_reversed += '0'
    print (is_reversed)
    return is_reversed

def BinaryToDec(binary):
    power = 0
    binary = str(binary)
    decimal = 0
    for i in range(len(binary)-1,0,-1):
        decimal += ((int(binary[i])*(2**power)))
        power += 1
    print(decimal)
    return decimal

def DecToBinary(decimal):
    num = decimal
    binary = ''
    quotient = num // 2
    while quotient != 0:
        quotient = num // 2
        rem = num % 2
        num = quotient
        binary = str(rem) + binary
    return binary

print(TwosComplement('1010'))
