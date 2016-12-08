"""

Story:

You arrive at Easter Bunny Headquarters under cover of darkness. However, you left in such a rush that you forgot to
use the bathroom! Fancy office buildings like this one usually have keypad locks on their bathrooms, so you search the
front desk for the code.

"In order to improve security," the document you find says, "bathroom codes will no longer be written down. Instead,
please memorize and follow the procedure below to access the bathrooms."

The document goes on to explain that each button to be pressed can be found by starting on the previous button and
moving to adjacent buttons on the keypad: U moves up, D moves down, L moves left, and R moves right. Each line of
instructions corresponds to one button, starting at the previous button (or, for the first line, the "5" button);
press whatever button you're on at the end of each line. If a move doesn't lead to a button, ignore it.

You can't hold it much longer, so you decide to figure out the code as you walk to the bathroom. You picture a keypad
like this:

1 2 3
4 5 6
7 8 9
Suppose your instructions are:

ULL
RRDDD
LURDL
UUUUD
You start at "5" and move up (to "2"), left (to "1"), and left (you can't, and stay on "1"), so the first button is 1.
Starting from the previous button ("1"), you move right twice (to "3") and then down three times (stopping at "9" after two moves and ignoring the third), ending up with 9.
Continuing from "9", you move left, up, right, down, and left, ending with 8.
Finally, you move up four times (stopping at "2"), then down once, ending with 5.
So, in this example, the bathroom code is 1985.

--- Part Two ---

You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many
fancy conference rooms and water coolers on this floor) and go to punch in the code. Much to your bladder's dismay,
the keypad is not at all like you imagined it. Instead, you are confronted with the result of hundreds of man-hours of
bathroom-keypad-design meetings:

    1
  2 3 4
5 6 7 8 9
  A B C
    D

You still start at "5" and stop when you're at an edge, but given the same instructions as above, the outcome is very
different:

You start at "5" and don't move at all (up and left are both edges), ending at 5.
Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), ending at D.
Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
Finally, after five more moves, you end at 3.
So, given the actual keypad layout, the code would be 5DB3.
"""

instruction = ["DUURRDRRURUUUDLRUDDLLLURULRRLDULDRDUULULLUUUDRDUDDURRULDRDDDUDDURLDLLDDRRURRUUUDDRUDDLLDDDURLRDDDULRDUD"
               "DRDRLRDUULDLDRDLUDDDLRDRLDLUUUDLRDLRUUUDDLUURRLLLUUUUDDLDRRDRDRLDRLUUDUDLDRUDDUDLLUUURUUDLULRDRULURURDL"
               "DLLDLLDUDLDRDULLDUDDURRDDLLRLLLLDLDRLDDUULRDRURUDRRRDDDUULRULDDLRLLLLRLLLLRLURRRLRLRDLULRRLDRULDRRLRURD"
               "DLDDRLRDLDRLULLRRUDUURRULLLRLRLRRUDLRDDLLRRUDUDUURRRDRDLDRUDLDRDLUUULDLRLLDRULRULLRLRDRRLRLULLRURUULRLL"
               "RRRDRLULUDDUUULDULDUDDDUDLRLLRDRDLUDLRLRRDDDURUUUDULDLDDLDRDDDLURLDRLDURUDRURDDDDDDULLDLDLU",
"LURLRUURDDLDDDLDDLULRLUUUDRDUUDDUDLDLDDLLUDURDRDRULULLRLDDUDRRDRUDLRLDDDURDUURLUURRLLDRURDRLDURUDLRLLDDLLRDRRLURLRRUUL"
"LLDRLULURULRRDLLLDLDLRDRRURUUUDUDRUULDLUDLURLRDRRLDRUDRUDURLDLDDRUULDURDUURLLUDRUUUUUURRLRULUDRDUDRLLDUDUDUULURUURURUL"
"LUUURDRLDDRLUURDLRULDRRRRLRULRDLURRUULURDRRLDLRUURUDRRRDRURRLDDURLUDLDRRLDRLLLLRDUDLULUDRLLLDULUDUULLULLRLURURURDRRDRU"
"URDULRDDLRULLLLLLDLLURLRLLRDLLRLUDLRUDDRLLLDDUDRLDLRLDUDU",
"RRDDLDLRRUULRDLLURLRURDLUURLLLUUDDULLDRURDUDRLRDRDDUUUULDLUDDLRDULDDRDDDDDLRRDDDRUULDLUDUDRRLUUDDRUDLUUDUDLUDURDURDLLL"
"LDUUUUURUUURDURUUUUDDURULLDDLDLDLULUDRULULULLLDRLRRLLDLURULRDLULRLDRRLDDLULDDRDDRURLDLUULULRDRDRDRRLLLURLLDUUUDRRUUURD"
"LLLRUUDDDULRDRRUUDDUUUDLRRURUDDLUDDDUDLRUDRRDLLLURRRURDRLLULDUULLURRULDLURRUURURRLRDULRLULUDUULRRULLLDDDDURLRRRDUDULLR"
"RDURUURUUULUDLDULLUURDRDRRDURDLUDLULRULRLLURULDRUURRRRDUDULLLLLRRLRUDDUDLLURLRDDLLDLLLDDUDDDDRDURRL",
"LLRURUDUULRURRUDURRDLUUUDDDDURUUDLLDLRULRUUDUURRLRRUDLLUDLDURURRDDLLRUDDUDLDUUDDLUUULUUURRURDDLUDDLULRRRUURLDLURDULULR"
"ULRLDUDLLLLDLLLLRLDLRLDLUULLDDLDRRRURDDRRDURUURLRLRDUDLLURRLDUULDRURDRRURDDDDUUUDDRDLLDDUDURDLUUDRLRDUDLLDDDDDRRDRDUUL"
"DDLLDLRUDULLRRLLDUDRRLRURRRRLRDUDDRRDDUUUDLULLRRRDDRUUUDUUURUULUDURUDLDRDRLDLRLLRLRDRDRULRURLDDULRURLRLDUURLDDLUDRLRUD"
"DURLUDLLULDLDDULDUDDDUDRLRDRUUURDUULLDULUUULLLDLRULDULUDLRRURDLULUDUDLDDRDRUUULDLRURLRUURDLULUDLULLRD",
"UURUDRRDDLRRRLULLDDDRRLDUDLRRULUUDULLDUDURRDLDRRRDLRDUUUDRDRRLLDULRLUDUUULRULULRUDURDRDDLDRULULULLDURULDRUDDDURLLDUDUU"
"UULRUULURDDDUUUURDLDUUURUDDLDRDLLUDDDDULRDLRUDRLRUDDURDLDRLLLLRLULRDDUDLLDRURDDUDRRLRRDLDDUDRRLDLUURLRLLRRRDRLRLLLLLLU"
"RULUURRDDRRLRLRUURDLULRUUDRRRLRLRULLLLUDRULLRDDRDDLDLDRRRURLURDDURRLUDDULRRDULRURRRURLUURDDDUDLDUURRRLUDUULULURLRDDRUL"
"DLRLLUULRLLRLUUURUUDUURULRRRUULUULRULDDURLDRRULLRDURRDDDLLUDLDRRRRUULDDD"]

board = {
    "1": {
        "U": None,
        "D": "3",
        "L": None,
        "R": None
    },
    "2": {
        "U": None,
        "D": "6",
        "L": None,
        "R": "3"
    },
    "3": {
        "U": "1",
        "D": "7",
        "L": "2",
        "R": "4"
    },
    "4": {
        "U": None,
        "D": "8",
        "L": "3",
        "R": None
    },
    "5": {
        "U": None,
        "D": None,
        "L": None,
        "R": "6"
    },
    "6": {
        "U": "2",
        "D": "A",
        "L": "5",
        "R": "7"
    },
    "7": {
        "U": "3",
        "D": "B",
        "L": "6",
        "R": "8"
    },
    "8": {
        "U": "4",
        "D": "C",
        "L": "7",
        "R": "9"
    },
    "9": {
        "U": None,
        "D": None,
        "L": "8",
        "R": None
    },
    "A": {
        "U": "6",
        "D": None,
        "L": None,
        "R": "B"
    },
    "B": {
        "U": "7",
        "D": "D",
        "L": "A",
        "R": "C"
    },
    "C": {
        "U": "8",
        "D": None,
        "L": "B",
        "R": None
    },
    "D": {
        "U": "B",
        "D": None,
        "L": None,
        "R": None
    },
}


def change_pos_1(pos, step):
    """
    given a step and the current position, update the position
    :param pos:
    :param step:
    :return:
    """
    if step == "U":
        if pos >= 4:
            pos += -3
    elif step == "D":
        if pos <= 6:
            pos += 3
    elif step == "R":
        if pos % 3 != 0:
            pos += 1
    elif step == "L":
        if pos % 3 != 1:
            pos += -1
    else:
        raise("Unexpected Input. Please check the input instructions. Step:"+step)

    return pos


def get_number(commands, board_choice):
    """
    given information for a number on the numberpad find the number
    :return: integer [1-9, A-D]
    """
    if board_choice == 1:
        pos = 5
        for step in commands:
            pos = change_pos_1(pos, step)
    elif board_choice == 2:
        pos = "5"
        for step in commands:
            if board[pos][step]:
                pos = board[pos][step]
    return pos


def main():
    numbers = []
    board_choice = input("board 1 or 2 :")
    board_choice = int(board_choice)
    if board_choice != 1 and board_choice != 2:
        raise "Invalid board number"
    for commands in instruction:
        pos = get_number(commands, board_choice)
        numbers.append(pos)
    print(numbers)


if __name__ == '__main__':
    main()
