def odd_numbers(start=0, end=100):
    print("Printing odd numbers from {} to {}".format(start, end))
    for i in range(start, end):
        if i % 2 != 0:
            print(i)

def hello_world():
    print("Hello World")

if __name__ == "__main__":
    hello_world()