#include <bits/stdc++.h>

using namespace std;

vector <char> hex_to_bin (int x){
    vector <char> ans(4);
    for (int i = 0; i < 4; i++) {
        ans[3-i] = '0' + (int(x/pow(2, i))%2);
    }
    return ans;
}

int main(){

    int final_arr[5][5][64];
    vector <int> ans(64);
    int done = 0;

    char hexa[16] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};

    string final_str_1 = "64E064E8000000008801800666E56A6CECE9E6EF66E56A6C8809820766E56A6C";
    string final_str_2 = "00080201000000008809820766E56A6C64E866E90000000064E064E800000000";

    vector<string> blocks; 

    for (int i = 0; i < 16; i++) {
        blocks.push_back("");
        for (int j = 0; j < 3; j++) {
            blocks[i] += final_str_1[i+16*j];
        }
    }

    for (int k = 0; k < 16; k++) {
        string s = blocks[k];
        vector <vector <char> > bin(3, vector <char> (4));
        for (int j = 0; j < 3; j++) {
            int x;
            for (int i = 0; i < 16; i++) {
                if (hexa[i] == s[j]) {
                    x = i;
                    break;
                }
            }
            bin[j] = hex_to_bin(x);
        }
        vector <string> temp(4);
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 3; j++) {
                temp[i] += bin[j][3-i];
            }
        }
        
        for (int i = 0; i < 4; i++) {
            if (temp[i] == "000"){ ans[4*k+i] = 0; done++; }
            if (temp[i] == "001"){ ans[4*k+i] = 1; done++; }
            if (temp[i] == "011"){ ans[4*k+i] = 2; done++; }
            if (temp[i] == "101"){ ans[4*k+i] = 3; done++; }
        }
    }

    // cout << done << endl; 
    // for (int i = 0; i < 64; i++) {
    //     cout << ans[i] << " ";
    // }

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            for (int k = 0; k < 64; k++) {
                final_arr[i][j][k] = 0;
            }
        }
    }
     
    for (int i = 0; i < 64; i++) {
        final_arr[0][0][i] = ans[i]/2;
        final_arr[0][1][i] = ans[i]%2;
    }

    uint64_t b = 1600;
    uint64_t l = 512;
    uint64_t c = 1024;
    uint64_t r = 576;
    int rounds = 24;
    int i, j, k;

    k = 0;
    while(k < 128){

        int index = 0;
        for(j = 0; j <= 7; ++j)
            index = index*2 + final_arr[k/(64*5)][(k/64)%5][k%64 + j];
        printf("%c", index);
        k += 8;
    }

    printf ("\n================================\n");

    uint64_t current_round = 0;
    uint64_t column_parity[5][64];

    int tempstate[5][5][64];

    while(current_round < rounds){
        //theta operation
        for(i = 0; i < 5; ++i){
            for(k = 0; k < 64; ++k){
                column_parity[i][k] = 0;
                for(j = 0; j < 5; ++j)
                    column_parity[i][k] ^= final_arr[i][j][k];
            }
        }

        for(i = 0; i < 5; ++i){
            for(j = 0; j < 5; ++j){
                for(k = 0; k < 64; ++k){
                    final_arr[i][j][k] ^= column_parity[(i+4)%5][k] ^ column_parity[(i+1)%5][k];
                    tempstate[i][j][k] = final_arr[i][j][k];
                }
            }
        }

        //pi operation
        for(i = 0; i < 5; ++i)
            for(j = 0; j < 5; ++j)
                for(k = 0; k < 64; ++k)
                    final_arr[j][((2 * i) + (3 * j)) % 5][k] = tempstate[i][j][k];
        

        //chi operation
        for(i = 0; i < 5; ++i)
            for(j = 0; j < 5; ++j)
                for(k = 0; k < 64; ++k)
                    tempstate[i][j][k] = final_arr[i][j][k];


        for(i = 0; i < 5; ++i)
            for(j = 0; j < 5; ++j)
                for(k = 0; k < 64; ++k)
                    final_arr[i][j][k] = tempstate[i][j][k] ^ (~tempstate[i][(j+1)%5][k] & tempstate[i][(j+2)%5][k]);

        ++current_round;
    }

    uint64_t index;

    k = 0;
    while(k < l){

        index = 0;
        for(j = 3; j >= 0; --j)
            index = index*2 + final_arr[k/(64*5)][(k/64)%5][k%64 + j];
        printf("%c", hexa[index]);
        k += 4;
        if(k%256 == 0)
            printf("\n");
    }

    // for (int x = 0; x < 4; x++) {

    //     string bits = "";
    //     if (x == 0) bits = "00";
    //     if (x == 1) bits = "01";
    //     if (x == 2) bits = "10";
    //     if (x == 3) bits = "11";

    //     for (int i = 0; i < 5; i++){
    //         for (int j = 0; j < 5; j++) {
    //             for (int k = 0; k < 64; k++) {
    //                 final_arr[i][j][k] = 0;
    //             }
    //         }
    //     }

    //     final_arr[0][0][0] = bits[0]-'0';
    //     final_arr[0][1][0] = bits[1]-'0';

    //     // cout << bits[0] << " " << final_arr[0][0][0] << ' ' << final_arr[0][1][0] << endl;
        
    //     uint64_t current_round = 0;
    //     uint64_t column_parity[5][64];

    //     while(current_round < rounds){
    //         //theta operation
    //         for(i = 0; i < 5; ++i){
    //             for(k = 0; k < 64; ++k){
    //                 column_parity[i][k] = 0;
    //                 for(j = 0; j < 5; ++j)
    //                     column_parity[i][k] ^= final_arr[i][j][k];
    //             }
    //         }

    //         for(i = 0; i < 5; ++i){
    //             for(j = 0; j < 5; ++j){
    //                 for(k = 0; k < 64; ++k){
    //                     final_arr[i][j][k] ^= column_parity[(i+4)%5][k] ^ column_parity[(i+1)%5][k];
    //                     tempstate[i][j][k] = final_arr[i][j][k];
    //                 }
    //             }
    //         }

    //         //pi operation
    //         for(i = 0; i < 5; ++i)
    //             for(j = 0; j < 5; ++j)
    //                 for(k = 0; k < 64; ++k)
    //                     final_arr[j][((2 * i) + (3 * j)) % 5][k] = tempstate[i][j][k];
            

    //         //chi operation
    //         for(i = 0; i < 5; ++i)
    //             for(j = 0; j < 5; ++j)
    //                 for(k = 0; k < 64; ++k)
    //                     tempstate[i][j][k] = final_arr[i][j][k];


    //         for(i = 0; i < 5; ++i)
    //             for(j = 0; j < 5; ++j)
    //                 for(k = 0; k < 64; ++k)
    //                     final_arr[i][j][k] = tempstate[i][j][k] ^ (~tempstate[i][(j+1)%5][k] & tempstate[i][(j+2)%5][k]);

    //         ++current_round;
    //     }
    //  }

    return 0;
}
