def even_numbers(start=0, end=100):
    print("Printing even numbers between {} and {}".format(start, end))
    for i in range(start, end):
        if i % 2 == 0:
            print(i)