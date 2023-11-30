#include <stdio.h>

int main(){
    int stick = 64;
    int X;
    int cnt = 0;
    scanf("%d", &X);
    while(X>0){
        if(stick>X){
            stick = stick/2;
        }
        else{
            cnt ++;
            X = X - stick;
        }
    }
    printf("%d", cnt);
    return 0;
}