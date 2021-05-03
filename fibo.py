
def recursive_nth_fibo(n):

    if n <= 1:
        return 1

    else:
        return (recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2))


def main():
    number = int(input("Kolko prvkov FS chces?"))
    # vypis FS
    fs = [recursive_nth_fibo(n) for n in range(number)]
    print(fs)
    # sucet FS
    fibo = recursive_nth_fibo(4)
    print(fibo)

if __name__ == '__main__':
    main()
