def ConvertTime(time, difference):
    delimiter = ':'
    time = time.split(delimiter)
    difference = difference.split(delimiter)

    sum_of = int(time[1]) + int(difference[1])
    result = ''
    if sum_of >= 60:
        carry = 1
        rem = sum_of - 60
        result += ':' + str(rem)
    elif sum_of <= 60:
        carry = 0
        result += ':' + str(sum_of)
    converted_hour = int(time[0]) + int(difference[0]) + carry
    converted_time = str(converted_hour) + result
    return converted_time

print(ConvertTime('12:45', '3:45'))
