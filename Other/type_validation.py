a = '10'
b = 10


def type_match(x, y):
    try:
        if int(x) == y:
            print("Value matches")
        else:
            print("value don't match")
    except Exception as e:
        print("exctp: ", e)


if __name__ == '__main__':
    type_match(a, b)
