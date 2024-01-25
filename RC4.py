mod=10
# Initialization
S = []
T = []
def initialization(key, keylen):
    for i in range(mod):
        S.append(i)
        T.append(key[i % keylen])
# Initialization    
    j = 0
    for i in range(mod):
        j = (j + S[i] + T[i])%mod
        S[i], S[j] = S[j], S[i]

def Generate():
    i = j = 0
    i = (i+1)%mod
    j = (j+S[i])%mod
    S[i],S[j] = S[j], S[i]
    t = (S[i] +S[j])%mod
    return S[t]
key = [1,2,3,6]
initialization(key, 4)
for i in range(10):
    print(Generate())
    