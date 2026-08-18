def countdown(number):
    print(number)

    if(number > 1):
        countdown(number - 1)

countdown(10)