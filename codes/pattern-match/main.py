import pattern


def main():
    a = raw_input('Enter A :')
    b = raw_input('Enter B :')
    if len(a) < len(b):
        print('B should not be longer than A')
    else:
        pattern.match_pattern(a, b)


if __name__ == '__main__':
    main()