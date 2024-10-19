from math import inf

def divide(first, second):
    if second != 0:
        return first / second
    return inf


def main():
    print(divide(1, 3))
    print(divide(1, 0))


if __name__ == '__main__':
    main()