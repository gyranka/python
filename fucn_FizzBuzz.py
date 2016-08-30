def newfunct(start, end, step):
    while start <= end:
        if start % 3 == 0 and start % 5 == 0:
            print("FizzBuzz")
        elif start % 3 == 0:
            print("Buzz")
        elif start % 5 == 0:
            print("Fizz")
        else:
            print(start)
        start = start + step
