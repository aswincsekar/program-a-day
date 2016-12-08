"""
story:
Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy
data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a
checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties
broken by alphabetization. For example:

aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y,
 and z, which are listed alphabetically.
a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are
listed alphabetically.
not-a-real-room-404[oarel] is a real room.
totally-real-room-200[decoy] is not.
Of the real rooms from the list above, the sum of their sector IDs is 1514.

--- Part Two ---

With all the decoy data out of the way, it's time to decrypt this list and get moving.

The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software.
 However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like
  yourself.

To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID.
 A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.
"""
import re
import functools


def generate_checksum(words):
    """
    generate checksum or five most occuring alphabets
    :param words:
    :return:
    """
    count = sorted([(-1*words.count(x), x) for x in set(words)])
    checksum = functools.reduce((lambda x, y: (1, x[1]+y[1])), count[:4])
    return checksum[1]


def check_parity(datum):
    """
    Receive datum and check parity
    :param datum:
    :return:
    """
    checksum = datum[-1]
    id = datum[-2]
    sentence = functools.reduce((lambda x, y: x + y), datum[:-2])
    gen_checksum = generate_checksum(sentence)
    # print(gen_checksum, checksum)
    return checksum == gen_checksum


def get_input():
    with open("data/day-4-data") as file:
        data = file.read()
        data = data.split('\n')
        data = [re.split('[-[]+', dat[:-2]) for dat in data]
        # print(data)
        return data


def rotate_word(word, n):
    word = word.lower()
    output = ""
    for ch in word:
        output += (chr((ord(ch) - 96 + n) % 26 + 96))
    return output


def rotate_name(room_name):
    n = int(room_name[-2]) % 26
    sentence = []
    for word in room_name[:-2]:
        sentence.append(rotate_word(word, n))
    if "northpole" in sentence and "objects":
        print("northpole objects are in "+room_name[-2])


def main():
    data = get_input()
    correct_rooms = list(filter(lambda x: check_parity(x), data))
    sum_id = 0
    for rooms in correct_rooms:
        sum_id += int(rooms[-2])
        rotate_name(rooms)
    print("sum_id:"+sum_id)

if __name__ == '__main__':
    main()
