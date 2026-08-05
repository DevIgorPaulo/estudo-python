def even_sum(beginning, ending):
    counter = beginning
    total = 0

    while counter <= ending:
        if counter % 2 == 0:
            total += counter

        counter += 1

    return total

total = even_sum(0, 10)
print(total)