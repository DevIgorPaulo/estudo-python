def sum_until(beginning, ending):
    total = 0
    counter = beginning + 1

    while counter < ending:
        total += counter
        counter += 1

    return total

result = sum_until(1, 10)
print(result)