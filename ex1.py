numbers = [int(i) for i in input().split(' ')]

last_zero_index = None
current_number_index = 0

while current_number_index < len(numbers):
    if numbers[current_number_index] != 0 and last_zero_index:
        numbers[current_number_index], numbers[last_zero_index] = numbers[last_zero_index], numbers[current_number_index]
        current_number_index = last_zero_index
        last_zero_index = None

    if numbers[current_number_index] == 0 and not last_zero_index:
        last_zero_index = current_number_index

    current_number_index += 1

for number in numbers:
    print(number, end=' ')