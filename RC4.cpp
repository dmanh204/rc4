#include <iostream>
using namespace std;

class RC4{
    public: 
        int S[255];
        int T[255];
        RC4(int key[]){
        initialize(key);
        a = 0;
        b = 0;
    }
    private: 
        int a;
        int b;

    
    private: void initialize(int K[]){
        int length = sizeof(K)/sizeof(K[0]);
        for (int i = 0; i < 255; i++){
            S[i] = i;
            T[i] = K[i%length];
        }
        // Initialize first S
        int j = 0;
        int temp = 0;
        for (int i = 0; i < 255; i++){
            j = (j + S[i] +T[i])%256;
            // Swap
            temp = S[i];
            S[i] = S[j];
            S[j] = temp;
        }
    }
    public: int Generate(){
        a = (a+1)%256;
        b = (b+S[a])%256;
        // Swap
        int temp = S[a];
        S[a] = S[b];
        S[b] = temp;

        int t = (S[a]+S[b])%256;
        return S[t];
    }
};