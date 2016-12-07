"""
Take input of directions and distance and return the final distance

Story:
Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by
stars.
Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to
retrieve all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the advent calendar; the second
puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get
- the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work
them out further.

The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then,
follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks
, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the
destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the
destination?

For example:

Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.
How many blocks away is Easter Bunny HQ?

Source : [http://adventofcode.com/2016/day/1]

"""

instructions = "R1, R1, R3, R1, R1, L2, R5, L2, R5, R1, R4, L2, R3, L3, R4, L5, R4, R4, R1, L5, L4, R5, R3, L1, R4, " \
               "R3, L2, L1, R3, L4, R3, L2, R5, R190, R3, R5, L5, L1, R54, L3, L4, L1, R4, R1, R3, L1, L1, R2, L2, " \
               "R2, R5, L3, R4, R76, L3, R4, R191, R5, R5, L5, L4, L5, L3, R1, R3, R2, L2, L2, L4, L5, L4, R5, R4, " \
               "R4, R2, R3, R4, L3, L2, R5, R3, L2, L1, R2, L3, R2, L1, L1, R1, L3, R5, L5, L1, L2, R5, R3, L3, R3, " \
               "R5, R2, R5, R5, L5, L5, R2, L3, L5, L2, L1, R2, R2, L2, R2, L3, L2, R3, L5, R4, L4, L5, R3, L4, R1, " \
               "R3, R2, R4, L2, L3, R2, L5, R5, R4, L2, R4, L1, L3, L1, L3, R1, R2, R1, L5, R5, R3, L3, L3, L2, R4, " \
               "R2, L5, L1, L1, L5, L4, L1, L1, R1"


def check_intersection(x, y):
    """
    Given a array of moves check for intersections
    :param x:
    :param y:
    :return:
    """
    for i in range(len(x)):
        if i < 4:
            pass
        else:
            for j in range(1, i-3):
                if (x[j-1] <= x[i] <= x[j] or x[j-1] >= x[i] >= x[j]) and (y[i] <= y[j] <= y[i-1] or y[i] >= y[j] >= y[i-1]) :
                    print(x[i], y[j], abs(x[i])+abs(y[j]))
                    return 1
                elif (y[j-1] <= y[i] <= y[j] or y[j-1] >= y[i] >= y[j]) and (x[i] <= x[j] <= x[i-1] or x[i] >= x[j] >= x[i-1]):
                    print(x[j], y[i], abs(x[j])+abs(y[i]))
                    return 1
                else:
                    pass


def track_steps(steps):
    """
    given steps find the final point
    :param steps:
    :return:
    """
    count = 0  # guy starts facing north
    x = []
    y = []
    x.append(0)
    y.append(0)
    x_tmp = 0
    y_tmp = 0
    turns = 0
    for step in steps:
        turns += 1
        step = step.strip()
        direction = step[0]
        number = step[1:]

        if direction == 'R':
            sym = 1
        else:
            sym = -1
        if count == 0:
            x_tmp += sym*int(number)
            count += sym
        elif count == 1:
            y_tmp += -1*sym*int(number)
            count += sym
        elif count == 2:
            x_tmp += -1*sym*int(number)
            count += sym
        else:
            y_tmp += sym*int(number)
            count += sym
        x.append(x_tmp)
        y.append(y_tmp)
        count %= 4
    print(x[turns], y[turns], abs(x[turns])+abs(y[turns]))
    return x, y


def take_input(default=None):
    """
    Take the input and read it
    :return:
    """
    if not default:
        steps = input('-->')
        steps = str(steps)
    else:
        steps = default
    steps = steps.split(',')
    return steps


def main():
    data = take_input(instructions)
    [x, y] = track_steps(data)
    check_intersection(x, y)


if __name__ == '__main__':
    main()

