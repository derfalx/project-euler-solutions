'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

https://projecteuler.net/problem=5
'''

max = 20 + 1
numbersOriginal = list(range(1, max))
numbers = list()

# Filter out numbers, which are multiples of a bigger number within numbersOriginal
index = max - 2
while index > 0:
    current = numbersOriginal[index]

    if current == -1:
        index -= 1
        continue

    next = index - 1

    while next > 0:
        if current % numbersOriginal[next] == 0:
            numbersOriginal[next] = -1
        next -= 1

    index -= 1

# Collect numbers left in a new list
print("numbers to divide by:")
for number in numbersOriginal:
    if not number == -1:
        numbers.append(number)
        print("\t{}".format(number))

dividable = False
factor = 2
max = len(numbers)

# Find the smallest possible number
while not dividable:
    sample = factor * max
    index = 1
    dividable = True
    while dividable and index < (max - 1):
        dividable &= (sample % numbers[index]) == 0
        index += 1
    factor += 1

print("Found the smallest: {}".format(sample))
