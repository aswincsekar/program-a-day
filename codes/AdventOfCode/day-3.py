"""
Many triangles for you
"""


def check_valid_triangle(sides):
    checked = list(filter(lambda x: (x[0] < x[1]+x[2])and(x[1] < x[0]+x[2])and(x[2] < x[0]+x[1]), sides))
    print(len(checked))


def get_input(method):
    with open('data/day-3-data') as data:
        dat = data.read()
        dat = str(dat)
        dat = dat.split("\n")
        dat = [sides.split() for sides in dat]
        dat = [list(map(lambda x: int(x), sides)) for sides in dat]
        if method == 1:
            return dat
        else:
            new_dat = []
            l = len(dat)
            for i in range(3*l):
                p = int(i%l)
                q = int(i/l)
                if p % 3 == 0:
                    tmp = []
                tmp.append(dat[p][q])
                if p % 3 == 2:
                    new_dat.append(tmp)
            return new_dat


def main():
    method = 2
    sides = get_input(method)
    print(len(sides))
    check_valid_triangle(sides)

if __name__ == '__main__':
    main()