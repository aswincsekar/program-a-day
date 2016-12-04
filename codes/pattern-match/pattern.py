

def match_pattern(a, b):
    """
     method to take two strings to match the strings
    inputs : string A, string B
    :return: [bool, x, y]
    """
    l = len(b)
    for i in range(len(a)-l):
        if a[i:i+l] == b:
            print (i, i+l-1)
