from RC4oop import RC4
key = [100, 90, 176, 211, 45, 73, 192, 153, 235, 111, 74, 32]
k = RC4(key)
text = ""

def byte2bin(int):
    string = ""
    for i in range(8):
        x = 0b00000001 << (7-i)
        x = x & int
        x = x >> (7-i)
        string += str(x)

    return string

# for _ in range(1000):
#     print(k.Generate())
for _ in range(125000):
    text += byte2bin(k.Generate())
with open("rc4.manh.txt", 'w') as f:
    f.write(text)