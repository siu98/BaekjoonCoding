//백준 1439(c++) : 뒤집기

#include <iostream>
using namespace std;

int zeroCnt;
int oneCnt;
int main(){
    string S;
    cin >> S;
    for (int i=0; i<S.size(); ++i){
        if (S[i] != S[i+1]){
            if(S[i]=='0')
                zeroCnt++;
            else
                oneCnt++;
        }
    }
    cout << min(zeroCnt, oneCnt) << endl;
}

