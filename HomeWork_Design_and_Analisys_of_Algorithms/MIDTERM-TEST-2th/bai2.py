# số thuận nghịch
def is_palindrome(num_str):
    return num_str[-7:] == num_str[-7:][::-1]

def is_type_i(num_str):
    return is_palindrome(num_str[-7:])

def is_type_ii(num_str):
    sum = 0
    for e in num_str[-7:-4]:
        sum += int(e)
    for e in num_str[-3:]:
        sum += int(e)
    return is_type_i(num_str) and sum % 10 == 0

def is_type_iii(num_str):
    return is_type_ii(num_str) and '0' not in num_str[-7:]


def write_numbers(filename, numbers):
    with open(filename, 'w') as f:
        for i in range(0, len(numbers), 8):
            f.write(' '.join(numbers[i:i+8]) + '\n')

type_i_numbers = []
type_ii_numbers = []
type_iii_numbers = []

for n in range(2, 9):
    for num in range(100000, 1000000):
        num_str = f"091{n}.{num // 1000:03d}.{num % 1000:03d}"
        if is_type_i(num_str):
            type_i_numbers.append(num_str)
            if is_type_ii(num_str):
                type_ii_numbers.append(num_str)
                if is_type_iii(num_str):
                    type_iii_numbers.append(num_str)

write_numbers("Loai1.out", [num for num in type_i_numbers if num not in type_ii_numbers])
write_numbers("Loai2.out", [num for num in type_ii_numbers if num not in type_iii_numbers])
write_numbers("Loai3.out", type_iii_numbers)
