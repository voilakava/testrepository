def find_divisor_of_num(number):
    if 3 >= number > 0:
        return number
    else:
        for dlit in range(1, number + 1):
            if number % dlit == 0:
                print('divisors of {} is {}'.format(number, dlit))


find_divisor_of_num(int(input('введите число')))

print('hallo world')