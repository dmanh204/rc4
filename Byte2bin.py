def byte2bin(int):
    string = ""
    for i in range(8):
        x = 0b00000001 << (7-i)
        x = x & int
        x = x >> (7-i)
        string += str(x)

    return string