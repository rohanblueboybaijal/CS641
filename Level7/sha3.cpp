#include <bits/stdc++.h>

using namespace std;

int main(){

    string str; 
    cout << "Enter the string to be hashed: ";
    getline(cin,str);
    
    char hexa[16] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};

    uint64_t str_length = str.length();
    uint64_t b = 1600;
    uint64_t l = 512;
    uint64_t c = 1024;
    uint64_t r = 576;
    int rounds = 24;
    int i, j, k;


    uint64_t state[5][5][64], tempstate[5][5][64];

    for(i = 0; i < 5; ++i)
        for(j = 0; j < 5; ++j)
            for(k = 0; k < 64; ++k)
                state[i][j][k] = 0;

    uint64_t message[r];

    k = 0;
    for(i = 0; i < str_length; ++i){
        for(j = 7; j >= 0; --j){
            if(((str[i] >> j) & 1) == 1)
                message[k] = 1;
            else
                message[k] = 0;
            ++k;
        }
    }

    while(k < r){
        message[k] = 0;
        ++k;
    }

    for(k = 0; k < r; ++k)
        state[k/(64*5)][(k/64) % 5][k%64] = message[k];


    uint64_t current_round = 0;
    uint64_t column_parity[5][64];

    while(current_round < rounds){
        //theta operation
        for(i = 0; i < 5; ++i){
            for(k = 0; k < 64; ++k){
                column_parity[i][k] = 0;
                for(j = 0; j < 5; ++j)
                    column_parity[i][k] ^= state[i][j][k];
            }
        }

        for(i = 0; i < 5; ++i){
            for(j = 0; j < 5; ++j){
                for(k = 0; k < 64; ++k){
                    state[i][j][k] ^= column_parity[(i+4)%5][k] ^ column_parity[(i+1)%5][k];
                    tempstate[i][j][k] = state[i][j][k];
                }
            }
        }

        //pi operation
        for(i = 0; i < 5; ++i)
            for(j = 0; j < 5; ++j)
                for(k = 0; k < 64; ++k)
                    state[j][((2 * i) + (3 * j)) % 5][k] = tempstate[i][j][k];
        

        //chi operation
        for(i = 0; i < 5; ++i)
            for(j = 0; j < 5; ++j)
                for(k = 0; k < 64; ++k)
                    tempstate[i][j][k] = state[i][j][k];


        for(i = 0; i < 5; ++i)
            for(j = 0; j < 5; ++j)
                for(k = 0; k < 64; ++k)
                    state[i][j][k] = tempstate[i][j][k] ^ (~tempstate[i][(j+1)%5][k] & tempstate[i][(j+2)%5][k]);

        ++current_round;
    }

    uint64_t index;

    k = 0;
    while(k < l){

        index = 0;
        for(j = 3; j >= 0; --j)
            index = index*2 + state[k/(64*5)][(k/64)%5][k%64 + j];
        printf("%c", hexa[index]);
        k += 4;
        if(k == 256)
            printf("\n");
    }

    return 0;
}
