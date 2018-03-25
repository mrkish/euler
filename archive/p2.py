import eulerlib

def main():
    values = eulerlib.fibonacci.fibo_less_than(4000000,1)

    sum = 0

    for item in values:
        if item % 2 == 0:
            sum += item

    print(sum)

if __name__ == "__main__":
    main()