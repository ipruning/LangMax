def callback(n):
    print("Sum = {}".format(n))


def main(a, b, _callback=None):
    print("adding {} + {}".format(a, b))
    if _callback:
        _callback(a + b)


main(1, 3)
main(1, 2, callback)
